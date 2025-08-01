#!/bin/bash
# M4SEC Toolkit Virtual Environment Activation Script
# 
# This script activates the M4SEC virtual environment and provides
# a convenient way to launch the toolkit with proper environment setup.

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

# Check for virtual environment
VENV_PATH="$HOME/.m4sec_venv"

if [ ! -d "$VENV_PATH" ]; then
    log_error "M4SEC virtual environment not found at $VENV_PATH"
    log_info "Please run the installation script first: ./scripts/install.sh"
    exit 1
fi

if [ ! -f "$VENV_PATH/bin/activate" ]; then
    log_error "Virtual environment activation script not found"
    log_info "Please reinstall M4SEC Toolkit: ./scripts/install.sh"
    exit 1
fi

# Show banner
echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════════════════════════╗"
echo "║                          M4SEC TOOLKIT LAUNCHER                             ║"
echo "║                     Virtual Environment Activation                          ║"
echo "╚══════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

log_info "Activating M4SEC virtual environment..."
log_info "Environment path: $VENV_PATH"

# Activate virtual environment
# shellcheck source=/dev/null
source "$VENV_PATH/bin/activate"

log_success "Virtual environment activated!"
echo

# Check if running from correct directory
if [ ! -f "src/main.py" ]; then
    log_warning "Not in M4SEC Toolkit root directory"
    log_info "Please run this script from the M4SEC Toolkit root directory"
    exit 1
fi

# Parse command line arguments
if [ $# -eq 0 ]; then
    # No arguments - run interactive mode
    log_info "Starting M4SEC Toolkit in interactive mode..."
    python3 src/main.py
elif [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    # Show help
    python3 src/main.py --help
else
    # Pass all arguments to main.py
    log_info "Starting M4SEC Toolkit with arguments: $*"
    python3 src/main.py "$@"
fi