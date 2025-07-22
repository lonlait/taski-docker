# Taski - Task Management Application

A modern task management application built with Django REST API backend and React frontend, containerized with Docker.

## Features

- Create, edit, and delete tasks
- Mark tasks as completed
- Filter tasks by completion status
- Modern responsive UI
- RESTful API
- Docker containerization

## Architecture

- **Frontend**: React.js with Bootstrap
- **Backend**: Django REST Framework
- **Database**: PostgreSQL
- **Gateway**: Nginx reverse proxy
- **Containerization**: Docker & Docker Compose

## Quick Start

### Development

```bash
# Clone the repository
git clone <repository-url>
cd taski-docker

# Start the application
docker-compose up -d
```

The application will be available at `http://localhost:8080`

### Production

```bash
# Use production configuration
docker-compose -f docker-compose.production.yml up -d
```

## Project Structure

```
taski-docker/
├── frontend/          # React frontend application
├── backend/           # Django REST API
├── gateway/           # Nginx reverse proxy
├── docker-compose.yml # Development configuration
└── docker-compose.production.yml # Production configuration
```

## API Endpoints

- `GET /api/tasks/` - List all tasks
- `POST /api/tasks/` - Create a new task
- `PUT /api/tasks/{id}/` - Update a task
- `DELETE /api/tasks/{id}/` - Delete a task

## License

MIT License
