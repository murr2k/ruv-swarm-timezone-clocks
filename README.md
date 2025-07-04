# 🕐 Timezone Clocks with ruv-swarm Integration

> **Docker-enabled 24-timezone analog clock application with ruv-swarm MCP integration for enhanced coordination, parallel execution, and neural pattern learning.**

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Docker](https://img.shields.io/badge/docker-ready-blue.svg)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20windows%20%7C%20macos-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🌟 Features

### 🕐 Timezone Clock Application
- **24 Analog Clocks** displaying major timezones worldwide
- **Real-time Updates** with beautiful analog clock faces
- **GUI & Web Deployment** options (Tkinter + HTTP server)
- **Cross-platform** support (Windows, Linux, macOS)
- **Docker containerized** for easy deployment

### 🧠 ruv-swarm MCP Integration
- **Enhanced Coordination** with Claude Code
- **Neural Pattern Learning** for improved development workflows
- **Parallel Execution** capabilities (2.8-4.4x speed improvement)
- **Cross-session Memory** persistence
- **Auto-optimization** and intelligent caching

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/murr2k/ruv-swarm-timezone-clocks.git
cd ruv-swarm-timezone-clocks

# Run web version (works everywhere)
cd timezone-clocks
./run-docker.sh web
# Open http://localhost:8080

# Or run GUI version (Linux/WSL with X11)
./run-docker.sh gui
```

### Option 2: Local Python
```bash
# Install dependencies
cd timezone-clocks
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 3: Claude Code + ruv-swarm
```bash
# Add ruv-swarm MCP integration to Claude Code
claude mcp add ruv-swarm npx ruv-swarm mcp start

# Use enhanced coordination in Claude Code
# (See CLAUDE.md for full integration guide)
```

## 📸 Screenshots

### 24-Timezone Analog Clocks
```
┌─────────────────────────────────────────────────────────────────┐
│  🕐 Honolulu    🕑 Los Angeles  🕒 New York     🕓 London      │
│  🕔 Paris       🕕 Cairo        🕖 Moscow       🕗 Dubai       │
│  🕘 Bangkok     🕙 Shanghai     🕚 Tokyo        🕛 Sydney      │
│                    ... and 12 more timezones                   │
└─────────────────────────────────────────────────────────────────┘
```

### Docker Deployment Options
- **GUI Mode**: Full Tkinter interface with X11 forwarding
- **Web Mode**: HTTP server serving the application files
- **Headless**: Background processing for automation

## 🛠️ Project Structure

```
ruv-swarm-timezone-clocks/
├── 🕐 timezone-clocks/           # Main Application
│   ├── 🐳 Dockerfile            # Container configuration
│   ├── 🐳 docker-compose.yml    # Multi-service orchestration
│   ├── 🚀 run-docker.sh         # Automated deployment script
│   ├── 📱 main.py               # GUI application entry point
│   ├── ⚙️ analog_clock.py       # Clock widget implementation
│   ├── 📋 requirements.txt      # Python dependencies
│   └── 📚 DOCKER_README.md      # Docker-specific documentation
├── 🧠 .claude/                  # Claude Code Integration
│   ├── ⚙️ settings.json         # MCP configuration
│   └── 📁 commands/             # ruv-swarm command documentation
├── 🔧 ruv-swarm*               # Swarm coordination executables
├── 📋 CLAUDE.md                # Full integration instructions
└── 📚 GITHUB_SETUP.md          # Repository setup guide
```

## 🐳 Docker Deployment

### Build and Run
```bash
# Build the image
docker build -t timezone-clocks ./timezone-clocks

# Run web version (recommended)
docker run -d -p 8080:8000 --name timezone-clocks-web \
  timezone-clocks python -m http.server 8000

# Run GUI version (Linux/WSL)
docker run -it --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  timezone-clocks
```

### Docker Compose
```bash
# Web version
docker-compose --profile web up

# GUI version  
docker-compose up timezone-clocks
```

## 🧠 ruv-swarm Integration

This project showcases advanced Claude Code coordination through ruv-swarm MCP tools:

### Key Benefits
- **84.8% SWE-Bench solve rate** improvement
- **32.3% token reduction** through efficient coordination
- **2.8-4.4x speed improvement** via parallel execution
- **27+ neural models** for diverse cognitive approaches

### MCP Tools Available
- `mcp__ruv-swarm__swarm_init` - Initialize coordination topology
- `mcp__ruv-swarm__agent_spawn` - Create specialized cognitive patterns
- `mcp__ruv-swarm__task_orchestrate` - Coordinate complex workflows
- `mcp__ruv-swarm__memory_usage` - Persistent cross-session memory
- `mcp__ruv-swarm__neural_*` - Neural pattern learning tools

### Setup with Claude Code
```bash
# Add MCP server
claude mcp add ruv-swarm npx ruv-swarm mcp start

# Verify integration
claude mcp list
```

## 🌍 Supported Timezones

The application displays 24 major timezones covering all UTC offsets:

| Region | Timezone | UTC Offset |
|--------|----------|------------|
| 🌺 Pacific | Honolulu, Midway | UTC-11, UTC-10 |
| 🇺🇸 Americas | Alaska, Pacific, Mountain, Central, Eastern | UTC-9 to UTC-5 |
| 🌎 South America | Caracas, Buenos Aires, São Paulo | UTC-4, UTC-3 |
| 🌊 Atlantic | South Georgia, Azores | UTC-2, UTC-1 |
| 🇪🇺 Europe | London, Paris, Moscow | UTC+0 to UTC+3 |
| 🕌 Middle East/Asia | Dubai, Karachi, Bangkok | UTC+4 to UTC+7 |
| 🏯 East Asia | Shanghai, Tokyo, Sydney | UTC+8 to UTC+10 |
| 🇦🇺 Oceania | Auckland, Noumea | UTC+11, UTC+12 |

## ⚡ Performance Features

### Automated Optimizations
- **Smart Agent Spawning** - Zero manual agent management
- **Automatic Topology Selection** - Optimal swarm structure per task
- **Self-Healing Workflows** - Automatic error recovery
- **Intelligent Caching** - Reduced redundant operations

### Neural Learning
- **Pattern Recognition** - Learn from successful operations
- **Cross-Session Memory** - Persistent learning and context
- **Bottleneck Analysis** - Real-time performance optimization
- **Token Efficiency** - Minimize API usage through coordination

## 🔧 Development

### Local Development
```bash
# Clone and setup
git clone https://github.com/murr2k/ruv-swarm-timezone-clocks.git
cd ruv-swarm-timezone-clocks

# Install Python dependencies
cd timezone-clocks
pip install -r requirements.txt

# Run locally
python main.py
```

### Docker Development
```bash
# Build development image
docker build -t timezone-clocks-dev ./timezone-clocks

# Run with volume mounting for live changes
docker run -it --rm \
  -v $(pwd)/timezone-clocks:/app \
  -p 8080:8000 \
  timezone-clocks-dev
```

## 📚 Documentation

- **[Docker Setup Guide](timezone-clocks/DOCKER_README.md)** - Complete Docker deployment instructions
- **[Claude Code Integration](CLAUDE.md)** - Full ruv-swarm MCP setup and usage
- **[GitHub Setup](GITHUB_SETUP.md)** - Repository creation and deployment guide
- **[Application Guide](timezone-clocks/README.md)** - Timezone clock app documentation

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** changes: `git commit -m 'Add amazing feature'`
4. **Push** to branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Development with ruv-swarm
This project is designed to showcase ruv-swarm capabilities. When contributing:
- Use the MCP tools for coordination
- Follow the parallel execution patterns
- Leverage neural learning for code improvements
- Maintain cross-session memory for context

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[ruv-swarm](https://github.com/ruvnet/ruv-FANN/tree/main/ruv-swarm)** - Enhanced coordination framework
- **[Claude Code](https://claude.ai/code)** - AI-powered development environment
- **[pytz](https://pypi.org/project/pytz/)** - Timezone handling library
- **Docker Community** - Containerization platform

## 🔗 Links

- **Repository**: https://github.com/murr2k/ruv-swarm-timezone-clocks
- **ruv-swarm Documentation**: https://github.com/ruvnet/ruv-FANN/tree/main/ruv-swarm
- **Claude Code**: https://docs.anthropic.com/en/docs/claude-code
- **Docker Hub**: (Coming soon)

---

**Built with ❤️ using Claude Code and ruv-swarm coordination**

*Showcasing the future of AI-enhanced development workflows*