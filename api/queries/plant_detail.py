import logging
from typing import Optional
from queries.pool import pool
from models import PlantIn, PlantOut
from acls import get_plant_details


class PlantRepository:
    def get_one(self, plant_id: int) -> Optional[PlantOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT *
                        FROM plants
                        WHERE id = %s;
                        """,
                        [plant_id]
                    )
                    record = result.fetchone()
                    return self.record_to_plant_out(record)
        except Exception as e:
            logging.error("Error in creating plant:", e)
            raise

    def delete(self, plant_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM plants
                        WHERE id = %s
                        """,
                        [plant_id]
                    )
                    return True
        except Exception as e:
            logging.error("Error in creating plant: %s", e)
            raise

    def update(self, plant_id: int, plant: PlantIn) -> PlantOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                    """
                    SELECT owner_id
                    FROM plants
                    WHERE id = %s;
                    """,
                    [plant_id]
                )
                    current_data = db.fetchone()
                    current_owner_id = current_data[0]
                    if current_data is None:
                        raise ValueError("Plant not found")
                    else:
                        details = get_plant_details(plant.species_id)
                        result = db.execute(
                            """
                            UPDATE plants
                            SET name = %s
                                , source = %s
                                , common_name = %s
                                , type = %s
                                , cycle = %s
                                , watering = %s
                                , sunlight = %s
                                , indoor = %s
                                , care_level = %s
                                , maintenance = %s
                                , description = %s
                                , hardiness = %s
                                , original_url = %s
                                , dimensions = %s
                                , owner_id = %s
                                , watering_schedule = %s
                            WHERE id = %s
                            RETURNING id, name, source, common_name, type, cycle, watering, sunlight,
                                indoor, care_level, maintenance, description, hardiness, original_url,
                                dimensions, owner_id, watering_schedule;
                            """,
                            [
                                plant.name,
                                plant.source,
                                details["common_name"],
                                details["type"],
                                details["cycle"],
                                details["watering"],
                                details["sunlight"],
                                details["indoor"],
                                details["care_level"],
                                details["maintenance"],
                                details["description"],
                                details["hardiness"],
                                details["original_url"],
                                details["dimensions"],
                                current_owner_id,
                                plant_id,
                                plant.watering_schedule
                            ]
                        )
                        if db.rowcount == 0:
                            raise ValueError("No updates made, plant data may be identical or plant not found")
                        plant_data = {
                        "id": plant_id,
                        "name": plant.name,
                        "source": plant.source,
                        "common_name": details["common_name"],
                        "type": details["type"],
                        "cycle": details["cycle"],
                        "watering": details["watering"],
                        "sunlight": details["sunlight"],
                        "indoor": details["indoor"],
                        "care_level": details["care_level"],
                        "maintenance": details["maintenance"],
                        "description": details["description"],
                        "hardiness": details["hardiness"],
                        "original_url": details["original_url"],
                        "dimensions": details["dimensions"],
                        "owner_id": current_owner_id,
                        "watering_schedule": plant.watering_schedule
                    }
                        print("Plant data:", plant_data)
                        return PlantOut(**plant_data)
        except Exception as e:
            logging.error("Error in updating plant: %s", e)
            raise

    def record_to_plant_out(self, record):
        return PlantOut(
                id=record[0],
                name=record[1],
                source=record[2],
                common_name=record[3],
                type=record[4],
                cycle=record[5],
                watering=record[6],
                sunlight=record[7],
                indoor=record[8],
                care_level=record[9],
                maintenance=record[10],
                description=record[11],
                hardiness=record[12],
                original_url=record[13],
                dimensions=record[14],
                owner_id=record[15],
                watering_schedule=record[16]
        )
