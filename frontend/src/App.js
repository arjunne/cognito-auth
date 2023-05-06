import React, { useState } from 'react';
import { Container, Button } from 'react-bootstrap';
import api from './api';
import LoginForm from './LoginForm';


const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLoginSuccess = () => {
    setIsLoggedIn(true);
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    setIsLoggedIn(false);
  };

  const renderLogin = () => {
    return <LoginForm onSuccess={handleLoginSuccess} />;
  };

  const renderLogout = () => {
    return (
      <div>
        <p>You are logged in.</p>
        <Button onClick={handleLogout} variant="outline-secondary">
          Logout
        </Button>
      </div>
    );
  };

  const checkLoggedIn = async () => {
    const accessToken = localStorage.getItem('access_token');
    if (!accessToken) {
      setIsLoggedIn(false);
      return;
    }

    try {
      const response = await api.get('/users/me', {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });

      if (response.status === 200) {
        setIsLoggedIn(true);
      }
    } catch (error) {
      setIsLoggedIn(false);
    }
  };

  // Call checkLoggedIn on component mount to check if user is already logged in
  React.useEffect(() => {
    checkLoggedIn();
  }, []);

  return (
    <Container className="mt-5">
      <h1>React App with FastAPI Backend</h1>
      {isLoggedIn ? renderLogout() : renderLogin()}
    </Container>
  );
};

export default App;