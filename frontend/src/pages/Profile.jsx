import React from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

const Profile = () => {
    const { user, logout } = useAuth();
    const navigate = useNavigate();

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    if (!user) return <div>Loading...</div>;

    return (
        <div className="container">
            <h2>Profile</h2>
            <div className="profile-info">
                <p><strong>Full Name:</strong> {user.full_name}</p>
                <p><strong>Email:</strong> {user.email}</p>
                <p><strong>Status:</strong> {user.is_active ? 'Active' : 'Inactive'}</p>
            </div>
            <button onClick={handleLogout} className="logout-btn">Logout</button>
        </div>
    );
};

export default Profile;
