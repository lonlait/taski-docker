#!/bin/bash

echo "Stopping and removing existing containers..."
docker-compose down

echo "Removing existing volumes..."
docker volume rm taski-docker_pg_data taski-docker_static 2>/dev/null || true

echo "Building and starting containers..."
docker-compose up --build

echo "Setup complete! Access your application at:"
echo "  - Frontend: http://localhost:8080"
echo "  - Backend API: http://localhost:8080/api/"
echo "  - Admin: http://localhost:8080/admin/" 