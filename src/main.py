#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
Main entry point with argument parsing and launcher initialization

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
User: 0x4ymn

Usage:
    python3 src/main.py                    # Interactive mode
    python3 src/main.py --setup           # Full system setup
    python3 src/main.py --health          # Health check
    python3 src/main.py --tool nmap       # Launch nmap directly
    python3 src/main.py --list-tools      # List all tools
    python3 src/main.py --version         # Show version
"""

import sys
import os
import argparse
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.config_manager import ConfigManager
from core.tool_manager import ToolManager
from core.terminal_launcher import TerminalLauncher
from core.utils import logger, get_build_info, check_security, SystemInfo
from ui.menu import MenuSystem
from ui.colors import ColorFormatter, print_separator
from ui.banner import BannerManager


class M4SECToolkit:
    """Main M4SEC Toolkit application class"""
    
    def __init__(self):
        self.formatter = ColorFormatter()
        self.banner = BannerManager(self.formatter)
        
        # Initialize core components
        try:
            self.config = ConfigManager()
            self.tool_manager = ToolManager(self.config)
            self.terminal = TerminalLauncher(self.config)
            self.menu = MenuSystem(self.config, self.tool_manager, self.terminal)
        except Exception as e:
            print(f"Error initializing M4SEC Toolkit: {e}")
            logger.error(f"Initialization error: {e}")
            sys.exit(1)
    
    def show_version(self) -> None:
        """Display version information"""
        build_info = get_build_info()
        
        print(self.formatter.header("M4SEC Ultimate CTF & Security Toolkit Manager"))
        print_separator(60, "═")
        print(f"Version:     {self.formatter.highlight(build_info['version'])}")
        print(f"Build:       {self.formatter.info(build_info['build'])}")
        print(f"Author:      {self.formatter.info(build_info['author'])}")
        print(f"Team:        {self.formatter.info(build_info['team'])}")
        print(f"UTC:         {self.formatter.info(build_info['utc'])}")
        print(f"User:        {self.formatter.info(build_info['user'])}")
        print_separator(60, "═")
    
    def run_health_check(self) -> None:
        """Run comprehensive health check"""
        self.banner.print_health_banner()
        
        # Security check
        security_check = check_security()
        
        if security_check["is_root"]:
            self.banner.print_warning_box(
                "SECURITY WARNING: Running as root is not recommended!\n"
                "Please run M4SEC Toolkit as a regular user for security."
            )
        
        if not security_check["python_version_ok"]:
            print(self.formatter.error("Python 3.8+ is required"))
            sys.exit(1)
        
        # Show detailed health information
        self.menu.show_health_status()
    
    def list_all_tools(self) -> None:
        """List all available tools by category"""
        self.banner.print_small_banner()
        
        print(self.formatter.header("📋 ALL AVAILABLE TOOLS"))
        print_separator(80, "═")
        
        categories = self.config.get_categories()
        if not categories:
            print(self.formatter.error("No tool categories found"))
            return
        
        total_tools = 0
        installed_tools = 0
        
        for cat_id, category in categories.items():
            name = category.get("name", f"Category {cat_id}")
            tools = category.get("tools", {})
            
            if not tools:
                continue
            
            print(f"\n{self.formatter.header(f'[{cat_id}] {name}')}")
            print_separator(60, "─")
            
            for tool_name, tool_config in tools.items():
                command = tool_config.get("command", tool_name)
                description = tool_config.get("description", "No description")
                is_installed = self.tool_manager.check_tool_installed(command)
                
                total_tools += 1
                if is_installed:
                    installed_tools += 1
                    status = self.formatter.success("✓ INSTALLED")
                else:
                    status = self.formatter.error("✗ MISSING")
                
                print(f"  {tool_name:<15} {status}")
                print(f"    {self.formatter.dim(description)}")
        
        print(f"\n{print_separator(80, '═')}")
        print(f"Total Tools: {self.formatter.highlight(str(total_tools))}")
        print(f"Installed:   {self.formatter.success(str(installed_tools))}")
        print(f"Missing:     {self.formatter.error(str(total_tools - installed_tools))}")
        coverage_percentage = f'{(installed_tools/total_tools*100):.1f}%' if total_tools > 0 else '0%'
        print(f"Coverage:    {self.formatter.info(coverage_percentage)}")
    
    def launch_tool_direct(self, tool_name: str) -> None:
        """Launch a specific tool directly"""
        print(self.formatter.status(f"Searching for tool: {tool_name}"))
        
        # Find tool in all categories
        categories = self.config.get_categories()
        if not categories:
            print(self.formatter.error("No tool categories found"))
            return
        
        found_tool = None
        found_category = None
        
        for cat_id, category in categories.items():
            tools = category.get("tools", {})
            if tool_name in tools:
                found_tool = tools[tool_name]
                found_category = cat_id
                break
            
            # Check by command name too
            for t_name, t_config in tools.items():
                if t_config.get("command", t_name) == tool_name:
                    found_tool = t_config
                    found_category = cat_id
                    tool_name = t_name  # Use the config name
                    break
        
        if not found_tool:
            print(self.formatter.error(f"Tool '{tool_name}' not found in configuration"))
            print("Use --list-tools to see all available tools")
            return
        
        command = found_tool.get("command", tool_name)
        
        if not self.tool_manager.check_tool_installed(command):
            print(self.formatter.error(f"Tool '{tool_name}' is not installed"))
            install_cmd = self.tool_manager.suggest_installation_command(command)
            print(f"Install with: {self.formatter.info(install_cmd)}")
            return
        
        print(self.formatter.success(f"Found tool: {tool_name}"))
        
        # Configure parameters interactively
        parameters = self.menu.configure_tool_parameters(tool_name, found_tool)
        if parameters is None:
            return
        
        # Launch tool
        print(self.formatter.status("Launching tool..."))
        if self.terminal.launch_tool(tool_name, found_tool, parameters):
            print(self.formatter.success(f"Successfully launched {tool_name}"))
        else:
            print(self.formatter.error(f"Failed to launch {tool_name}"))
    
    def run_setup(self) -> None:
        """Run full system setup"""
        self.banner.print_main_banner(clear=True)
        
        print(self.formatter.header("🔧 M4SEC TOOLKIT SYSTEM SETUP"))
        print_separator(80, "═")
        print()
        
        # Security check
        if SystemInfo.is_root():
            self.banner.print_warning_box(
                "SECURITY WARNING: Running as root detected!\n"
                "Setup should be run as a regular user.\n"
                "Some operations may require sudo permissions."
            )
            
            confirm = input(self.formatter.warning("Continue anyway? (y/N): "))
            if confirm.lower() not in ['y', 'yes']:
                print(self.formatter.info("Setup cancelled"))
                return
        
        print(self.formatter.info("Starting M4SEC Toolkit setup..."))
        print()
        
        # Check system compatibility
        print(self.formatter.status("Checking system compatibility..."))
        
        if not SystemInfo.check_python_version():
            print(self.formatter.error("Python 3.8+ is required"))
            return
        
        terminals = SystemInfo.get_available_terminals()
        if not terminals:
            print(self.formatter.warning("No compatible terminal emulators found"))
            print("Install one of: gnome-terminal, konsole, xfce4-terminal, xterm")
        else:
            print(self.formatter.success(f"Found {len(terminals)} compatible terminals"))
        
        # Display missing tools
        missing_tools = self.tool_manager.get_missing_tools()
        if missing_tools:
            print(f"\n{self.formatter.header(f'MISSING TOOLS ({len(missing_tools)} found):')}")
            print_separator(60, "─")
            
            categories_shown = set()
            for tool in missing_tools[:20]:  # Show first 20
                category = tool["category"]
                if category not in categories_shown:
                    print(f"\n{self.formatter.highlight(category)}:")
                    categories_shown.add(category)
                
                name = tool["name"]
                command = tool["command"]
                install_cmd = self.tool_manager.suggest_installation_command(command)
                
                print(f"  • {name} ({command})")
                print(f"    {self.formatter.dim(install_cmd)}")
        
        print(f"\n{self.formatter.header('SETUP COMPLETE')}")
        print_separator(80, "═")
        print(self.formatter.success("M4SEC Toolkit is ready to use!"))
        print("Run without arguments to start the interactive menu.")
    
    def run_interactive(self) -> None:
        """Run interactive menu mode"""
        # Initial security check
        security_check = check_security()
        
        if security_check["is_root"]:
            self.banner.print_warning_box(
                "SECURITY WARNING: Running as root is not recommended!\n"
                "M4SEC Toolkit should be run as a regular user for security.\n"
                "Press Ctrl+C to exit or Enter to continue anyway."
            )
            try:
                input()
            except KeyboardInterrupt:
                print("\n" + self.formatter.info("Exiting for security..."))
                sys.exit(0)
        
        if not security_check["python_version_ok"]:
            print(self.formatter.error("Python 3.8+ is required"))
            sys.exit(1)
        
        if not security_check["terminals_available"]:
            print(self.formatter.error("No compatible terminal emulators found"))
            print("Please install one of: gnome-terminal, konsole, xfce4-terminal, xterm")
            sys.exit(1)
        
        # Start interactive menu
        self.menu.run()


def create_argument_parser() -> argparse.ArgumentParser:
    """Create command line argument parser"""
    parser = argparse.ArgumentParser(
        description="M4SEC Ultimate CTF & Security Toolkit Manager v3.0.0",
        epilog="Visit m4sec.team for more information",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--setup",
        action="store_true",
        help="Run full system setup and tool installation guide"
    )
    
    parser.add_argument(
        "--health",
        action="store_true", 
        help="Display system health check and tool status"
    )
    
    parser.add_argument(
        "--tool",
        type=str,
        metavar="TOOL_NAME",
        help="Launch specific tool directly (e.g., --tool nmap)"
    )
    
    parser.add_argument(
        "--list-tools",
        action="store_true",
        help="List all available tools by category"
    )
    
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version information"
    )
    
    parser.add_argument(
        "--config",
        type=str,
        metavar="FILE",
        help="Use custom configuration file"
    )
    
    return parser


def main() -> None:
    """Main entry point"""
    try:
        parser = create_argument_parser()
        args = parser.parse_args()
        
        # Initialize the toolkit
        toolkit = M4SECToolkit()
        
        # Handle command line arguments
        if args.version:
            toolkit.show_version()
        elif args.health:
            toolkit.run_health_check()
        elif args.list_tools:
            toolkit.list_all_tools()
        elif args.tool:
            toolkit.launch_tool_direct(args.tool)
        elif args.setup:
            toolkit.run_setup()
        else:
            # Default: run interactive mode
            toolkit.run_interactive()
    
    except KeyboardInterrupt:
        print("\n🔒 M4SEC Toolkit terminated by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()