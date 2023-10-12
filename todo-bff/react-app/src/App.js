import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [todos, setTodos] = useState([]);
  const [todoText, setTodoText] = useState('');

  useEffect(() => {
    axios.get('/api/todos')
      .then(response => setTodos(response.data));
  }, []);

  const addTodo = () => {
    axios.post('/api/todos', { text: todoText })
      .then(() => {
        setTodoText('');
        axios.get('/api/todos')
          .then(response => setTodos(response.data));
      });
  };

  const updateTodo = (index, text) => {
    axios.put(`/api/todos/${index}`, { text: text })
      .then(() => {
        axios.get('/api/todos')
          .then(response => setTodos(response.data));
      });
  };

  const deleteTodo = (index) => {
    axios.delete(`/api/todos/${index}`)
      .then(() => {
        axios.get('/api/todos')
          .then(response => setTodos(response.data));
      });
  };

  return (
    <div className="App">
      <h1>TODO App</h1>
      <input type="text" value={todoText} onChange={(e) => setTodoText(e.target.value)} />
      <button onClick={addTodo}>Add</button>
      <ul>
        {todos.map((todo, index) => (
          <li key={index}>
            <input
              type="text"
              value={todo.text}
              onChange={(e) => updateTodo(index, e.target.value)}
            />
            <button onClick={() => deleteTodo(index)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
