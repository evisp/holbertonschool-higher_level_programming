# Docker Essentials

## 0. Create a Simple Docker Image Locally Based on Alpine

### Step 1: Create the Dockerfile
- Open the Dockerfile in your preferred editor (e.g., VS Code).
- Add the following content to the Dockerfile:
```bash
FROM alpine:latest
CMD ["echo", "Hello, World!"]
```
