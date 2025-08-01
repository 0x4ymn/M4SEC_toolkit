# M4SEC Ultimate CTF & Security Toolkit Manager

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/0x4ymn/M4SEC_toolkit)
[![Build](https://img.shields.io/badge/build-20250801--182338-green.svg)](https://github.com/0x4ymn/M4SEC_toolkit)
[![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Team](https://img.shields.io/badge/team-m4sec.team-red.svg)](https://m4sec.team)

```
████████████████████████████████████████████████████████████████████████████████
█                                                                              █
█  ███╗   ███╗██╗  ██╗███████╗███████╗ ██████╗                               █
█  ████╗ ████║██║  ██║██╔════╝██╔════╝██╔════╝                               █
█  ██╔████╔██║███████║███████╗█████╗  ██║                                     █
█  ██║╚██╔╝██║╚════██║╚════██║██╔══╝  ██║                                     █
█  ██║ ╚═╝ ██║     ██║███████║███████╗╚██████╗                               █
█  ╚═╝     ╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝                               █
█                                                                              █
█  Ultimate CTF & Security Toolkit Manager                                    █
█  Professional All-in-One Launcher & Environment Setup                       █
█                                                                              █
█  Version: 3.0.0 | Build: 20250801-182338                                   █
█  Author: 0x4ymn | Team: m4sec.team                                          █
█  UTC: 2025-08-01 18:23:38 | User: 0x4ymn                                   █
█                                                                              █
████████████████████████████████████████████████████████████████████████████████
```

**Professional all-in-one security toolkit manager that provides interactive launcher for 50+ security tools across 12 categories with terminal integration, guided parameter configuration, and comprehensive health monitoring.**

## 🚀 Quick Start

```bash
# Clone and install
git clone https://github.com/0x4ymn/M4SEC_toolkit.git
cd M4SEC_toolkit
./scripts/install.sh

# Launch interactive mode
python3 src/main.py

# Or run system health check
python3 src/main.py --health
```

## ✨ Key Features

### 🎯 **Professional Interface**
- Interactive menu system with 12 security categories
- Professional ASCII art branding with M4SEC theme
- Color-coded status indicators and progress bars
- Clean, intuitive navigation with help system

### 🛠️ **Comprehensive Tool Coverage**
- **50+ security tools** across 12 specialized categories
- **Web Application Testing**: gobuster, sqlmap, nikto, ffuf
- **Network Reconnaissance**: nmap, masscan, rustscan, enum4linux  
- **Binary Analysis**: radare2, gdb, ghidra, strings
- **Forensics & Steganography**: binwalk, steghide, exiftool, volatility3
- **Password Cracking**: john, hashcat, hydra
- **And much more...**

### 🖥️ **Advanced Terminal Integration**
- Launches tools in new terminal windows with professional branding
- Supports multiple terminal emulators (gnome-terminal, konsole, xfce4-terminal, etc.)
- Automatic terminal detection and configuration
- Custom launch scripts with proper command formatting

### ⚙️ **Intelligent Configuration**
- Interactive parameter configuration with validation
- Smart defaults and example commands
- JSON-based tool definitions for easy extensibility  
- User preferences and custom settings support

### 📊 **Health Monitoring**
- Real-time tool installation status tracking
- System compatibility checks and recommendations
- Missing tool detection with installation suggestions
- Comprehensive health reports and statistics

## 🎮 Usage Examples

### Interactive Mode
```bash
python3 src/main.py
# Navigate through categories → Select tools → Configure parameters → Launch
```

### Direct Tool Launch
```bash
python3 src/main.py --tool nmap
# Configure nmap parameters interactively and launch in new terminal
```

### System Health Check
```bash
python3 src/main.py --health
# View installation status of all 50+ tools and system compatibility
```

### List All Tools
```bash
python3 src/main.py --list-tools
# Display all available tools organized by category with status
```

## 📁 Project Structure

```
M4SEC_toolkit/
├── src/                    # 🐍 Core Python application
│   ├── core/              # Core functionality modules
│   │   ├── config_manager.py     # JSON configuration management
│   │   ├── tool_manager.py       # Tool detection & verification
│   │   ├── terminal_launcher.py  # Terminal integration system
│   │   └── utils.py              # Utilities, logging, system checks
│   ├── ui/                # User interface components  
│   │   ├── colors.py             # ANSI color formatting
│   │   ├── banner.py             # ASCII art and branding
│   │   └── menu.py               # Interactive menu system
│   └── main.py            # 🚀 Main entry point
├── config/                # ⚙️ Configuration files
│   ├── tools.json         # Tool definitions (50+ tools)
│   └── settings.json      # Application preferences  
├── scripts/               # 📜 Installation & setup scripts
│   ├── install.sh         # Automated installation
│   └── uninstall.sh       # Clean removal
├── docs/                  # 📚 Comprehensive documentation
│   ├── INSTALLATION.md    # Detailed installation guide
│   ├── USER_GUIDE.md      # Complete user manual
│   └── CONTRIBUTING.md    # Contribution guidelines
└── requirements.txt       # Python dependencies
```

## 🔧 Installation

### Prerequisites
- **Linux OS** (Ubuntu 18.04+, Debian 10+, CentOS 7+, Arch Linux)
- **Python 3.8+** 
- **Terminal emulator** (gnome-terminal, konsole, xfce4-terminal, xterm)

### Automatic Installation
```bash
git clone https://github.com/0x4ymn/M4SEC_toolkit.git
cd M4SEC_toolkit
./scripts/install.sh
```

### Manual Installation
```bash
# Install Python dependencies
pip3 install -r requirements.txt

# Make scripts executable  
chmod +x scripts/*.sh

# Test installation
python3 src/main.py --version
```

## 🛠️ Tool Categories

| Category | Tools | Description |
|----------|--------|-------------|
| **1. Web Application Testing** | gobuster, sqlmap, nikto, ffuf, dirb, whatweb | Web security assessment tools |
| **2. Network Reconnaissance** | nmap, masscan, rustscan, enum4linux, dnsrecon | Network discovery and scanning |
| **3. Binary Analysis** | radare2, gdb, ghidra, objdump, strings | Reverse engineering frameworks |
| **4. Forensics & Steganography** | binwalk, steghide, exiftool, foremost, volatility3 | Digital forensics tools |
| **5. Cryptography & Passwords** | john, hashcat, openssl, hydra | Password cracking and crypto |
| **6. Wireless Security** | aircrack-ng, reaver | WiFi penetration testing |
| **7. Social Engineering & OSINT** | theharvester, maltego | Information gathering |
| **8. Exploitation** | metasploit, msfvenom | Penetration testing frameworks |
| **9. Mobile Security** | apktool, jadx | Mobile application testing |
| **10. Cloud Security** | awscli, scout | Cloud infrastructure assessment |
| **11. Database Security** | sqlmap, nosqlimap | Database vulnerability testing |
| **12. Miscellaneous** | burpsuite, wireshark, netcat, socat | Additional security utilities |

## 💻 Command Line Interface

```bash
# Interactive mode (default)
python3 src/main.py

# System setup and tool installation guide  
python3 src/main.py --setup

# System health check and tool status
python3 src/main.py --health

# Launch specific tool directly
python3 src/main.py --tool nmap

# List all available tools by category
python3 src/main.py --list-tools

# Show version information
python3 src/main.py --version

# Use custom configuration file
python3 src/main.py --config /path/to/config.json
```

## 🎨 Screenshots & UI

### Main Menu
```
🔧 SECURITY TOOL CATEGORIES
═══════════════════════════════════════════════════════════════════════════════

  [1] Web Application Testing
      Tools for web application security testing and vulnerability assessment
      ✅ (4/6 tools installed)

  [2] Network Reconnaissance & Scanning  
      Network discovery and reconnaissance tools
      ⚠️ (3/5 tools installed)

  [s] System Status & Health Check
  [h] Help & Documentation  
  [q] Quit M4SEC Toolkit
```

### Tool Selection
```
🛠️  TOOLS IN WEB APPLICATION TESTING
═══════════════════════════════════════════════════════════════════════════════

  [1] ✅ gobuster
      Fast directory/file brute-forcer written in Go
      Version: gobuster v3.1.0
      Path: /usr/bin/gobuster

  [2] ✅ sqlmap  
      Automatic SQL injection and database takeover tool
      Version: sqlmap/1.6.12#stable

  [3] ❌ nikto
      Web server scanner for vulnerabilities and misconfigurations  
      Install: sudo apt install nikto
```

## 🔒 Security Features

### Security-First Design
- **Never runs as root**: Built-in root detection and prevention
- **Input validation**: Comprehensive sanitization of user inputs
- **Command injection protection**: Safe parameter passing to tools
- **Secure temporary files**: Proper cleanup of temporary scripts

### Professional Security Practices
- **Logging system**: Comprehensive audit trail of all activities
- **Error handling**: Graceful failure handling with detailed logging
- **Permission checks**: Validates file and directory permissions
- **Safe execution**: Sandboxed tool execution in separate processes

## 📊 System Health Monitoring

The health monitoring system provides:

```bash
🛠️  TOOLS SUMMARY
────────────────────────
Total Tools:     50
Installed:       42  
Missing:         8
Coverage:        84.0%

💻 SYSTEM INFORMATION  
────────────────────────
Platform:        Linux-5.4.0-Ubuntu
Python Version:  3.9.2
Python Status:   ✅ Compatible
User Status:     ✅ Running as regular user

🖥️  TERMINAL SUPPORT
────────────────────────
Available:       3
Status:          ✅ Terminal support available
  • gnome-terminal
  • xfce4-terminal  
  • xterm
```

## 🎯 Use Cases

### CTF Competitions
Perfect for Capture The Flag events with comprehensive tool coverage:
- **Web challenges**: gobuster, sqlmap, nikto, ffuf
- **Network challenges**: nmap, masscan, enum4linux  
- **Forensics challenges**: binwalk, exiftool, volatility3
- **Crypto challenges**: john, hashcat, openssl

### Penetration Testing
Professional penetration testing workflow:
- **Reconnaissance**: nmap, gobuster, enum4linux, theharvester
- **Vulnerability Assessment**: nikto, sqlmap, masscan
- **Exploitation**: metasploit, msfvenom, hydra
- **Post-Exploitation**: volatility3, binwalk, exiftool

### Security Education
Learning and training platform:
- **Guided parameter configuration** with examples
- **Professional UI** for better learning experience  
- **Comprehensive tool coverage** across security domains
- **Health monitoring** to track learning progress

### Red Team Operations
Advanced red team toolkit:
- **OSINT gathering**: theharvester, maltego
- **Network reconnaissance**: nmap, masscan, rustscan
- **Web application testing**: burpsuite integration
- **Social engineering**: Comprehensive OSINT tools

## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](docs/CONTRIBUTING.md) for details.

### Ways to Contribute
- 🐛 Report bugs and issues
- 💡 Suggest new features or tools
- 📝 Improve documentation
- 🔧 Submit code improvements
- 🧪 Test on different platforms

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/M4SEC_toolkit.git

# Install development dependencies
pip3 install -r requirements.txt
pip3 install pytest black flake8 mypy

# Create feature branch
git checkout -b feature/your-feature-name
```

## 📚 Documentation

- **[Installation Guide](docs/INSTALLATION.md)**: Comprehensive setup instructions
- **[User Guide](docs/USER_GUIDE.md)**: Complete usage manual with examples  
- **[Contributing Guide](docs/CONTRIBUTING.md)**: Development and contribution guidelines
- **[GitHub Wiki](https://github.com/0x4ymn/M4SEC_toolkit/wiki)**: Additional resources

## 🐛 Issues & Support

- **Bug Reports**: [GitHub Issues](https://github.com/0x4ymn/M4SEC_toolkit/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/0x4ymn/M4SEC_toolkit/discussions)
- **Email Support**: admin@m4sec.team
- **Documentation**: [docs/](docs/) directory

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Acknowledgments

- **Security Community**: For the amazing tools we integrate
- **Contributors**: Everyone who helps improve the project
- **Testers**: Beta testers and bug reporters
- **M4SEC Team**: Core development and maintenance

## 📞 Contact & Links

- **🌐 Website**: [m4sec.team](https://m4sec.team)
- **📧 Email**: admin@m4sec.team  
- **🐙 GitHub**: [0x4ymn/M4SEC_toolkit](https://github.com/0x4ymn/M4SEC_toolkit)
- **👥 Team**: M4SEC Security Team
- **📅 Build**: 20250801-182338

---

## 🎯 Project Metadata

**Current Build Information:**
- **Version**: 3.0.0
- **Build**: 20250801-182338  
- **Author**: 0x4ymn
- **Team**: m4sec.team
- **UTC**: 2025-08-01 18:23:38
- **User**: 0x4ymn

**Technical Specifications:**
- **Python**: 3.8+ compatibility
- **Architecture**: Modular design with separation of concerns
- **Configuration**: JSON-based with extensible structure
- **UI**: Professional ANSI color terminal interface
- **Security**: Built-in safety mechanisms and input validation

---

**⭐ Star this repository if you find it useful!**

**🔐 Happy hacking with M4SEC Toolkit!**
