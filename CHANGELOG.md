# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-11-23

### Added
#### Documentation
- **Generation Process Section**: Added "Generación con Antigravity" section to `index.html` showcasing the agent's development process with screenshots.
- **Formatted Documentation Page**: Created `docs/documentation.html` to render `ANTIGRAVITY_CREATION.md` as a proper HTML page.
- **Enhanced Screenshots**: Improved the "Aplicación en Acción" section with larger cards and detailed feature lists.

### Changed
#### Documentation
- **Header Fix**: Improved text rendering for "Google Antigravity" in the header to fix blurriness.
- **Documentation Link**: Updated the "Leer Documentación Completa" link to point to the new HTML page instead of raw Markdown.
- **Visual Improvements**: Updated `styles.css` with new animations, card styles, and responsive layouts for the new sections.

## [0.1.0] - 2025-11-23

### Added

#### Backend
- FastAPI application with SQLModel for data modeling
- SQLite database integration
- User registration endpoint (`POST /users/register`)
- User login endpoint with JWT authentication (`POST /users/token`)
- Protected user profile endpoint (`GET /users/me`)
- Argon2 password hashing for secure credential storage
- JWT token generation and validation
- Comprehensive pytest test suite for all endpoints
- Python project setup using `uv` package manager

#### Frontend
- React application initialized with Vite
- User registration page with form validation
- User login page with authentication
- Protected user profile page
- AuthContext for centralized authentication state management
- React Router integration with protected routes
- Automatic token storage in localStorage
- Modern responsive UI with Vanilla CSS
- Smooth animations and transitions

#### Documentation
- Main README with setup instructions
- Backend API documentation
- Frontend component documentation
- Walkthrough with verification screenshots
- Project creation documentation explaining Antigravity agent development process

#### Configuration
- `.gitignore` files for backend and frontend
- Python version pinning (`.python-version`)
- ESLint configuration for frontend
- Vite configuration for optimal development

### Security
- JWT-based authentication system
- Argon2 password hashing algorithm
- Protected API routes requiring authentication
- Secure token validation and expiration

[0.2.0]: https://github.com/pedroid999/test-antigravity/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/pedroid999/test-antigravity/releases/tag/v0.1.0
