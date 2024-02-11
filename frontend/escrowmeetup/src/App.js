
// import React, { useState } from 'react';
// import './App.css';

// function App() {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [showButtons, setShowButtons] = useState(false);

//   const handleLogin = () => {
//     // Dummy check for demo purposes
//     if (email === 'user@example.com' && password === 'password') {
//       // Hide email and password fields
//       setShowButtons(true);
//     } else {
//       alert('Invalid email or password. Please try again.');
//     }
//   };

//   return (
//     <div className="login-container">
//       <input
//         type="email"
//         placeholder="Email"
//         required
//         value={email}
//         onChange={(e) => setEmail(e.target.value)}
//       />
//       <input
//         type="password"
//         placeholder="Password"
//         required
//         value={password}
//         onChange={(e) => setPassword(e.target.value)}
//       />
//       <button type="button" onClick={handleLogin}>Login</button>

//       {showButtons && (
//         <div className="buttons-container">
//           <button className="big-button red-button">Red Button</button>
//           <button className="big-button green-button">Green Button</button>
//         </div>
//       )}

//       <div className='page'>
//         <h1>HANDSHAKE</h1>
//         <button className='green-button'>CONFIRM PAYMENT</button>
//         <button className='red-button'>DENY PAYMENT</button>
//       </div>
//     </div>
//   );
// }

// export default App;
// src/App.js

// src/App.js

import React, { useState } from 'react';
import UserLogin from './components/UserLogin';
import CreateRequest from './components/CreateRequest';
import CurrentRequests from './components/CurrentRequests';

const App = () => {
  const [loggedInUser, setLoggedInUser] = useState(null);

  const handleLogin = (username) => {
    setLoggedInUser(username);
  };

  const handleCreateRequest = (requestData) => {
    // Implement logic to create a new request (e.g., make API request)
    console.log('Create Request:', requestData);
  };

  const handleConfirmDenyRequest = (requestId, status) => {
    // Implement logic to confirm/deny a request (e.g., make API request)
    console.log('Confirm/Deny Request:', requestId, status);
  };

  return (
    <div>
      <h1>Your Web Application</h1>
      {loggedInUser ? (
        <div>
          <p>Welcome, {loggedInUser}!</p>
          <CreateRequest username={loggedInUser} onCreateRequest={handleCreateRequest} />
          <CurrentRequests username={loggedInUser} onConfirmDenyRequest={handleConfirmDenyRequest} />
        </div>
      ) : (
        <UserLogin onLogin={handleLogin} />
      )}
    </div>
  );
};

export default App;

