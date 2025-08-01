#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
ANSI color utilities and formatted printing functions

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
"""

import os
import sys
from typing import Optional


class Colors:
    """ANSI color codes for terminal output"""
    
    # Reset
    RESET = '\033[0m'
    
    # Regular colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bold colors
    BOLD_BLACK = '\033[1;30m'
    BOLD_RED = '\033[1;31m'
    BOLD_GREEN = '\033[1;32m'
    BOLD_YELLOW = '\033[1;33m'
    BOLD_BLUE = '\033[1;34m'
    BOLD_MAGENTA = '\033[1;35m'
    BOLD_CYAN = '\033[1;36m'
    BOLD_WHITE = '\033[1;37m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Text styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    STRIKETHROUGH = '\033[9m'


class ColorFormatter:
    """Professional color formatting for M4SEC Toolkit"""
    
    def __init__(self, use_colors: bool = None):
        if use_colors is None:
            # Auto-detect color support
            self.use_colors = self._supports_color()
        else:
            self.use_colors = use_colors
    
    def _supports_color(self) -> bool:
        """Check if terminal supports colors"""
        # Check environment variables
        if os.environ.get('NO_COLOR'):
            return False
        
        if os.environ.get('FORCE_COLOR'):
            return True
        
        # Check if output is a TTY
        if not hasattr(sys.stdout, 'isatty') or not sys.stdout.isatty():
            return False
        
        # Check TERM environment variable
        term = os.environ.get('TERM', '')
        if term in ['dumb', 'unknown']:
            return False
        
        return True
    
    def colorize(self, text: str, color: str) -> str:
        """Apply color to text if colors are enabled"""
        if not self.use_colors:
            return text
        return f"{color}{text}{Colors.RESET}"
    
    # Semantic color methods for M4SEC branding
    def header(self, text: str) -> str:
        """Format header text (Bold Blue)"""
        return self.colorize(text, Colors.BOLD_BLUE)
    
    def success(self, text: str) -> str:
        """Format success text (Green with ✓)"""
        symbol = "✓" if self.use_colors else "[OK]"
        return self.colorize(f"{symbol} {text}", Colors.GREEN)
    
    def warning(self, text: str) -> str:
        """Format warning text (Yellow with !)"""
        symbol = "!" if self.use_colors else "[WARN]"
        return self.colorize(f"{symbol} {text}", Colors.YELLOW)
    
    def error(self, text: str) -> str:
        """Format error text (Red with ✗)"""
        symbol = "✗" if self.use_colors else "[ERROR]"
        return self.colorize(f"{symbol} {text}", Colors.RED)
    
    def info(self, text: str) -> str:
        """Format info text (Cyan with i)"""
        symbol = "i" if self.use_colors else "[INFO]"
        return self.colorize(f"{symbol} {text}", Colors.CYAN)
    
    def status(self, text: str) -> str:
        """Format status text (Blue with ●)"""
        symbol = "●" if self.use_colors else "[*]"
        return self.colorize(f"{symbol} {text}", Colors.BLUE)
    
    def menu_number(self, number: str) -> str:
        """Format menu numbers (Green)"""
        return self.colorize(number, Colors.BOLD_GREEN)
    
    def menu_description(self, text: str) -> str:
        """Format menu descriptions (Cyan)"""
        return self.colorize(text, Colors.CYAN)
    
    def tool_installed(self, text: str) -> str:
        """Format installed tool (Green with ✅)"""
        symbol = "✅" if self.use_colors else "[INSTALLED]"
        return self.colorize(f"{symbol} {text}", Colors.GREEN)
    
    def tool_missing(self, text: str) -> str:
        """Format missing tool (Red with ❌)"""
        symbol = "❌" if self.use_colors else "[MISSING]"
        return self.colorize(f"{symbol} {text}", Colors.RED)
    
    def highlight(self, text: str) -> str:
        """Highlight important text (Bold White)"""
        return self.colorize(text, Colors.BOLD_WHITE)
    
    def dim(self, text: str) -> str:
        """Dim less important text"""
        return self.colorize(text, Colors.DIM)
    
    def brand_primary(self, text: str) -> str:
        """Primary brand color (Bold Blue)"""
        return self.colorize(text, Colors.BOLD_BLUE)
    
    def brand_secondary(self, text: str) -> str:
        """Secondary brand color (Cyan)"""
        return self.colorize(text, Colors.BOLD_CYAN)


class ProgressBar:
    """Simple progress bar for operations"""
    
    def __init__(self, total: int, width: int = 50, formatter: ColorFormatter = None):
        self.total = total
        self.width = width
        self.current = 0
        self.formatter = formatter or ColorFormatter()
    
    def update(self, current: int) -> None:
        """Update progress bar"""
        self.current = current
        self.display()
    
    def increment(self) -> None:
        """Increment progress by 1"""
        self.current += 1
        self.display()
    
    def display(self) -> None:
        """Display current progress"""
        if self.total == 0:
            return
        
        percentage = min(100, (self.current / self.total) * 100)
        filled_width = int(self.width * self.current // self.total)
        
        # Create progress bar
        bar = "█" * filled_width + "░" * (self.width - filled_width)
        
        # Format with colors
        colored_bar = self.formatter.colorize(bar, Colors.GREEN)
        percentage_text = self.formatter.highlight(f"{percentage:.1f}%")
        
        # Display
        print(f"\r{colored_bar} {percentage_text} ({self.current}/{self.total})", end="", flush=True)
    
    def finish(self) -> None:
        """Finish progress bar"""
        self.current = self.total
        self.display()
        print()  # New line


def print_separator(char: str = "─", width: int = 80, formatter: ColorFormatter = None) -> None:
    """Print a separator line"""
    formatter = formatter or ColorFormatter()
    separator = char * width
    print(formatter.dim(separator))


def print_centered(text: str, width: int = 80, formatter: ColorFormatter = None) -> None:
    """Print centered text"""
    formatter = formatter or ColorFormatter()
    padding = (width - len(text)) // 2
    centered_text = " " * padding + text
    print(formatter.highlight(centered_text))


def clear_screen() -> None:
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_terminal_size() -> tuple:
    """Get terminal size (width, height)"""
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except OSError:
        return 80, 24  # Default fallback


def format_table(
    headers: list, 
    rows: list, 
    formatter: ColorFormatter = None
) -> str:
    """Format data as a table"""
    formatter = formatter or ColorFormatter()
    
    if not headers or not rows:
        return ""
    
    # Calculate column widths
    col_widths = [len(header) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(col_widths):
                col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Format header
    header_line = " | ".join(
        formatter.header(header.ljust(col_widths[i])) 
        for i, header in enumerate(headers)
    )
    
    # Format separator
    separator = "-+-".join("-" * width for width in col_widths)
    
    # Format rows
    formatted_rows = []
    for row in rows:
        formatted_row = " | ".join(
            str(cell).ljust(col_widths[i]) 
            for i, cell in enumerate(row)
        )
        formatted_rows.append(formatted_row)
    
    # Combine
    table = [header_line, formatter.dim(separator)] + formatted_rows
    return "\n".join(table)


# Global formatter instance
color_formatter = ColorFormatter()


# Convenience functions
def print_header(text: str) -> None:
    """Print header text"""
    print(color_formatter.header(text))


def print_success(text: str) -> None:
    """Print success message"""
    print(color_formatter.success(text))


def print_warning(text: str) -> None:
    """Print warning message"""
    print(color_formatter.warning(text))


def print_error(text: str) -> None:
    """Print error message"""
    print(color_formatter.error(text))


def print_info(text: str) -> None:
    """Print info message"""
    print(color_formatter.info(text))


def print_status(text: str) -> None:
    """Print status message"""
    print(color_formatter.status(text))