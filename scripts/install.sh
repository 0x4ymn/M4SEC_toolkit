#!/bin/bash
# M4SEC Ultimate CTF & Security Toolkit Manager
# Installation Script with M4SEC Branding
# 
# Version: 3.0.0
# Build: 20250801-182338
# Author: 0x4ymn
# Team: m4sec.team
# UTC: 2025-08-01 18:23:38

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# M4SEC Banner
print_banner() {
    echo -e "${BLUE}"
    echo "████████████████████████████████████████████████████████████████████████████████"
    echo "█                                                                              █"
    echo "█  ███╗   ███╗██╗  ██╗███████╗███████╗ ██████╗                               █"
    echo "█  ████╗ ████║██║  ██║██╔════╝██╔════╝██╔════╝                               █"
    echo "█  ██╔████╔██║███████║███████╗█████╗  ██║                                     █"
    echo "█  ██║╚██╔╝██║╚════██║╚════██║██╔══╝  ██║                                     █"
    echo "█  ██║ ╚═╝ ██║     ██║███████║███████╗╚██████╗                               █"
    echo "█  ╚═╝     ╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝                               █"
    echo "█                                                                              █"
    echo "█  Ultimate CTF & Security Toolkit Manager - INSTALLER                       █"
    echo "█  Professional All-in-One Launcher & Environment Setup                       █"
    echo "█                                                                              █"
    echo "█  Version: 3.0.0 | Build: 20250801-182338                                   █"
    echo "█  Author: 0x4ymn | Team: m4sec.team                                          █"
    echo "█  UTC: 2025-08-01 18:23:38 | User: $(whoami)                               █"
    echo "█                                                                              █"
    echo "████████████████████████████████████████████████████████████████████████████████"
    echo -e "${NC}"
    echo
}

