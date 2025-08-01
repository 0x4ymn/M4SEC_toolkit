# M4SEC Ultimate CTF & Security Toolkit Manager - Installation Guide

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/0x4ymn/M4SEC_toolkit)
[![Build](https://img.shields.io/badge/build-20250801--182338-green.svg)](https://github.com/0x4ymn/M4SEC_toolkit)
[![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://python.org)
[![Team](https://img.shields.io/badge/team-m4sec.team-red.svg)](https://m4sec.team)

## 🚀 Quick Installation

### Automated Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/0x4ymn/M4SEC_toolkit.git
cd M4SEC_toolkit

# Run the installation script
./scripts/install.sh
```

The installation script automatically:
- ✅ Detects externally-managed Python environments
- ✅ Creates virtual environments when needed
- ✅ Installs dependencies in the correct environment
- ✅ Provides clear activation instructions

### Environment Management

M4SEC Toolkit automatically handles different Python environment configurations:

#### For Externally-Managed Environments (Ubuntu 24.04+, Debian 12+)
The installer detects systems with externally-managed Python environments and automatically:
1. Creates a dedicated virtual environment at `~/.m4sec_venv`
2. Installs all dependencies within the virtual environment
3. Provides an activation script for easy use

#### Usage with Virtual Environment
```bash
# Activate M4SEC environment and run toolkit
./scripts/activate_m4sec.sh

# Or manually activate the environment
source ~/.m4sec_venv/bin/activate
python3 src/main.py
```

### Manual Installation

```bash
# For standard environments
pip3 install -r requirements.txt

# For externally-managed environments
python3 -m venv ~/.m4sec_venv
source ~/.m4sec_venv/bin/activate
pip install -r requirements.txt

# Make scripts executable
chmod +x scripts/*.sh

# Test the installation
python3 src/main.py --version
```

## 📋 System Requirements

### Minimum Requirements
- **Operating System**: Linux (Ubuntu 18.04+, Debian 10+, CentOS 7+, Arch Linux)
- **Python**: 3.8 or higher
- **Memory**: 512 MB RAM
- **Storage**: 100 MB for toolkit + space for security tools
- **Terminal**: Any compatible terminal emulator

### Recommended Requirements
- **Operating System**: Ubuntu 20.04+ or Debian 11+
- **Python**: 3.9 or higher
- **Memory**: 2 GB RAM or more
- **Storage**: 10 GB+ for full tool suite
- **Terminal**: gnome-terminal, konsole, or xfce4-terminal

### Supported Platforms
- ✅ **Ubuntu** (18.04, 20.04, 22.04)
- ✅ **Debian** (10, 11, 12)
- ✅ **CentOS** (7, 8)
- ✅ **RHEL** (7, 8, 9)
- ✅ **Fedora** (35+)
- ✅ **Arch Linux**
- ✅ **Kali Linux**
- ✅ **Parrot Security OS**
- ⚠️ **macOS** (limited support)
- ❌ **Windows** (not supported)

## 🔧 Installation Methods

### Method 1: Quick Setup Script

The installation script will:
- Check system compatibility
- Install Python dependencies
- Install common security tools
- Set up directories and permissions
- Test the installation

```bash
./scripts/install.sh
```

### Method 2: Docker Installation (Coming Soon)

```bash
# Pull the M4SEC Toolkit Docker image
docker pull m4sec/toolkit:latest

# Run the toolkit
docker run -it --rm m4sec/toolkit:latest
```

### Method 3: Package Manager Installation (Future)

```bash
# Ubuntu/Debian
sudo apt install m4sec-toolkit

# Fedora
sudo dnf install m4sec-toolkit

# Arch Linux
yay -S m4sec-toolkit
```

## 🔧 Environment Troubleshooting

### Common Environment Issues

#### 1. Externally-Managed Environment Error
```
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
```

**Solution**: Use the automated installer which creates a virtual environment:
```bash
./scripts/install.sh
```

#### 2. Virtual Environment Not Activated
If you see environment warnings when running M4SEC Toolkit:

```bash
# Use the activation script (recommended)
./scripts/activate_m4sec.sh

# Or manually activate
source ~/.m4sec_venv/bin/activate
python3 src/main.py
```

#### 3. Missing python3-venv Package
```
Error: The virtual environment was not created successfully
```

**Solution**: Install virtual environment support:
```bash
# Ubuntu/Debian
sudo apt install python3-venv

# Fedora/CentOS
sudo dnf install python3-venv

# Arch Linux
sudo pacman -S python-virtualenv
```

#### 4. Permission Issues
```bash
# If installation fails due to permissions, ensure you're not running as root
whoami  # Should NOT return 'root'

# If you need to fix ownership
sudo chown -R $USER:$USER ~/.m4sec_venv
```

### Health Check Commands

```bash
# Check environment status
python3 src/main.py --health

# Check if virtual environment is active
echo $VIRTUAL_ENV

# Check Python path
which python3
```

## 📦 Dependency Installation

### Python Dependencies

The toolkit requires these Python packages:

```bash
# Core dependencies
pip3 install colorama psutil rich click

# Optional but recommended
pip3 install tqdm pyyaml requests
```

### Security Tools Installation

#### Ubuntu/Debian Systems

```bash
# Update package lists
sudo apt update

# Essential tools
sudo apt install -y nmap gobuster nikto sqlmap john hashcat

# Binary analysis tools
sudo apt install -y radare2 gdb binutils binwalk exiftool

# Network tools
sudo apt install -y masscan hydra aircrack-ng wireshark netcat socat

# Additional tools
sudo apt install -y steghide foremost theharvester
```

#### Red Hat/CentOS/Fedora Systems

```bash
# Enable EPEL repository (CentOS/RHEL)
sudo yum install -y epel-release

# Essential tools
sudo yum install -y nmap nikto john hashcat

# Or for Fedora
sudo dnf install -y nmap gobuster nikto john hashcat radare2
```

#### Arch Linux

```bash
# Essential tools
sudo pacman -S nmap gobuster nikto sqlmap john hashcat

# AUR tools
yay -S radare2 binwalk exiftool masscan hydra
```

### Manual Tool Installation

Some tools need to be installed manually:

#### Gobuster
```bash
# Go-based installation
go install github.com/OJ/gobuster/v3@latest

# Or download binary
wget https://github.com/OJ/gobuster/releases/download/v3.1.0/gobuster-linux-amd64.tar.gz
```

#### SQLMap
```bash
git clone https://github.com/sqlmapproject/sqlmap.git
cd sqlmap
python3 sqlmap.py --version
```

#### FFuf
```bash
go install github.com/ffuf/ffuf@latest
```

#### RustScan
```bash
cargo install rustscan
```

## 🏗️ Post-Installation Setup

### 1. Environment Configuration

```bash
# Add Go binaries to PATH (if using Go tools)
echo 'export PATH=$PATH:$(go env GOPATH)/bin' >> ~/.bashrc
source ~/.bashrc

# Create output directory
mkdir -p ~/m4sec_output

# Set up wordlists directory
sudo mkdir -p /usr/share/wordlists
```

### 2. Wordlists Setup

```bash
# Download common wordlists
sudo wget -O /usr/share/wordlists/rockyou.txt.gz \
    https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# Install SecLists
git clone https://github.com/danielmiessler/SecLists.git
sudo mv SecLists /usr/share/wordlists/seclists
```

### 3. Terminal Emulator Setup

Install at least one compatible terminal:

```bash
# Ubuntu/Debian
sudo apt install gnome-terminal

# Fedora
sudo dnf install gnome-terminal

# Arch Linux
sudo pacman -S gnome-terminal
```

### 4. Permissions Setup

```bash
# Make scripts executable
chmod +x scripts/*.sh

# Set proper permissions for logs
mkdir -p logs
chmod 755 logs
```

## 🧪 Testing Installation

### Quick Test

```bash
# Test basic functionality
python3 src/main.py --version

# Check system health
python3 src/main.py --health

# List available tools
python3 src/main.py --list-tools
```

### Comprehensive Test

```bash
# Run setup mode
python3 src/main.py --setup

# Test tool detection
python3 src/main.py --health

# Try launching a simple tool
python3 src/main.py --tool nmap
```

## 🔒 Security Considerations

### Running as Non-Root User

⚠️ **IMPORTANT**: Never run M4SEC Toolkit as root!

```bash
# Check current user
whoami

# If you're root, create a regular user
sudo useradd -m -s /bin/bash m4sec
sudo usermod -aG sudo m4sec
su - m4sec
```

### Firewall Configuration

Some tools may require firewall adjustments:

```bash
# Ubuntu/Debian
sudo ufw allow out 53
sudo ufw allow out 80
sudo ufw allow out 443

# CentOS/RHEL
sudo firewall-cmd --permanent --add-service=dns
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

## 🚨 Troubleshooting

### Common Issues

#### 1. Permission Denied Errors
```bash
# Fix script permissions
chmod +x scripts/*.sh
chmod +x src/main.py
```

#### 2. Python Import Errors
```bash
# Reinstall dependencies
pip3 install --force-reinstall -r requirements.txt

# Check Python path
python3 -c "import sys; print(sys.path)"
```

#### 3. Tool Not Found Errors
```bash
# Check tool installation
which nmap gobuster nikto

# Install missing tools
sudo apt install nmap gobuster nikto
```

#### 4. Terminal Launch Failures
```bash
# Check available terminals
python3 src/main.py --health

# Install a terminal emulator
sudo apt install gnome-terminal
```

### Log Files

Check log files for detailed error information:

```bash
# View recent logs
tail -f logs/m4sec_$(date +%Y%m%d).log

# Search for errors
grep -i error logs/*.log
```

### Getting Help

1. **Check the logs**: `logs/m4sec_*.log`
2. **Run health check**: `python3 src/main.py --health`
3. **Check GitHub issues**: [Issues](https://github.com/0x4ymn/M4SEC_toolkit/issues)
4. **Contact team**: admin@m4sec.team

## 🔄 Updating M4SEC Toolkit

### Automatic Update (Future Feature)

```bash
python3 src/main.py --update
```

### Manual Update

```bash
# Backup configuration
cp config/settings.json config/settings.json.bak

# Pull latest changes
git pull origin main

# Reinstall dependencies
pip3 install -r requirements.txt

# Restore configuration
cp config/settings.json.bak config/settings.json
```

## 🗑️ Uninstallation

To completely remove M4SEC Toolkit:

```bash
# Run uninstall script
./scripts/uninstall.sh

# Or manual removal
pip3 uninstall colorama psutil rich click tqdm pyyaml requests
rm -rf logs ~/m4sec_output
```

## 📞 Support & Resources

- **Website**: [m4sec.team](https://m4sec.team)
- **Documentation**: [GitHub Wiki](https://github.com/0x4ymn/M4SEC_toolkit/wiki)
- **Issues**: [GitHub Issues](https://github.com/0x4ymn/M4SEC_toolkit/issues)
- **Email**: admin@m4sec.team
- **Team**: M4SEC Security Team

---

**Build Information**
- Version: 3.0.0
- Build: 20250801-182338
- Author: 0x4ymn
- Team: m4sec.team
- UTC: 2025-08-01 18:23:38