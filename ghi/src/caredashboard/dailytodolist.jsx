import React, { useState } from "react";
import { TextField, Button, List, ListItem, ListItemText } from "@mui/material";

const DailyTodoList = () => {
  const [task, setTask] = useState("");
  const [todos, setTodos] = useState([]);

  const addTodo = () => {
    if (task.trim() !== "") {
      setTodos([...todos, task]);
      setTask("");
    }
  };

  const removeTodo = (index) => {
    const newTodos = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  return (
    <div>
      <TextField
        label="Add a task"
        value={task}
        onChange={(e) => setTask(e.target.value)}
      />
      <Button onClick={addTodo}>Add</Button>

      {todos.length > 0 && (
        <List>
          {todos.map((todo, index) => (
            <ListItem key={index}>
              <ListItemText primary={todo} />
              <Button onClick={() => removeTodo(index)}>Remove</Button>
            </ListItem>
          ))}
        </List>
      )}
    </div>
  );
};

export default DailyTodoList;