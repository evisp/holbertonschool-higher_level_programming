# Use the official Alpine image from the Docker Hub
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Copy the config.txt file into the container
COPY config.txt /app/config.txt

# Define the command to run when the container starts
CMD ["echo", "Hello, World!"]
