import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
    const [data, setData] = useState([]);
    // Figyelj az URL végére: /api/leaderboard/
    const VAR_URL = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

    useEffect(() => {
        fetch(VAR_URL)
            .then(res => res.json())
            .then(json => setData(json.results || json))
            .catch(err => console.error("Hiba:", err));
    }, [VAR_URL]);

    return (
        <div className="container mt-4">
            <h2 className="text-primary">Leaderboard</h2>
            <div className="card p-3 shadow-sm">
                <table className="table table-striped">
                    <thead className="table-dark">
                        <tr><th>Rank</th><th>User</th><th>Points</th></tr>
                    </thead>
                    <tbody>
                        {data.map((item, i) => (
                            <tr key={i}><td>{i + 1}</td><td>{item.username || "N/A"}</td><td>{item.points || 0}</td></tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default Leaderboard;