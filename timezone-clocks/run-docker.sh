#!/bin/bash

# Docker Run Script for Timezone Clocks App
# Supports multiple environments: Linux, WSL, macOS

echo "🐳 Docker Container Setup for Timezone Clocks App"
echo "=================================================="

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker first."
    exit 1
fi

# Function to run GUI version (Linux/WSL with X11)
run_gui() {
    echo "🖥️  Running GUI version with X11 forwarding..."
    
    # Check if running on WSL
    if grep -q microsoft /proc/version; then
        echo "🔧 WSL detected - Make sure you have X11 server running on Windows"
        echo "   (e.g., VcXsrv, Xming, or Windows 11 WSLg)"
        export DISPLAY=:0.0
    fi
    
    # Allow X11 forwarding
    xhost +local:docker > /dev/null 2>&1 || echo "⚠️  xhost not available, GUI may not work"
    
    docker run -it --rm \
        --name timezone-clocks-gui \
        -e DISPLAY=$DISPLAY \
        -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
        timezone-clocks
}

# Function to run web version (headless)
run_web() {
    echo "🌐 Running web version (headless)..."
    
    # Stop existing container if running
    docker stop timezone-clocks-web > /dev/null 2>&1
    docker rm timezone-clocks-web > /dev/null 2>&1
    
    # Run web server
    docker run -d \
        --name timezone-clocks-web \
        -p 8080:8000 \
        timezone-clocks \
        python -m http.server 8000
    
    echo "✅ Container started successfully!"
    echo "🔗 Access the files at: http://localhost:8080"
    echo "📋 To stop: docker stop timezone-clocks-web"
}

# Function to build image
build_image() {
    echo "🔨 Building Docker image..."
    docker build -t timezone-clocks .
    echo "✅ Image built successfully!"
}

# Function to show container status
show_status() {
    echo "📊 Container Status:"
    docker ps -a | grep timezone || echo "No timezone containers found"
}

# Function to clean up
cleanup() {
    echo "🧹 Cleaning up containers..."
    docker stop timezone-clocks-web timezone-clocks-gui > /dev/null 2>&1
    docker rm timezone-clocks-web timezone-clocks-gui > /dev/null 2>&1
    echo "✅ Cleanup completed!"
}

# Main menu
case "$1" in
    gui|GUI)
        run_gui
        ;;
    web|WEB)
        run_web
        ;;
    build|BUILD)
        build_image
        ;;
    status|STATUS)
        show_status
        ;;
    clean|CLEAN)
        cleanup
        ;;
    *)
        echo "Usage: $0 {gui|web|build|status|clean}"
        echo ""
        echo "Commands:"
        echo "  gui    - Run GUI version (requires X11)"
        echo "  web    - Run web version (headless, port 8080)"
        echo "  build  - Build Docker image"
        echo "  status - Show container status"
        echo "  clean  - Stop and remove containers"
        echo ""
        echo "Examples:"
        echo "  $0 build    # Build the image first"
        echo "  $0 gui      # Run with GUI (Linux/WSL)"
        echo "  $0 web      # Run web version (any platform)"
        exit 1
        ;;
esac