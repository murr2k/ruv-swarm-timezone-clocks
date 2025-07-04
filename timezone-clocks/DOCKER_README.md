# 🐳 Docker Setup for Timezone Clocks App

This guide explains how to build and run the Timezone Clocks application using Docker.

## 📦 What's Included

- **Dockerfile** - Multi-stage build for Python GUI app
- **docker-compose.yml** - Orchestration for both GUI and web versions
- **.dockerignore** - Optimized build context
- **run-docker.sh** - Automated setup script

## 🚀 Quick Start

### 1. Build the Docker Image
```bash
# Using the script
./run-docker.sh build

# Or manually
docker build -t timezone-clocks .
```

### 2. Run the Application

#### Option A: Web Version (Recommended for WSL/Remote)
```bash
# Using the script
./run-docker.sh web

# Or manually
docker run -d --name timezone-clocks-web -p 8080:8000 timezone-clocks python -m http.server 8000
```
Then open http://localhost:8080 in your browser.

#### Option B: GUI Version (Linux/WSL with X11)
```bash
# Using the script
./run-docker.sh gui

# Or manually (Linux)
docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw timezone-clocks

# Or using docker-compose
docker-compose up timezone-clocks
```

## 🛠️ Manual Docker Commands

### Build Image
```bash
docker build -t timezone-clocks .
```

### Run Web Version
```bash
docker run -d \
  --name timezone-clocks-web \
  -p 8080:8000 \
  timezone-clocks \
  python -m http.server 8000
```

### Run GUI Version (Linux)
```bash
# Allow X11 forwarding
xhost +local:docker

# Run container
docker run -it --rm \
  --name timezone-clocks-gui \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  timezone-clocks
```

### Check Running Containers
```bash
docker ps | grep timezone
```

### Stop and Remove Containers
```bash
docker stop timezone-clocks-web
docker rm timezone-clocks-web
```

## 🔧 Environment-Specific Setup

### WSL (Windows Subsystem for Linux)
1. Install X11 server on Windows (VcXsrv, Xming, or use Windows 11 WSLg)
2. Set DISPLAY environment variable:
   ```bash
   export DISPLAY=:0.0
   ```
3. Use the web version for easier setup:
   ```bash
   ./run-docker.sh web
   ```

### Linux
1. GUI version works out of the box:
   ```bash
   ./run-docker.sh gui
   ```

### macOS
1. Install XQuartz for X11 support
2. Use the web version for simpler setup:
   ```bash
   ./run-docker.sh web
   ```

## 🐳 Docker Compose Usage

### Run GUI Version
```bash
docker-compose up timezone-clocks
```

### Run Web Version
```bash
docker-compose --profile web up timezone-clocks-web
```

## 📊 Container Management

### View Container Status
```bash
./run-docker.sh status
```

### Clean Up All Containers
```bash
./run-docker.sh clean
```

### View Container Logs
```bash
docker logs timezone-clocks-web
```

## 🔍 Troubleshooting

### GUI Not Working
- Ensure X11 server is running
- Check DISPLAY variable: `echo $DISPLAY`
- Try: `xhost +local:docker`
- For WSL, use web version instead

### Container Won't Start
- Check if port 8080 is available: `lsof -i :8080`
- Verify Docker is running: `docker info`
- Check container logs: `docker logs timezone-clocks-web`

### Permission Issues
- Make script executable: `chmod +x run-docker.sh`
- Run with sudo if needed: `sudo ./run-docker.sh`

## 🎯 Use Cases

1. **Development**: Use GUI version for testing
2. **Deployment**: Use web version for servers
3. **CI/CD**: Use headless version for automated testing
4. **Demos**: Use web version for easy sharing

## 📝 Notes

- GUI version requires X11 display server
- Web version serves files on port 8080
- Container includes all Python dependencies
- Image size: ~334MB (optimized with slim base)

## 🔧 Customization

Edit the Dockerfile to:
- Change Python version
- Add additional dependencies
- Modify application settings
- Optimize image size further

## 🚀 Next Steps

1. Set up CI/CD pipeline
2. Add health checks
3. Create Kubernetes manifests
4. Set up monitoring and logging