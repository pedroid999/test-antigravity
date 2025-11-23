# User Registration Service - Frontend

A React application for user registration, login, and profile management. This frontend interacts with the FastAPI backend to provide a complete user authentication system.

## Tech Stack

- **Framework**: [React](https://react.dev/)
- **Build Tool**: [Vite](https://vitejs.dev/)
- **Routing**: [React Router](https://reactrouter.com/)
- **State Management**: React Context API
- **Styling**: CSS Modules / Standard CSS

## Prerequisites

- **Node.js**: v18 or higher recommended
- **npm**: Installed with Node.js

## Setup Instructions

1.  Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

## Available Scripts

In the project directory, you can run:

### `npm run dev`

Runs the app in the development mode.\
Open [http://localhost:5173](http://localhost:5173) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm run build`

Builds the app for production to the `dist` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

### `npm run lint`

Runs ESLint to check for code quality and style issues.

## Project Structure

```
frontend/
├── src/
│   ├── components/      # Reusable UI components
│   ├── context/         # Context providers (e.g., AuthContext)
│   ├── pages/           # Application pages (Login, Register, Profile)
│   ├── App.jsx          # Main application component with routing configuration
│   └── main.jsx         # Entry point
├── public/              # Static assets
├── index.html           # HTML template
└── vite.config.js       # Vite configuration
```

## Backend Integration

This frontend is configured to communicate with the backend API running at `http://127.0.0.1:8000`.

**Important**: Ensure the backend server is running before starting the frontend application to enable full functionality (authentication, data fetching).
