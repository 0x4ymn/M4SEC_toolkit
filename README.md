# M4SEC Ultimate CTF & Security Toolkit Manager

<div align="center">

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/0x4ymn/M4SEC_toolkit)
[![Build](https://img.shields.io/badge/build-20250801--182338-green.svg)](https://github.com/0x4ymn/M4SEC_toolkit)
[![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Team](https://img.shields.io/badge/team-m4sec.team-red.svg)](https://m4sec.team)
[![Tools](https://img.shields.io/badge/tools-41-orange.svg)](https://github.com/0x4ymn/M4SEC_toolkit)
[![Categories](https://img.shields.io/badge/categories-12-yellow.svg)](https://github.com/0x4ymn/M4SEC_toolkit)

</div>

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

<div align="center">

**Professional all-in-one security toolkit manager that provides interactive launcher for 41 security tools across 12 specialized categories with terminal integration, guided parameter configuration, and comprehensive health monitoring.**

</div>

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
- **41 security tools** across 12 specialized categories
- **Web Application Testing** (6 tools): gobuster, sqlmap, nikto, ffuf, dirb, whatweb
- **Network Reconnaissance** (5 tools): nmap, masscan, rustscan, enum4linux, dnsrecon  
- **Binary Analysis** (5 tools): radare2, gdb, ghidra, objdump, strings
- **Forensics & Steganography** (5 tools): binwalk, steghide, exiftool, foremost, volatility3
- **Password Cracking** (4 tools): john, hashcat, openssl, hydra
- **And 7 more specialized categories...**

### 🖥️ **Advanced Terminal Integration**
- Launches tools in new terminal windows with professional branding
- Supports multiple terminal emulators (gnome-terminal, konsole, xfce4-terminal, etc.)
- Automatic terminal detection and configuration
- Custom launch scripts with proper command formatting

### ⚙️ **Smart Environment Management**
- Python-based architecture (79.4%) with Shell script integration (20.6%)
- Virtual environment support with automatic detection
- Smart environment management and dependency handling
- Professional configuration management with JSON-based tool definitions

### 🎛️ **Intelligent Configuration**
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
# View installation status of all 41 tools and system compatibility
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

## 📋 System Requirements

### **Minimum Requirements**
- **Operating System**: Linux (Ubuntu 18.04+, Debian 10+, CentOS 7+, Arch Linux)
- **Python Version**: 3.8 or higher
- **Terminal Emulator**: gnome-terminal, konsole, xfce4-terminal, or xterm
- **Memory**: 512MB RAM minimum (1GB+ recommended)
- **Storage**: 100MB for toolkit + space for security tools

### **Recommended Setup**
- **OS**: Ubuntu 20.04+ or Debian 11+
- **Python**: 3.9+ with virtual environment support
- **Terminal**: gnome-terminal or konsole for best experience
- **Memory**: 2GB+ RAM for heavy tools like Ghidra
- **Storage**: 5GB+ for full tool installation

### **Compatible Platforms**
- ✅ **Ubuntu** 18.04, 20.04, 22.04+
- ✅ **Debian** 10, 11, 12
- ✅ **CentOS/RHEL** 7, 8, 9
- ✅ **Arch Linux** (latest)
- ✅ **Kali Linux** (recommended for security testing)
- ⚠️ **macOS** (limited support, manual tool installation required)

## 🔧 Installation

### **Quick Installation (Recommended)**
```bash
git clone https://github.com/0x4ymn/M4SEC_toolkit.git
cd M4SEC_toolkit
./scripts/install.sh
```

### **Manual Installation**
```bash
# Install Python dependencies
pip3 install -r requirements.txt

# Make scripts executable  
chmod +x scripts/*.sh

# Test installation
python3 src/main.py --version
```

## 🛠️ Tool Categories

| Category | Count | Tools | Description |
|----------|-------|--------|-------------|
| **1. Web Application Testing** | 6 | gobuster, sqlmap, nikto, ffuf, dirb, whatweb | Web security assessment tools |
| **2. Network Reconnaissance** | 5 | nmap, masscan, rustscan, enum4linux, dnsrecon | Network discovery and scanning |
| **3. Binary Analysis** | 5 | radare2, gdb, ghidra, objdump, strings | Reverse engineering frameworks |
| **4. Forensics & Steganography** | 5 | binwalk, steghide, exiftool, foremost, volatility3 | Digital forensics tools |
| **5. Cryptography & Passwords** | 4 | john, hashcat, openssl, hydra | Password cracking and crypto |
| **6. Wireless Security** | 2 | aircrack-ng, reaver | WiFi penetration testing |
| **7. Social Engineering & OSINT** | 2 | theharvester, maltego | Information gathering |
| **8. Exploitation** | 2 | metasploit, msfvenom | Penetration testing frameworks |
| **9. Mobile Security** | 2 | apktool, jadx | Mobile application testing |
| **10. Cloud Security** | 2 | awscli, scout | Cloud infrastructure assessment |
| **11. Database Security** | 2 | sqlmap, nosqlimap | Database vulnerability testing |
| **12. Miscellaneous** | 4 | burpsuite, wireshark, netcat, socat | Additional security utilities |

**Total: 41 professional security tools across 12 specialized categories**

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

## 🎨 Screenshots & Interface Demo

### **Main Menu Interface**
```
🔧 SECURITY TOOL CATEGORIES
═══════════════════════════════════════════════════════════════════════════════

  [1] Web Application Testing (6 tools)
      Tools for web application security testing and vulnerability assessment
      ⚠️ (2/6 tools installed) - Install missing: nikto, ffuf, dirb, whatweb

  [2] Network Reconnaissance & Scanning (5 tools)
      Network discovery and reconnaissance tools
      ❌ (0/5 tools installed) - Install missing: nmap, masscan, rustscan

  [3] Binary Analysis & Reverse Engineering (5 tools)
      Reverse engineering and binary analysis frameworks
      ❌ (0/5 tools installed) - Install missing: radare2, gdb, ghidra

  [s] System Status & Health Check
  [h] Help & Documentation  
  [q] Quit M4SEC Toolkit
```

### **Tool Selection Menu**
```
🛠️  TOOLS IN WEB APPLICATION TESTING
═══════════════════════════════════════════════════════════════════════════════

  [1] ✅ gobuster
      Fast directory/file brute-forcer written in Go
      Version: gobuster v3.1.0
      Path: /usr/bin/gobuster
      Status: Ready to launch

  [2] ✅ sqlmap  
      Automatic SQL injection and database takeover tool
      Version: sqlmap/1.6.12#stable
      Status: Ready to launch

  [3] ❌ nikto
      Web server scanner for vulnerabilities and misconfigurations  
      Status: Not installed
      Install: sudo apt install nikto

  [4] ❌ ffuf
      Fast web fuzzer written in Go
      Status: Not installed  
      Install: sudo apt install ffuf

  [b] Back to Categories  [h] Help  [q] Quit
```

### **System Health Dashboard**
```
🔧 M4SEC TOOLKIT HEALTH STATUS
════════════════════════════════════════════════════════════════════════════════

🛠️  TOOLS SUMMARY
────────────────────────
Total Tools:     41
Installed:       5  
Missing:         36
Coverage:        12.2%

📊 CATEGORY BREAKDOWN
────────────────────────
Web Application Testing:     2/6 tools (33.3%)
Network Reconnaissance:      0/5 tools (0.0%)
Binary Analysis:             0/5 tools (0.0%)
Forensics & Steganography:   0/5 tools (0.0%)
Cryptography & Passwords:    1/4 tools (25.0%)
[...additional categories...]

💻 SYSTEM ENVIRONMENT
────────────────────────
Platform:        Linux 5.15.0-Ubuntu 22.04
Python Version:  3.10.6
Python Status:   ✅ Compatible (3.8+ required)
Virtual Env:     ✅ Active (recommended)
User Status:     ✅ Running as regular user (secure)
Terminal Status: ✅ gnome-terminal available

🖥️  TERMINAL SUPPORT
────────────────────────
Available Terminals: 3
Primary:        gnome-terminal (recommended)
Alternatives:   xfce4-terminal, xterm
Status:         ✅ Full terminal integration available
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
Total Tools:     41
Installed:       5  
Missing:         36
Coverage:        12.2%

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
Perfect for Capture The Flag events with comprehensive tool coverage across all 41 tools:
- **Web challenges**: gobuster, sqlmap, nikto, ffuf, dirb, whatweb (6 tools)
- **Network challenges**: nmap, masscan, rustscan, enum4linux, dnsrecon (5 tools)
- **Forensics challenges**: binwalk, steghide, exiftool, foremost, volatility3 (5 tools)
- **Crypto challenges**: john, hashcat, openssl, hydra (4 tools)
- **Binary challenges**: radare2, gdb, ghidra, objdump, strings (5 tools)

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
- **Documentation**: [docs/](docs/) directory

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Acknowledgments

- **Security Community**: For the amazing tools we integrate
- **Contributors**: Everyone who helps improve the project
- **Testers**: Beta testers and bug reporters
- **M4SEC Team**: Core development and maintenance

## 📞 Contact & Links

- **🐙 GitHub**: [0x4ymn/M4SEC_toolkit](https://github.com/0x4ymn/M4SEC_toolkit)
- **👥 Team**: M4SEC Team
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
- **Architecture**: 79.4% Python (3,121 lines) + 20.6% Shell scripts (811 lines)
- **Total Tools**: 41 professional security tools across 12 categories
- **Configuration**: JSON-based with extensible structure
- **UI**: Professional ANSI color terminal interface with ASCII art branding
- **Security**: Built-in safety mechanisms and input validation

---

**⭐ Star this repository if you find it useful!**

**🔐 Happy hacking with M4SEC Toolkit!**