# Logging functions
log_info() {
    echo -e "${CYAN}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as root
check_root() {
    if [ "$EUID" -eq 0 ]; then
        log_error "This script should not be run as root for security reasons!"
        log_info "Please run as a regular user. Some operations may require sudo."
        echo
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            log_info "Installation cancelled for security."
            exit 1
        fi
    fi
}

# Check system compatibility
check_system() {
    log_info "Checking system compatibility..."
    
    # Check Python version
    if command -v python3 >/dev/null 2>&1; then
        PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
        log_success "Python $PYTHON_VERSION found"
        
        # Check if version is 3.8+
        if python3 -c 'import sys; exit(0 if sys.version_info >= (3, 8) else 1)'; then
            log_success "Python version is compatible (3.8+)"
        else
            log_error "Python 3.8+ is required. Current version: $PYTHON_VERSION"
            exit 1
        fi
    else
        log_error "Python 3 is not installed"
        exit 1
    fi
    
    # Check for package managers
    if command -v apt >/dev/null 2>&1; then
        PACKAGE_MANAGER="apt"
        INSTALL_CMD="sudo apt install -y"
        UPDATE_CMD="sudo apt update"
    elif command -v yum >/dev/null 2>&1; then
        PACKAGE_MANAGER="yum"
        INSTALL_CMD="sudo yum install -y"
        UPDATE_CMD="sudo yum update"
    elif command -v dnf >/dev/null 2>&1; then
        PACKAGE_MANAGER="dnf"
        INSTALL_CMD="sudo dnf install -y"
        UPDATE_CMD="sudo dnf update"
    elif command -v pacman >/dev/null 2>&1; then
        PACKAGE_MANAGER="pacman"
        INSTALL_CMD="sudo pacman -S --noconfirm"
        UPDATE_CMD="sudo pacman -Sy"
    else
        log_warning "No supported package manager found (apt/yum/dnf/pacman)"
        PACKAGE_MANAGER="unknown"
    fi
    
    log_success "System compatibility check completed"
    echo
}

# Install Python dependencies
install_python_deps() {
    log_info "Installing Python dependencies..."
    
    # Check if pip is available
    if ! command -v pip3 >/dev/null 2>&1; then
        log_warning "pip3 not found, attempting to install..."
        if [ "$PACKAGE_MANAGER" != "unknown" ]; then
            $INSTALL_CMD python3-pip
        else
            log_error "Cannot install pip3 automatically"
            exit 1
        fi
    fi
    
    # Install requirements
    if [ -f "requirements.txt" ]; then
        log_info "Installing packages from requirements.txt..."
        pip3 install --user -r requirements.txt
        log_success "Python dependencies installed"
    else
        log_warning "requirements.txt not found, installing core dependencies..."
        pip3 install --user colorama psutil rich click tqdm pyyaml requests
        log_success "Core Python dependencies installed"
    fi
    echo
}

# Install security tools
install_security_tools() {
    log_info "Installing common security tools..."
    echo
    
    if [ "$PACKAGE_MANAGER" = "unknown" ]; then
        log_warning "Cannot install tools automatically. Please install manually:"
        log_info "  • nmap, gobuster, nikto, sqlmap"
        log_info "  • john, hashcat, binwalk, exiftool"
        log_info "  • radare2, gdb, strings, masscan"
        return
    fi
    
    # Update package lists
    log_info "Updating package lists..."
    $UPDATE_CMD
    
    # Common tools available in most repos
    COMMON_TOOLS=(
        "nmap"
        "nikto" 
        "john"
        "hashcat"
        "binwalk"
        "exiftool"
        "radare2"
        "gdb"
        "binutils"  # for strings
        "masscan"
        "hydra"
        "aircrack-ng"
        "wireshark"
        "netcat"
        "socat"
        "python3-scapy"
    )
    
    # Install tools
    for tool in "${COMMON_TOOLS[@]}"; do
        log_info "Installing $tool..."
        if $INSTALL_CMD "$tool" 2>/dev/null; then
            log_success "$tool installed"
        else
            log_warning "Failed to install $tool (may not be available)"
        fi
    done
    
    echo
    log_info "Additional tools to install manually:"
    log_info "  • gobuster: https://github.com/OJ/gobuster"
    log_info "  • sqlmap: https://github.com/sqlmapproject/sqlmap"
    log_info "  • ffuf: go install github.com/ffuf/ffuf@latest"
    log_info "  • rustscan: cargo install rustscan"
    log_info "  • ghidra: https://ghidra-sre.org/"
    echo
}

# Check for terminal emulators
check_terminals() {
    log_info "Checking for terminal emulators..."
    
    TERMINALS=(
        "gnome-terminal"
        "konsole"
        "xfce4-terminal"
        "mate-terminal"
        "terminator"
        "kitty"
        "alacritty"
        "tilix"
        "xterm"
    )
    
    FOUND_TERMINALS=()
    for terminal in "${TERMINALS[@]}"; do
        if command -v "$terminal" >/dev/null 2>&1; then
            FOUND_TERMINALS+=("$terminal")
            log_success "$terminal found"
        fi
    done
    
    if [ ${#FOUND_TERMINALS[@]} -eq 0 ]; then
        log_warning "No terminal emulators found!"
        log_info "Installing xterm as fallback..."
        if [ "$PACKAGE_MANAGER" != "unknown" ]; then
            $INSTALL_CMD xterm
        fi
    else
        log_success "Found ${#FOUND_TERMINALS[@]} terminal emulator(s)"
    fi
    echo
}

# Create directories and setup
setup_directories() {
    log_info "Setting up directories..."
    
    # Create output directory
    OUTPUT_DIR="$HOME/m4sec_output"
    mkdir -p "$OUTPUT_DIR"
    log_success "Created output directory: $OUTPUT_DIR"
    
    # Create logs directory
    mkdir -p logs
    log_success "Created logs directory"
    
    # Make scripts executable
    if [ -d "scripts" ]; then
        chmod +x scripts/*.sh 2>/dev/null || true
        log_success "Made scripts executable"
    fi
    
    echo
}

# Test installation
test_installation() {
    log_info "Testing M4SEC Toolkit installation..."
    
    # Test Python imports
    if python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    from core.config_manager import ConfigManager
    from core.tool_manager import ToolManager
    from ui.colors import ColorFormatter
    print('✓ All modules imported successfully')
except ImportError as e:
    print(f'✗ Import error: {e}')
    sys.exit(1)
" 2>/dev/null; then
        log_success "Python modules test passed"
    else
        log_error "Python modules test failed"
        return 1
    fi
    
    # Test basic functionality
    if python3 src/main.py --version >/dev/null 2>&1; then
        log_success "Basic functionality test passed"
    else
        log_warning "Basic functionality test failed (may be normal)"
    fi
    
    echo
}

# Main installation function
main() {
    print_banner
    
    log_info "Starting M4SEC Toolkit installation..."
    log_info "This will install dependencies and set up the environment"
    echo
    
    # Confirmation
    read -p "Continue with installation? (Y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Nn]$ ]]; then
        log_info "Installation cancelled by user"
        exit 0
    fi
    
    echo "================================="
    echo "  M4SEC TOOLKIT INSTALLATION"
    echo "================================="
    echo
    
    # Run installation steps
    check_root
    check_system
    install_python_deps
    install_security_tools
    check_terminals
    setup_directories
    test_installation
    
    # Final success message
    echo "================================="
    echo "     INSTALLATION COMPLETE"
    echo "================================="
    echo
    log_success "M4SEC Toolkit has been installed successfully!"
    echo
    log_info "To get started:"
    log_info "  1. Run: python3 src/main.py"
    log_info "  2. Or run: python3 src/main.py --help"
    log_info "  3. For health check: python3 src/main.py --health"
    echo
    log_info "Visit m4sec.team for more information and updates"
    echo
    
    # Show quick stats
    log_info "Quick system status:"
    python3 src/main.py --health 2>/dev/null || log_info "Run --health for detailed status"
    
    echo
    log_success "Happy hacking! 🔐"
}

# Run main function
main "$@"