from queries.pool import pool
from models import UserOutWithPassword


class UserQueries:
    def get(self, email) -> UserOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    """
                        SELECT *
                        FROM users
                        WHERE email = %s
                        """,
                    [email],
                )
                try:
                    record = result.fetchone()
                    return UserOutWithPassword(
                        id=record[0],
                        name=record[1],
                        email=record[2],
                        password=record[3],
                        zipcode=record[4],
                        hashed_password=record[5],
                    )
                except Exception:
                    return {
                        "message": "Could not get user record for this user id"
                    }

    def get_by_id(self, id) -> UserOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                        SELECT *
                        FROM users
                        WHERE id = %s;
                        """,
                    [id],
                )
                try:
                    record = None
                    for row in cur.fetchall():
                        record = {}
                        for i, column in enumerate(cur.description):
                            record[column.name] = row[i]
                    return UserOutWithPassword(**record)
                except Exception:
                    return {
                        "message": "Could not get user record for this user id"
                    }

    def create_user(self, info, hashed_password) -> UserOutWithPassword:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                params = [
                    info.name,
                    info.email,
                    info.password,
                    info.zipcode,
                    hashed_password,
                ]
                cur.execute(
                    """
                        INSERT INTO users (name,email,password,zipcode,
                        hashed_password)
                        VALUES (%s, %s, %s, %s, %s)
                        RETURNING id, name, email, password, zipcode,
                        hashed_password
                    """,
                    params,
                )

                try:
                    record = None
                    row = cur.fetchone()
                    if row is not None:
                        record = {}
                        for i, column in enumerate(cur.description):
                            record[column.name] = row[i]
                    return UserOutWithPassword(**record)
                except Exception:
                    return {"message": "Email already exists"}

    def update_user(self, user_id, info):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                input = [
                    info.name,
                    info.email,
                    info.password,
                    info.zipcode,
                    user_id,
                ]
                cur.execute(
                    """
                        UPDATE users
                        SET name = %s,
                            email = %s,
                            password = %s,
                            zipcode = %s
                        WHERE id = %s
                        RETURNING id, name, email, password, zipcode
                    """,
                    input,
                )
                try:
                    record = None
                    for row in cur.fetchall():
                        record = {}
                        for i, column in enumerate(cur.description):
                            record[column.name] = row[i]
                    return record
                except Exception:
                    return {"message": "Update Failed"}
