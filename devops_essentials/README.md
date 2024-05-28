# Docker Essentials

## 0. Create a Simple Docker Image Locally Based on Alpine

### Step 1: Create the Dockerfile
- Open the Dockerfile in your preferred editor (e.g., VS Code).
- Add the following content to the Dockerfile:
```bash
FROM alpine:latest
CMD ["echo", "Hello, World!"]
```

### Step 2: Build the Docker Image
- Open a terminal and make sure to be at the `docker-alpine-hello` directory 
- Build the Docker image using the docker `build` command
```bash
docker build -t hello-alpine .
```
Once the build is complete, you'll have a new image tagged as `hello-alpine`.

### Step 3. Run the Docker Container
- Run a container based on the `hello-alpine` image using the docker `run` command:
```bash
docker run hello-alpine
```

## Task 1. Customize Your Alpine-based Docker Image

### Step 1: Create the `config.txt` File
- In your `docker-alpine-hello` directory, create a file named `config.txt`
```bash
echo "Welcome to Docker!" > config.txt
```

### Step 2: Modify the `Dockerfile`
- Open your existing `Dockerfile` in the `docker-alpine-hello` directory and modify it to include the installation of curl and to copy the `config.txt` file into the image.
- Update the `Dockerfile` to:
```bash
# Use the official Alpine image from the Docker Hub
FROM alpine:latest

# Install curl
RUN apk add --no-cache curl

# Copy the config.txt file into the container
COPY config.txt /app/config.txt

# Define the command to run when the container starts
CMD ["echo", "Hello, World!"]
```

### Step 3. Build the Extended Docker Image
- Build the Docker image with a new tag
```bash
docker build -t extended-hello-alpine .
```

### Step 4: Test the Docker Container

#### Test the Docker container
Run a container from the newly created image and test the `curl` command:
Example: `docker run extended-hello-alpine curl https://jsonplaceholder.typicode.com/users`

You should see the content of the json placeholder api (users) printed in the terminal, which confirms that curl is installed and working.

#### Confirm the existence and content of the `config.txt` file

```bash
docker run extended-hello-alpine cat /app/config.txt
```

You should see `Welcome to Docker!` printed in the terminal, confirming that the config.txt file is correctly copied into the container.