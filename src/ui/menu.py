#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
Interactive menu system with category and tool selection

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
"""

import sys
import time
from typing import Dict, List, Optional, Any, Tuple
from core.config_manager import ConfigManager
from core.tool_manager import ToolManager
from core.terminal_launcher import TerminalLauncher
from core.utils import logger, validate_input
from ui.colors import ColorFormatter, print_separator
from ui.banner import BannerManager


class MenuSystem:
    """Interactive menu system for M4SEC Toolkit"""
    
    def __init__(
        self, 
        config_manager: ConfigManager,
        tool_manager: ToolManager,
        terminal_launcher: TerminalLauncher
    ):
        self.config = config_manager
        self.tool_manager = tool_manager
        self.terminal = terminal_launcher
        self.formatter = ColorFormatter()
        self.banner = BannerManager(self.formatter)
        
        # Menu state
        self.current_category = None
        self.running = True
    
    def show_main_menu(self) -> None:
        """Display the main category menu"""
        self.banner.print_main_banner()
        
        categories = self.config.get_categories()
        if not categories:
            self.formatter.error("No tool categories found in configuration")
            return
        
        print(self.formatter.header("🔧 SECURITY TOOL CATEGORIES"))
        print_separator(80, "═")
        print()
        
        # Display categories in a professional format
        for cat_id, category in categories.items():
            name = category.get("name", f"Category {cat_id}")
            description = category.get("description", "No description available")
            tools_count = len(category.get("tools", {}))
            
            # Get installed tools count for this category
            installed_count = 0
            for tool_name, tool_config in category.get("tools", {}).items():
                command = tool_config.get("command", tool_name)
                if self.tool_manager.check_tool_installed(command):
                    installed_count += 1
            
            status_text = f"({installed_count}/{tools_count} tools installed)"
            
            cat_id_str = f'[{cat_id}]'
            print(f"  {self.formatter.menu_number(cat_id_str)} "
                  f"{self.formatter.highlight(name)}")
            print(f"      {self.formatter.menu_description(description)}")
            
            if installed_count == tools_count and tools_count > 0:
                print(f"      {self.formatter.success(status_text)}")
            elif installed_count > 0:
                print(f"      {self.formatter.warning(status_text)}")
            else:
                print(f"      {self.formatter.error(status_text)}")
            print()
        
        print_separator(80, "─")
        print()
        
        # Additional options
        print(self.formatter.header("📊 ADDITIONAL OPTIONS"))
        print(f"  {self.formatter.menu_number('[s]')} "
              f"{self.formatter.menu_description('System Status & Health Check')}")
        print(f"  {self.formatter.menu_number('[h]')} "
              f"{self.formatter.menu_description('Help & Documentation')}")
        print(f"  {self.formatter.menu_number('[q]')} "
              f"{self.formatter.menu_description('Quit M4SEC Toolkit')}")
        print()
        print_separator(80, "═")
    
    def show_category_menu(self, category_id: str) -> None:
        """Display tools in a specific category"""
        categories = self.config.get_categories()
        if not categories or category_id not in categories:
            self.formatter.error(f"Category {category_id} not found")
            return
        
        category = categories[category_id]
        category_name = category.get("name", f"Category {category_id}")
        
        self.banner.print_category_banner(category_name, category_id)
        
        tools = category.get("tools", {})
        if not tools:
            print(self.formatter.warning("No tools found in this category"))
            return
        
        print(self.formatter.header(f"🛠️  TOOLS IN {category_name.upper()}"))
        print_separator(80, "═")
        print()
        
        # Display tools with installation status
        tool_counter = 1
        for tool_name, tool_config in tools.items():
            name = tool_config.get("name", tool_name)
            description = tool_config.get("description", "No description available")
            command = tool_config.get("command", tool_name)
            
            is_installed = self.tool_manager.check_tool_installed(command)
            
            # Format tool entry
            status_symbol = "✅" if is_installed else "❌"
            tool_number = self.formatter.menu_number(f"[{tool_counter}]")
            tool_name_display = self.formatter.highlight(name)
            
            print(f"  {tool_number} {status_symbol} {tool_name_display}")
            print(f"      {self.formatter.menu_description(description)}")
            
            if is_installed:
                version = self.tool_manager.get_tool_version(command)
                if version and version != "Version unknown":
                    version_str = f'Version: {version}'
                    print(f"      {self.formatter.dim(version_str)}")
                path = self.tool_manager.get_tool_path(command)
                if path:
                    path_str = f'Path: {path}'
                    print(f"      {self.formatter.dim(path_str)}")
            else:
                install_cmd = self.tool_manager.suggest_installation_command(command)
                install_str = f'Install: {install_cmd}'
                print(f"      {self.formatter.warning(install_str)}")
            
            print()
            tool_counter += 1
        
        print_separator(80, "─")
        print()
        print(f"  {self.formatter.menu_number('[b]')} "
              f"{self.formatter.menu_description('Back to Main Menu')}")
        print(f"  {self.formatter.menu_number('[r]')} "
              f"{self.formatter.menu_description('Refresh Tool Status')}")
        print(f"  {self.formatter.menu_number('[q]')} "
              f"{self.formatter.menu_description('Quit')}")
        print()
        print_separator(80, "═")
    
    def show_health_status(self) -> None:
        """Display system health and tool status"""
        self.banner.print_health_banner()
        
        health = self.tool_manager.get_system_health()
        
        # Overall status
        status_color = self.formatter.success if health["status"] == "healthy" else self.formatter.warning
        print(status_color(f"Overall Status: {health['status'].title()}"))
        print()
        
        # Tools summary
        print(self.formatter.header("🛠️  TOOLS SUMMARY"))
        print_separator(60, "─")
        tools_info = health["tools"]
        print(f"Total Tools:     {self.formatter.highlight(str(tools_info['total']))}")
        print(f"Installed:       {self.formatter.success(str(tools_info['installed']))}")
        print(f"Missing:         {self.formatter.error(str(tools_info['missing']))}")
        coverage_text = f"{tools_info['percentage']:.1f}%"
        print(f"Coverage:        {self.formatter.info(coverage_text)}")
        print()
        
        # System information
        print(self.formatter.header("💻 SYSTEM INFORMATION"))
        print_separator(60, "─")
        system_info = health["system"]
        print(f"Platform:        {self.formatter.info(system_info['platform'])}")
        print(f"Python Version:  {self.formatter.info(system_info['python_version'])}")
        
        if system_info['python_compatible']:
            print(f"Python Status:   {self.formatter.success('Compatible')}")
        else:
            print(f"Python Status:   {self.formatter.error('Incompatible (3.8+ required)')}")
        
        if system_info['is_root']:
            print(f"User Status:     {self.formatter.error('Running as root (NOT RECOMMENDED)')}")
        else:
            print(f"User Status:     {self.formatter.success('Running as regular user')}")
        print()
        
        # Terminal information
        print(self.formatter.header("🖥️  TERMINAL SUPPORT"))
        print_separator(60, "─")
        terminal_info = health["terminals"]
        print(f"Available:       {self.formatter.highlight(str(terminal_info['count']))}")
        
        if terminal_info["has_terminal"]:
            print(f"Status:          {self.formatter.success('Terminal support available')}")
            for terminal in terminal_info["available"]:
                print(f"  • {self.formatter.info(terminal)}")
        else:
            print(f"Status:          {self.formatter.error('No compatible terminals found')}")
        print()
        
        # Missing tools (top 10)
        if health["missing_tools"]:
            print(self.formatter.header("❌ MISSING TOOLS (Top 10)"))
            print_separator(60, "─")
            for tool in health["missing_tools"]:
                category = tool["category"]
                name = tool["name"]
                command = tool["command"]
                install_cmd = self.tool_manager.suggest_installation_command(command)
                
                print(f"• {self.formatter.error(name)} ({category})")
                install_str = f'Install: {install_cmd}'
                print(f"  {self.formatter.dim(install_str)}")
        print()
        
        print_separator(80, "═")
        print(f"{self.formatter.menu_description('Press Enter to continue...')}")
        input()
    
    def configure_tool_parameters(
        self, 
        tool_name: str, 
        tool_config: Dict[str, Any]
    ) -> Optional[Dict[str, str]]:
        """Interactive parameter configuration for a tool"""
        parameters = tool_config.get("parameters", {})
        if not parameters:
            return {}
        
        print(self.formatter.header(f"🔧 CONFIGURE {tool_name.upper()}"))
        print_separator(60, "─")
        print(self.formatter.info("Configure parameters for the tool. Press Enter for defaults."))
        print()
        
        configured_params = {}
        
        for param_name, param_config in parameters.items():
            param_type = param_config.get("type", "input")
            description = param_config.get("description", param_name)
            default = param_config.get("default")
            required = param_config.get("required", False)
            choices = param_config.get("choices", [])
            
            while True:
                # Display parameter info
                param_display = self.formatter.highlight(param_name.replace('_', ' ').title())
                print(f"{param_display}: {self.formatter.menu_description(description)}")
                
                if param_type == "choice" and choices:
                    print(f"  Choices: {self.formatter.info(', '.join(choices))}")
                
                if default:
                    print(f"  Default: {self.formatter.dim(str(default))}")
                
                if required:
                    print(f"  {self.formatter.warning('* Required')}")
                
                # Get user input
                prompt = f"  Enter value: "
                try:
                    user_input = input(prompt).strip()
                except (KeyboardInterrupt, EOFError):
                    print("\n" + self.formatter.warning("Configuration cancelled"))
                    return None
                
                # Handle empty input
                if not user_input:
                    if default is not None:
                        configured_params[param_name] = str(default)
                        break
                    elif required:
                        print(f"  {self.formatter.error('This parameter is required')}")
                        continue
                    else:
                        configured_params[param_name] = ""
                        break
                
                # Validate input
                user_input = validate_input(user_input)
                
                if param_type == "choice" and choices and user_input not in choices:
                    choices_str = ', '.join(choices)
                    error_msg = f'Invalid choice. Must be one of: {choices_str}'
                    print(f"  {self.formatter.error(error_msg)}")
                    continue
                
                if param_type == "boolean":
                    if user_input.lower() in ['true', 'yes', '1', 'on']:
                        configured_params[param_name] = "true"
                    elif user_input.lower() in ['false', 'no', '0', 'off']:
                        configured_params[param_name] = "false"
                    else:
                        print(f"  {self.formatter.error('Boolean value required (true/false)')}")
                        continue
                else:
                    configured_params[param_name] = user_input
                
                break
            
            print()
        
        # Display summary
        print(self.formatter.header("📋 CONFIGURATION SUMMARY"))
        print_separator(60, "─")
        for param, value in configured_params.items():
            if value:
                print(f"{param.replace('_', ' ').title()}: {self.formatter.highlight(value)}")
        print()
        
        # Confirm launch
        confirm = input(f"{self.formatter.menu_description('Launch tool with these parameters? (y/N): ')}")
        if confirm.lower() in ['y', 'yes']:
            return configured_params
        else:
            print(self.formatter.warning("Tool launch cancelled"))
            return None
    
    def launch_tool_interactive(self, category_id: str, tool_selection: str) -> None:
        """Launch a tool interactively"""
        try:
            tool_number = int(tool_selection)
        except ValueError:
            print(self.formatter.error("Invalid tool selection"))
            return
        
        # Get tools in category
        categories = self.config.get_categories()
        if not categories or category_id not in categories:
            print(self.formatter.error(f"Category {category_id} not found"))
            return
        
        tools = list(categories[category_id].get("tools", {}).items())
        if tool_number < 1 or tool_number > len(tools):
            print(self.formatter.error("Invalid tool number"))
            return
        
        tool_name, tool_config = tools[tool_number - 1]
        command = tool_config.get("command", tool_name)
        
        # Check if tool is installed
        if not self.tool_manager.check_tool_installed(command):
            print(self.formatter.error(f"Tool '{tool_name}' is not installed"))
            install_cmd = self.tool_manager.suggest_installation_command(command)
            print(f"Install with: {self.formatter.info(install_cmd)}")
            return
        
        print(self.formatter.success(f"Tool '{tool_name}' found and ready to launch"))
        print()
        
        # Configure parameters
        parameters = self.configure_tool_parameters(tool_name, tool_config)
        if parameters is None:
            return
        
        # Launch tool
        print(self.formatter.status("Launching tool in new terminal..."))
        
        if self.terminal.launch_tool(tool_name, tool_config, parameters):
            print(self.formatter.success(f"Successfully launched {tool_name}"))
            # Brief pause to show success message
            time.sleep(1)
        else:
            print(self.formatter.error(f"Failed to launch {tool_name}"))
            print("Check terminal configuration and try again")
    
    def handle_main_menu_input(self, choice: str) -> bool:
        """Handle main menu input, return False to exit"""
        choice = choice.lower().strip()
        
        if choice == 'q':
            return False
        elif choice == 's':
            self.show_health_status()
        elif choice == 'h':
            self.show_help()
        elif choice.isdigit():
            category_id = choice
            categories = self.config.get_categories()
            if categories and category_id in categories:
                self.current_category = category_id
                self.show_category_submenu()
            else:
                print(self.formatter.error("Invalid category selection"))
                time.sleep(1)
        else:
            print(self.formatter.error("Invalid selection"))
            time.sleep(1)
        
        return True
    
    def show_category_submenu(self) -> None:
        """Show category submenu and handle tool selection"""
        while self.running and self.current_category:
            self.show_category_menu(self.current_category)
            
            try:
                choice = input(f"\n{self.formatter.menu_description('Select tool number or option: ')}")
                choice = choice.strip()
                
                if choice.lower() == 'b':
                    self.current_category = None
                    break
                elif choice.lower() == 'q':
                    self.running = False
                    break
                elif choice.lower() == 'r':
                    print(self.formatter.status("Refreshing tool status..."))
                    self.tool_manager.clear_cache()
                    time.sleep(1)
                elif choice.isdigit():
                    self.launch_tool_interactive(self.current_category, choice)
                    # Pause to show result
                    input(f"\n{self.formatter.menu_description('Press Enter to continue...')}")
                else:
                    print(self.formatter.error("Invalid selection"))
                    time.sleep(1)
                    
            except (KeyboardInterrupt, EOFError):
                print("\n" + self.formatter.warning("Returning to main menu..."))
                self.current_category = None
                break
    
    def show_help(self) -> None:
        """Show help information"""
        self.banner.print_small_banner()
        
        print(self.formatter.header("📚 M4SEC TOOLKIT HELP"))
        print_separator(80, "═")
        print()
        
        print(self.formatter.highlight("MAIN MENU OPTIONS:"))
        print(f"  {self.formatter.menu_number('1-12')} - Select tool category")
        print(f"  {self.formatter.menu_number('s')}    - System status and health check")
        print(f"  {self.formatter.menu_number('h')}    - Show this help")
        print(f"  {self.formatter.menu_number('q')}    - Quit the application")
        print()
        
        print(self.formatter.highlight("CATEGORY MENU OPTIONS:"))
        print(f"  {self.formatter.menu_number('1-N')} - Select and launch tool")
        print(f"  {self.formatter.menu_number('b')}   - Back to main menu")
        print(f"  {self.formatter.menu_number('r')}   - Refresh tool status")
        print(f"  {self.formatter.menu_number('q')}   - Quit the application")
        print()
        
        print(self.formatter.highlight("TOOL LAUNCH PROCESS:"))
        print("  1. Select a tool from the category menu")
        print("  2. Configure parameters (interactive prompts)")
        print("  3. Confirm configuration")
        print("  4. Tool launches in new terminal window")
        print()
        
        print(self.formatter.highlight("SYMBOLS:"))
        print(f"  ✅ - Tool is installed and ready")
        print(f"  ❌ - Tool is missing (installation required)")
        print(f"  ✓  - Success/OK status")
        print(f"  !  - Warning")
        print(f"  ✗  - Error")
        print(f"  i  - Information")
        print(f"  ●  - Status/Processing")
        print()
        
        print(self.formatter.highlight("VERSION INFORMATION:"))
        print(f"  Version: {self.formatter.info('3.0.0')}")
        print(f"  Build:   {self.formatter.info('20250801-182338')}")
        print(f"  Author:  {self.formatter.info('0x4ymn')}")
        print(f"  Team:    {self.formatter.info('m4sec.team')}")
        print(f"  UTC:     {self.formatter.info('2025-08-01 18:23:38')}")
        print()
        
        print_separator(80, "═")
        print(f"{self.formatter.menu_description('Press Enter to continue...')}")
        input()
    
    def run(self) -> None:
        """Main menu loop"""
        try:
            while self.running:
                self.show_main_menu()
                
                try:
                    choice = input(f"\n{self.formatter.menu_description('Select category or option: ')}")
                    if not self.handle_main_menu_input(choice):
                        break
                except (KeyboardInterrupt, EOFError):
                    print("\n" + self.formatter.warning("Exiting..."))
                    break
            
            # Show goodbye message
            self.banner.print_goodbye_banner()
            
        except Exception as e:
            logger.error(f"Menu system error: {e}")
            print(self.formatter.error("An error occurred. Check logs for details."))
            sys.exit(1)