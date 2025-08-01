#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
ASCII art banners and branding

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
"""

from ui.colors import ColorFormatter, clear_screen


class BannerManager:
    """Manages ASCII art banners and branding for M4SEC Toolkit"""
    
    def __init__(self, formatter: ColorFormatter = None):
        self.formatter = formatter or ColorFormatter()
    
    def get_main_banner(self) -> str:
        """Get the main M4SEC banner"""
        return """████████████████████████████████████████████████████████████████████████████████
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
████████████████████████████████████████████████████████████████████████████████"""
    
    def get_small_banner(self) -> str:
        """Get a smaller M4SEC banner for sub-pages"""
        return """╔══════════════════════════════════════════════════════════════════════════════════╗
║  M4SEC Ultimate CTF & Security Toolkit Manager v3.0.0                           ║
║  Professional All-in-One Launcher | Build: 20250801-182338                      ║
╚══════════════════════════════════════════════════════════════════════════════════╝"""
    
    def get_tool_banner(self, tool_name: str, category: str) -> str:
        """Get banner for tool launch"""
        return f"""┌──────────────────────────────────────────────────────────────────────────────────┐
│  M4SEC Toolkit - Tool Launcher                                                  │
│  Category: {category:<68} │
│  Tool: {tool_name:<72} │
│  Time: 2025-08-01 18:23:38                                                      │
└──────────────────────────────────────────────────────────────────────────────────┘"""
    
    def get_health_banner(self) -> str:
        """Get banner for health check"""
        return """┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  M4SEC SYSTEM HEALTH CHECK                                                     ┃
┃  Comprehensive Security Toolkit Status Report                                 ┃
┃  Generated: 2025-08-01 18:23:38                                               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
    
    def get_category_banner(self, category_name: str, category_id: str) -> str:
        """Get banner for category selection"""
        return f"""╭─────────────────────────────────────────────────────────────────────────────────╮
│  M4SEC Toolkit - Category {category_id}                                              │
│  {category_name:<75} │
│  Select your tool and configure parameters                                     │
╰─────────────────────────────────────────────────────────────────────────────────╯"""
    
    def get_ascii_art_m4sec(self) -> str:
        """Get ASCII art version of M4SEC logo"""
        return """
    ███╗   ███╗██╗  ██╗███████╗███████╗ ██████╗ 
    ████╗ ████║██║  ██║██╔════╝██╔════╝██╔════╝ 
    ██╔████╔██║███████║███████╗█████╗  ██║      
    ██║╚██╔╝██║╚════██║╚════██║██╔══╝  ██║      
    ██║ ╚═╝ ██║     ██║███████║███████╗╚██████╗ 
    ╚═╝     ╚═╝     ╚═╝╚══════╝╚══════╝ ╚═════╝ 
"""
    
    def get_loading_banner(self) -> str:
        """Get loading banner"""
        return """
    ┌─ M4SEC Toolkit Loading ─┐
    │  ██████████████████████  │
    │  Loading components...   │
    └─────────────────────────┘
"""
    
    def get_goodbye_banner(self) -> str:
        """Get goodbye banner"""
        return """
╔═══════════════════════════════════════════════════════════════════════════════════╗
║                                                                                   ║
║  Thank you for using M4SEC Ultimate CTF & Security Toolkit Manager!             ║
║                                                                                   ║
║  🔐 Stay secure, stay vigilant                                                   ║
║  🚀 Keep learning, keep hacking                                                  ║
║  🎯 Good luck in your security journey!                                         ║
║                                                                                   ║
║  Team: m4sec.team | Author: 0x4ymn                                              ║
║  UTC: 2025-08-01 18:23:38                                                       ║
║                                                                                   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
"""
    
    def print_main_banner(self, clear: bool = True) -> None:
        """Print the main banner with colors"""
        if clear:
            clear_screen()
        
        banner = self.get_main_banner()
        print(self.formatter.brand_primary(banner))
        print()
    
    def print_small_banner(self) -> None:
        """Print small banner with colors"""
        banner = self.get_small_banner()
        print(self.formatter.brand_secondary(banner))
        print()
    
    def print_tool_banner(self, tool_name: str, category: str) -> None:
        """Print tool launch banner"""
        banner = self.get_tool_banner(tool_name, category)
        print(self.formatter.info(banner))
        print()
    
    def print_health_banner(self) -> None:
        """Print health check banner"""
        banner = self.get_health_banner()
        print(self.formatter.header(banner))
        print()
    
    def print_category_banner(self, category_name: str, category_id: str) -> None:
        """Print category banner"""
        banner = self.get_category_banner(category_name, category_id)
        print(self.formatter.brand_secondary(banner))
        print()
    
    def print_loading_animation(self, steps: int = 20) -> None:
        """Print a simple loading animation"""
        import time
        import sys
        
        print(self.formatter.info("M4SEC Toolkit initializing..."))
        
        for i in range(steps + 1):
            percentage = (i / steps) * 100
            filled = "█" * i
            empty = "░" * (steps - i)
            
            bar = self.formatter.colorize(filled + empty, self.formatter.Colors.GREEN)
            percentage_text = self.formatter.highlight(f"{percentage:.0f}%")
            
            print(f"\r[{bar}] {percentage_text}", end="", flush=True)
            time.sleep(0.1)
        
        print("\n")
        print(self.formatter.success("M4SEC Toolkit ready!"))
        time.sleep(0.5)
    
    def print_goodbye_banner(self) -> None:
        """Print goodbye banner"""
        banner = self.get_goodbye_banner()
        print(self.formatter.brand_primary(banner))
    
    def print_separator(self, width: int = 80, char: str = "─") -> None:
        """Print a separator line"""
        separator = char * width
        print(self.formatter.dim(separator))
    
    def print_section_header(self, title: str, width: int = 80) -> None:
        """Print a section header"""
        padding = (width - len(title) - 4) // 2
        header = f"{'─' * padding} {title} {'─' * padding}"
        if len(header) < width:
            header += "─" * (width - len(header))
        print(self.formatter.header(header))
    
    def print_warning_box(self, message: str) -> None:
        """Print a warning message in a box"""
        lines = message.split('\n')
        max_length = max(len(line) for line in lines)
        width = max_length + 4
        
        print(self.formatter.warning("┌" + "─" * (width - 2) + "┐"))
        for line in lines:
            padded_line = f"│ {line:<{max_length}} │"
            print(self.formatter.warning(padded_line))
        print(self.formatter.warning("└" + "─" * (width - 2) + "┘"))
    
    def print_info_box(self, message: str) -> None:
        """Print an info message in a box"""
        lines = message.split('\n')
        max_length = max(len(line) for line in lines)
        width = max_length + 4
        
        print(self.formatter.info("┌" + "─" * (width - 2) + "┐"))
        for line in lines:
            padded_line = f"│ {line:<{max_length}} │"
            print(self.formatter.info(padded_line))
        print(self.formatter.info("└" + "─" * (width - 2) + "┘"))


# Global banner manager instance
banner_manager = BannerManager()