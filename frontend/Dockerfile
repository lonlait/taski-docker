# Use the official Node.js runtime as the base image
FROM node:18-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of the application code
COPY . .

# Build the React app for production
RUN npm run build

# Create directory for static files
RUN mkdir -p /frontend_static

# Copy built files to static directory
RUN cp -r build/* /frontend_static/

# Keep container running for Docker Compose
CMD ["tail", "-f", "/dev/null"] 