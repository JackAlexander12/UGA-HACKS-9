// src/components/UserLogin.js

import React, { useState } from 'react';

const UserLogin = ({ onLogin }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    // Perform user login logic (e.g., make API request)
    // Assume onLogin function is passed as a prop to handle successful login
    onLogin(username);
  };

  return (
    <div>
      <h2>User Login</h2>
      <label>
        Username:
        <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
      </label>
      <br />
      <label>
        Password:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label>
      <br />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default UserLogin;
