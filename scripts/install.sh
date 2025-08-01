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

# Check if Python environment is externally managed
check_externally_managed() {
    local python_version
    python_version=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
    
    # Check for EXTERNALLY-MANAGED file in various locations
    local externally_managed_files=(
        "/usr/lib/python${python_version}/EXTERNALLY-MANAGED"
        "/usr/local/lib/python${python_version}/EXTERNALLY-MANAGED"
        "$(python3 -c 'import sys; print(sys.prefix)')/EXTERNALLY-MANAGED"
    )
    
    for file in "${externally_managed_files[@]}"; do
        if [ -f "$file" ]; then
            return 0  # Externally managed
        fi
    done
    return 1  # Not externally managed
}

# Create and setup virtual environment
setup_virtual_environment() {
    local venv_path="$HOME/.m4sec_venv"
    
    log_info "Setting up Python virtual environment..."
    log_info "Virtual environment path: $venv_path"
    
    # Remove existing venv if it exists and is corrupted
    if [ -d "$venv_path" ] && [ ! -f "$venv_path/bin/activate" ]; then
        log_warning "Removing corrupted virtual environment..."
        rm -rf "$venv_path"
    fi
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "$venv_path" ]; then
        log_info "Creating new virtual environment..."
        if ! python3 -m venv "$venv_path"; then
            log_error "Failed to create virtual environment"
            log_info "Make sure python3-venv is installed:"
            if [ "$PACKAGE_MANAGER" != "unknown" ]; then
                log_info "  $INSTALL_CMD python3-venv"
            fi
            exit 1
        fi
        log_success "Virtual environment created successfully"
    else
        log_success "Virtual environment already exists"
    fi
    
    # Activate virtual environment
    # shellcheck source=/dev/null
    source "$venv_path/bin/activate"
    
    # Upgrade pip in virtual environment
    log_info "Upgrading pip in virtual environment..."
    pip install --upgrade pip
    
    # Set global variables for use in other functions
    VENV_PATH="$venv_path"
    VENV_ACTIVE=1
    
    log_success "Virtual environment is ready and activated"
    echo
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
    
    # Check for externally managed environment
    if check_externally_managed; then
        log_warning "Detected externally-managed Python environment"
        log_info "This system restricts system-wide package installation"
        log_info "Virtual environment will be created automatically"
        EXTERNALLY_MANAGED=1
    else
        log_success "Python environment allows package installation"
        EXTERNALLY_MANAGED=0
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
    
    # Handle externally managed environments
    if [ "$EXTERNALLY_MANAGED" -eq 1 ]; then
        # Check if python3-venv is available
        if [ "$PACKAGE_MANAGER" != "unknown" ]; then
            log_info "Installing python3-venv package for virtual environment support..."
            $INSTALL_CMD python3-venv python3-pip || log_warning "Failed to install python3-venv, continuing..."
        fi
        
        # Setup virtual environment
        setup_virtual_environment
        PIP_CMD="pip"  # Use pip from venv
        INSTALL_FLAGS=""  # No --user flag needed in venv
    else
        # Check if pip is available for system installation
        if ! command -v pip3 >/dev/null 2>&1; then
            log_warning "pip3 not found, attempting to install..."
            if [ "$PACKAGE_MANAGER" != "unknown" ]; then
                $INSTALL_CMD python3-pip
            else
                log_error "Cannot install pip3 automatically"
                exit 1
            fi
        fi
        PIP_CMD="pip3"
        INSTALL_FLAGS="--user"
    fi
    
    # Install requirements
    if [ -f "requirements.txt" ]; then
        log_info "Installing packages from requirements.txt..."
        if $PIP_CMD install $INSTALL_FLAGS -r requirements.txt; then
            log_success "Python dependencies installed successfully"
        else
            log_error "Failed to install Python dependencies"
            if [ "$EXTERNALLY_MANAGED" -eq 0 ]; then
                log_info "Trying with virtual environment as fallback..."
                setup_virtual_environment
                pip install -r requirements.txt
            else
                exit 1
            fi
        fi
    else
        log_warning "requirements.txt not found, installing core dependencies..."
        if $PIP_CMD install $INSTALL_FLAGS colorama psutil rich click tqdm pyyaml requests; then
            log_success "Core Python dependencies installed successfully"
        else
            log_error "Failed to install core Python dependencies"
            if [ "$EXTERNALLY_MANAGED" -eq 0 ]; then
                log_info "Trying with virtual environment as fallback..."
                setup_virtual_environment
                pip install colorama psutil rich click tqdm pyyaml requests
            else
                exit 1
            fi
        fi
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
    
    # Set up Python command based on environment
    if [ "$VENV_ACTIVE" -eq 1 ]; then
        PYTHON_CMD="python3"  # Virtual environment is already activated
    else
        PYTHON_CMD="python3"
    fi
    
    # Test Python imports
    if $PYTHON_CMD -c "
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
        if [ "$VENV_ACTIVE" -eq 1 ]; then
            log_info "Virtual environment may need additional setup"
        fi
        return 1
    fi
    
    # Test basic functionality
    if $PYTHON_CMD src/main.py --version >/dev/null 2>&1; then
        log_success "Basic functionality test passed"
    else
        log_warning "Basic functionality test failed (may be normal during initial setup)"
    fi
    
    echo
}

# Main installation function
main() {
    print_banner
    
    # Initialize global variables
    EXTERNALLY_MANAGED=0
    VENV_ACTIVE=0
    VENV_PATH=""
    
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
    
    # Show environment-specific instructions
    if [ "$VENV_ACTIVE" -eq 1 ]; then
        log_info "🔧 VIRTUAL ENVIRONMENT SETUP:"
        echo -e "${YELLOW}  Virtual environment created at: ${VENV_PATH}${NC}"
        echo
        log_info "To use M4SEC Toolkit, you need to activate the virtual environment:"
        echo -e "${CYAN}  source ${VENV_PATH}/bin/activate${NC}"
        echo
        log_info "Or use the activation script (recommended):"
        echo -e "${CYAN}  ./scripts/activate_m4sec.sh${NC}"
        echo
        log_warning "The virtual environment must be activated before running M4SEC Toolkit!"
        echo
    fi
    
    log_info "To get started:"
    if [ "$VENV_ACTIVE" -eq 1 ]; then
        log_info "  1. Activate environment: source ${VENV_PATH}/bin/activate"
        log_info "  2. Run: python3 src/main.py"
        log_info "  3. Or run: python3 src/main.py --help"
        log_info "  4. For health check: python3 src/main.py --health"
    else
        log_info "  1. Run: python3 src/main.py"
        log_info "  2. Or run: python3 src/main.py --help"
        log_info "  3. For health check: python3 src/main.py --health"
    fi
    echo
    log_info "Visit m4sec.team for more information and updates"
    echo
    
    # Show environment status
    log_info "Environment Summary:"
    if [ "$EXTERNALLY_MANAGED" -eq 1 ]; then
        echo -e "  ${YELLOW}• Externally-managed Python environment detected${NC}"
        echo -e "  ${GREEN}• Virtual environment created and configured${NC}"
    else
        echo -e "  ${GREEN}• Standard Python environment (user packages)${NC}"
    fi
    
    if [ "$VENV_ACTIVE" -eq 1 ]; then
        echo -e "  ${GREEN}• Virtual environment: ${VENV_PATH}${NC}"
    fi
    
    echo
    log_success "Happy hacking! 🔐"
}

# Run main function
main "$@"