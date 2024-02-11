// src/components/CurrentRequests.js

import React, { useState, useEffect } from 'react';

const CurrentRequests = ({ username, onConfirmDenyRequest }) => {
  const [requests, setRequests] = useState([]);

  useEffect(() => {
    // Fetch current requests for the logged-in user
    // (e.g., make API request to get requests for a specific user)
    // Update the 'requests' state with the fetched data
  }, [username]);

  const handleConfirmDeny = (requestId, status) => {
    // Perform confirmation/denial logic (e.g., make API request)
    // Assume onConfirmDenyRequest function is passed as a prop to handle confirmation/denial
    onConfirmDenyRequest(requestId, status);
  };

  return (
    <div>
      <h2>Current Requests</h2>
      <ul>
        {requests.map((request) => (
          <li key={request.request_id}>
            <strong>Request ID:</strong> {request.request_id}<br />
            <strong>Buyer:</strong> {request.buyer_username}<br />
            <strong>Seller:</strong> {request.seller_username}<br />
            {/* Display other request details */}
            <button onClick={() => handleConfirmDeny(request.request_id, 'accept')}>Accept</button>
            <button onClick={() => handleConfirmDeny(request.request_id, 'deny')}>Deny</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CurrentRequests;
