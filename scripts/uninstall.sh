#!/bin/bash
# M4SEC Ultimate CTF & Security Toolkit Manager
# Clean Uninstallation Script
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

# Print uninstall banner
print_banner() {
    echo -e "${RED}"
    echo "╔══════════════════════════════════════════════════════════════════════════════════╗"
    echo "║                                                                                  ║"
    echo "║  M4SEC Ultimate CTF & Security Toolkit Manager - UNINSTALLER                   ║"
    echo "║                                                                                  ║"
    echo "║  This will remove M4SEC Toolkit and its associated files                       ║"
    echo "║  Security tools installed separately will NOT be removed                       ║"
    echo "║                                                                                  ║"
    echo "║  Version: 3.0.0 | Build: 20250801-182338                                      ║"
    echo "║  Author: 0x4ymn | Team: m4sec.team                                             ║"
    echo "║                                                                                  ║"
    echo "╚══════════════════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    echo
}

# Remove Python packages
remove_python_deps() {
    log_info "Removing Python dependencies..."
    
    # List of packages to remove
    PACKAGES=(
        "colorama"
        "psutil" 
        "rich"
        "click"
        "tqdm"
        "pyyaml"
        "requests"
    )
    
    for package in "${PACKAGES[@]}"; do
        if pip3 show "$package" >/dev/null 2>&1; then
            log_info "Removing $package..."
            pip3 uninstall -y "$package" 2>/dev/null || log_warning "Failed to remove $package"
        fi
    done
    
    log_success "Python dependencies cleanup completed"
    echo
}

# Clean up directories and files
cleanup_files() {
    log_info "Cleaning up M4SEC Toolkit files..."
    
    # Remove logs
    if [ -d "logs" ]; then
        rm -rf logs
        log_success "Removed logs directory"
    fi
    
    # Remove user output directory
    OUTPUT_DIR="$HOME/m4sec_output"
    if [ -d "$OUTPUT_DIR" ]; then
        log_info "Found output directory: $OUTPUT_DIR"
        read -p "Remove output directory and all files? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf "$OUTPUT_DIR"
            log_success "Removed output directory"
        else
            log_info "Kept output directory"
        fi
    fi
    
    # Clean temporary files
    log_info "Cleaning temporary files..."
    rm -f /tmp/m4sec_* 2>/dev/null || true
    
    # Remove Python cache
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    
    log_success "File cleanup completed"
    echo
}

# Remove configuration (optional)
remove_config() {
    log_info "Configuration files found in config/"
    read -p "Remove configuration files? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -f config/settings.json.bak 2>/dev/null || true
        log_success "Removed configuration backups"
    else
        log_info "Kept configuration files"
    fi
    echo
}

# Show what will be removed
show_removal_plan() {
    log_info "The following will be removed:"
    echo "  • Python dependencies (colorama, psutil, rich, etc.)"
    echo "  • Log files and temporary files"
    echo "  • Python cache files (__pycache__, *.pyc)"
    echo
    log_info "The following will be kept:"
    echo "  • Main source code (src/, config/, scripts/, docs/)"
    echo "  • Security tools installed separately"
    echo "  • System packages and dependencies"
    echo
    log_warning "User data in ~/m4sec_output/ will be optionally removed"
    echo
}

# Confirm uninstallation
confirm_uninstall() {
    echo -e "${YELLOW}"
    echo "⚠️  WARNING: This will remove M4SEC Toolkit components from your system"
    echo -e "${NC}"
    echo
    read -p "Are you sure you want to continue? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log_info "Uninstallation cancelled by user"
        exit 0
    fi
    echo
}

# Main uninstallation function
main() {
    print_banner
    
    log_info "M4SEC Toolkit Uninstaller"
    log_info "This will remove M4SEC Toolkit components from your system"
    echo
    
    show_removal_plan
    confirm_uninstall
    
    echo "================================="
    echo "    M4SEC TOOLKIT REMOVAL"
    echo "================================="
    echo
    
    # Run removal steps
    remove_python_deps
    cleanup_files
    remove_config
    
    # Final message
    echo "================================="
    echo "      REMOVAL COMPLETE"
    echo "================================="
    echo
    log_success "M4SEC Toolkit has been removed from your system"
    echo
    log_info "Thank you for using M4SEC Toolkit!"
    log_info "Visit m4sec.team for other security tools and resources"
    echo
    log_info "To reinstall in the future, run: ./scripts/install.sh"
    echo
    
    # Show remaining files
    log_info "Remaining files:"
    log_info "  • Source code is still available in current directory"
    log_info "  • Security tools installed separately are still available"
    log_info "  • System packages remain unchanged"
    echo
    
    echo -e "${GREEN}Goodbye! 👋${NC}"
}

# Check if we're in the right directory
if [ ! -f "src/main.py" ] || [ ! -d "scripts" ]; then
    log_error "Please run this script from the M4SEC Toolkit root directory"
    log_info "Expected structure: src/, config/, scripts/, docs/"
    exit 1
fi

# Run main function
main "$@"