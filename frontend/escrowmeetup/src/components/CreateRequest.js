// src/components/CreateRequest.js

import React, { useState } from 'react';

const CreateRequest = ({ username, onCreateRequest }) => {
  const [requestType, setRequestType] = useState('');
  const [time, setTime] = useState('');
  const [location, setLocation] = useState('');
  const [amount, setAmount] = useState('');

  const handleCreateRequest = () => {
    // Perform request creation logic (e.g., make API request)
    // Assume onCreateRequest function is passed as a prop to handle request creation
    onCreateRequest({ buyer_username: username, request_type: requestType, time, location, amount });
  };

  return (
    <div>
      <h2>Create Request</h2>
      <label>
        Request Type:
        <input type="text" value={requestType} onChange={(e) => setRequestType(e.target.value)} />
      </label>
      <br />
      <label>
        Time:
        <input type="text" value={time} onChange={(e) => setTime(e.target.value)} />
      </label>
      <br />
      <label>
        Location:
        <input type="text" value={location} onChange={(e) => setLocation(e.target.value)} />
      </label>
      <br />
      <label>
        Amount:
        <input type="text" value={amount} onChange={(e) => setAmount(e.target.value)} />
      </label>
      <br />
      <button onClick={handleCreateRequest}>Create Request</button>
    </div>
  );
};

export default CreateRequest;
