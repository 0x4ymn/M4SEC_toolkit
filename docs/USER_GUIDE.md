# M4SEC Ultimate CTF & Security Toolkit Manager - User Guide

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/0x4ymn/M4SEC_toolkit)
[![Build](https://img.shields.io/badge/build-20250801--182338-green.svg)](https://github.com/0x4ymn/M4SEC_toolkit)

## 🎯 Welcome to M4SEC Toolkit

M4SEC Ultimate CTF & Security Toolkit Manager is your professional all-in-one launcher for security tools. This guide will help you master every feature and get the most out of your security testing workflow.

## 🚀 Getting Started

### First Launch

```bash
# Start the interactive toolkit
python3 src/main.py

# Or see all available options
python3 src/main.py --help
```

### Command Line Interface Options

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

## 🎨 User Interface Guide

### Main Menu Navigation

When you launch M4SEC Toolkit, you'll see the professional main menu:

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

### Menu Controls

- **Numbers (1-12)**: Select tool categories
- **s**: System status and health check
- **h**: Help and documentation
- **q**: Quit the application

### Status Indicators

- ✅ **Tool Installed**: Tool is available and ready to use
- ❌ **Tool Missing**: Tool needs to be installed
- ✓ **Success**: Operation completed successfully
- ! **Warning**: Attention required
- ✗ **Error**: Operation failed
- i **Information**: General information
- ● **Status**: Processing or status update

## 🛠️ Tool Categories Overview

### 1. Web Application Testing
Professional web application security assessment tools:
- **gobuster**: Fast directory/file brute-forcer
- **sqlmap**: Automatic SQL injection testing
- **nikto**: Web server vulnerability scanner
- **ffuf**: Fast web fuzzer written in Go
- **dirb**: Web content scanner
- **whatweb**: Website fingerprinting tool

### 2. Network Reconnaissance & Scanning
Network discovery and reconnaissance utilities:
- **nmap**: Network discovery and security auditing
- **masscan**: High-speed port scanner
- **rustscan**: Modern port scanner in Rust
- **enum4linux**: SMB enumeration tool
- **dnsrecon**: DNS enumeration and reconnaissance

### 3. Binary Analysis & Reverse Engineering
Binary analysis and reverse engineering frameworks:
- **radare2**: Comprehensive reverse engineering framework
- **gdb**: GNU Debugger for program analysis
- **ghidra**: NSA's reverse engineering suite
- **objdump**: Object file disassembler
- **strings**: Extract printable strings from binaries

### 4. Forensics & Steganography
Digital forensics and steganography tools:
- **binwalk**: Firmware analysis and extraction
- **steghide**: Steganography for hiding data
- **exiftool**: Metadata reader and writer
- **foremost**: File carving and recovery
- **volatility3**: Advanced memory forensics

### 5. Cryptography & Password Cracking
Cryptographic analysis and password recovery:
- **john**: John the Ripper password cracker
- **hashcat**: Advanced password recovery
- **openssl**: OpenSSL cryptography toolkit
- **hydra**: Network login cracker

### 6-12. Additional Categories
- **Wireless Security**: WiFi penetration testing
- **Social Engineering & OSINT**: Information gathering
- **Exploitation & Post-Exploitation**: Attack frameworks
- **Mobile Security**: Mobile app testing
- **Cloud Security**: Cloud infrastructure assessment
- **Database Security**: Database vulnerability testing
- **Miscellaneous Security Tools**: Additional utilities

## 🎮 Interactive Workflow

### Step 1: Category Selection

1. Launch M4SEC Toolkit
2. Review available categories and tool counts
3. Select a category by entering its number (1-12)

### Step 2: Tool Selection

1. View tools in the selected category
2. Check installation status (✅/❌)
3. Select a tool by entering its number
4. Review tool information and examples

### Step 3: Parameter Configuration

The toolkit will guide you through configuring tool parameters:

```
🔧 CONFIGURE NMAP
────────────────────────────────────────────────────────────
Configure parameters for the tool. Press Enter for defaults.

Target: Target IP/Network/Host
  Default: None
  * Required
  Enter value: 192.168.1.0/24

Scan Type: Scan type
  Choices: -sS, -sT, -sU, -sA, -sV, -sC
  Default: -sS
  Enter value: -sV

Ports: Port range
  Default: 1-1000
  Enter value: 1-65535

Timing: Timing template
  Choices: -T0, -T1, -T2, -T3, -T4, -T5
  Default: -T4
  Enter value: 

📋 CONFIGURATION SUMMARY
────────────────────────────────────────────────────────────
Target: 192.168.1.0/24
Scan Type: -sV
Ports: 1-65535
Timing: -T4

Launch tool with these parameters? (y/N): y
```

### Step 4: Tool Execution

The tool launches in a new terminal window with:
- Professional M4SEC branding
- Command being executed
- Real-time output
- Completion status

## 🔧 Advanced Configuration

### Custom Configuration File

Create a custom configuration file:

```json
{
  "ui": {
    "use_colors": true,
    "clear_screen": true
  },
  "terminal": {
    "preferred_terminal": "gnome-terminal",
    "keep_open": true
  },
  "paths": {
    "wordlists_dir": "/usr/share/wordlists",
    "output_dir": "~/custom_output"
  }
}
```

Use it with:
```bash
python3 src/main.py --config custom_config.json
```

### Environment Variables

Set environment variables for custom behavior:

```bash
# Disable colors
export NO_COLOR=1

# Force colors
export FORCE_COLOR=1

# Custom wordlists directory
export M4SEC_WORDLISTS="/path/to/wordlists"
```

## 🎯 Practical Examples

### Example 1: Web Application Testing

1. **Select Category 1**: Web Application Testing
2. **Choose gobuster**: Directory brute-forcing
3. **Configure parameters**:
   - Target: `http://testphp.vulnweb.com`
   - Wordlist: `/usr/share/wordlists/dirb/common.txt`
   - Extensions: `php,html,txt`
   - Threads: `20`
4. **Launch**: Tool opens in new terminal

### Example 2: Network Reconnaissance

1. **Select Category 2**: Network Reconnaissance & Scanning
2. **Choose nmap**: Network scanning
3. **Configure parameters**:
   - Target: `192.168.1.0/24`
   - Scan type: `-sV` (version detection)
   - Ports: `1-1000`
   - Timing: `-T4`
4. **Launch**: Comprehensive network scan

### Example 3: Password Cracking

1. **Select Category 5**: Cryptography & Password Cracking
2. **Choose hashcat**: Advanced password recovery
3. **Configure parameters**:
   - Attack mode: `0` (dictionary)
   - Hash type: `1000` (NTLM)
   - Hash file: `ntlm_hashes.txt`
   - Wordlist: `/usr/share/wordlists/rockyou.txt`
4. **Launch**: Hash cracking session

## 🔍 System Health Monitoring

Use the health check feature to monitor your security toolkit:

```bash
python3 src/main.py --health
```

The health check provides:
- **Tool Status**: Installation status of all 50+ tools
- **System Information**: Platform, Python version, user status
- **Terminal Support**: Available terminal emulators
- **Missing Tools**: List of tools that need installation
- **Coverage Percentage**: Overall toolkit completeness

## 📊 Tool Management

### Installing Missing Tools

When tools are missing (❌), the toolkit provides installation commands:

```bash
# Example installation commands shown by toolkit
sudo apt install nmap          # For nmap
go install github.com/OJ/gobuster/v3@latest  # For gobuster
pip3 install volatility3       # For volatility3
```

### Refreshing Tool Status

- Press `r` in category menus to refresh tool detection
- The toolkit caches tool status for performance
- Changes in tool installation are detected automatically

## 🎨 Customization Options

### Terminal Preferences

The toolkit supports multiple terminal emulators:
- **gnome-terminal** (recommended)
- **konsole** (KDE)
- **xfce4-terminal** (XFCE)
- **mate-terminal** (MATE)
- **terminator**
- **kitty**
- **alacritty**
- **tilix**
- **xterm** (fallback)

### Color Themes

Colors can be customized in the configuration:
- **Headers**: Bold Blue
- **Success**: Green with ✓
- **Warnings**: Yellow with !
- **Errors**: Red with ✗
- **Info**: Cyan with i
- **Status**: Blue with ●

### Output Directory

Customize where tool outputs are saved:

```json
{
  "paths": {
    "output_dir": "~/custom_security_output"
  }
}
```

## 🔐 Security Best Practices

### User Security

1. **Never run as root**: The toolkit prevents root execution for security
2. **Use dedicated user**: Consider a separate user for security testing
3. **Isolate environment**: Use VMs or containers for testing
4. **Regular updates**: Keep tools and toolkit updated

### Network Security

1. **Use VPN**: Route traffic through VPN when appropriate
2. **Isolated networks**: Test on isolated or lab networks
3. **Permission first**: Always get explicit permission before testing
4. **Document everything**: Keep detailed logs of activities

### Legal Considerations

⚠️ **IMPORTANT**: Only use M4SEC Toolkit on systems you own or have explicit permission to test. Unauthorized security testing is illegal and unethical.

## 🚨 Troubleshooting

### Common Issues and Solutions

#### Tool Launch Failures
```bash
# Check terminal availability
python3 src/main.py --health

# Install a supported terminal
sudo apt install gnome-terminal
```

#### Permission Errors
```bash
# Fix script permissions
chmod +x scripts/*.sh
chmod +x src/main.py

# Check file ownership
ls -la src/main.py
```

#### Import Errors
```bash
# Reinstall dependencies
pip3 install --force-reinstall -r requirements.txt

# Check Python path
python3 -c "import sys; print(sys.path)"
```

#### Configuration Issues
```bash
# Reset to defaults
rm config/settings.json
python3 src/main.py  # Will recreate defaults
```

### Log Analysis

Check logs for detailed error information:

```bash
# View today's log
tail -f logs/m4sec_$(date +%Y%m%d).log

# Search for specific errors
grep -i "error\|exception" logs/*.log

# View tool launch history
grep "Launching" logs/*.log
```

## 📞 Getting Help

### Built-in Help

- Press `h` in the main menu for interactive help
- Use `--help` flag for command-line help
- Check tool examples in category menus

### External Resources

- **Documentation**: Complete guides at [GitHub Wiki](https://github.com/0x4ymn/M4SEC_toolkit/wiki)
- **Video Tutorials**: Coming soon on [YouTube](https://youtube.com/@m4sec)
- **Community**: Join discussions on [Discord](https://discord.gg/m4sec)
- **Issues**: Report bugs on [GitHub Issues](https://github.com/0x4ymn/M4SEC_toolkit/issues)

### Professional Support

For professional support and training:
- **Email**: admin@m4sec.team
- **Website**: [m4sec.team](https://m4sec.team)
- **Consulting**: Available for enterprise deployments

## 🎓 Learning Resources

### Recommended Learning Path

1. **Start with basics**: Web application testing (Category 1)
2. **Network fundamentals**: Network reconnaissance (Category 2)
3. **Defensive analysis**: Binary analysis and forensics (Categories 3-4)
4. **Advanced topics**: Cryptography and exploitation (Categories 5+)

### CTF Practice

M4SEC Toolkit is perfect for CTF competitions:
- **Web challenges**: Use gobuster, sqlmap, nikto
- **Network challenges**: Use nmap, masscan, enum4linux
- **Forensics challenges**: Use binwalk, exiftool, volatility3
- **Crypto challenges**: Use john, hashcat, openssl

### Certification Preparation

The toolkit supports preparation for:
- **OSCP**: Offensive Security Certified Professional
- **CEH**: Certified Ethical Hacker
- **GCPEN**: GIAC Penetration Tester
- **PNPT**: Practical Network Penetration Tester

---

**Thank You for Using M4SEC Toolkit!**

*Version: 3.0.0 | Build: 20250801-182338 | Author: 0x4ymn | Team: m4sec.team*

Happy hacking! 🔐