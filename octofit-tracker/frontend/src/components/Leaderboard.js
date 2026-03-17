import React, { useEffect, useState } from 'react';

const API_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboards/`;

function Leaderboard() {
  const [leaderboards, setLeaderboards] = useState([]);

  useEffect(() => {
    console.log('Fetching from:', API_URL);
    fetch(API_URL)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        console.log('Fetched leaderboards:', results);
        setLeaderboards(results);
      })
      .catch(err => console.error('Error fetching leaderboards:', err));
  }, []);

  return (
    <div className="container mt-4">
      <h2>Leaderboard</h2>
      <ul className="list-group">
        {leaderboards.map((entry, idx) => (
          <li className="list-group-item" key={entry.id || idx}>
            {entry.team ? entry.team.name : 'Team'}: {entry.points} Punkte
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Leaderboard;
