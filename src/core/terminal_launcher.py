#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
Terminal integration for launching tools in new windows

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
"""

import os
import shutil
import subprocess
import tempfile
from typing import Dict, List, Optional, Any
from .utils import logger, FileManager, SystemInfo, validate_input
from .config_manager import ConfigManager


class TerminalLauncher:
    """Handles launching tools in new terminal windows"""
    
    def __init__(self, config_manager: ConfigManager):
        self.config = config_manager
        self.available_terminals = SystemInfo.get_available_terminals()
        self.preferred_terminal = self._get_preferred_terminal()
    
    def _get_preferred_terminal(self) -> Optional[str]:
        """Get preferred terminal emulator"""
        # Check user preference
        preferred = self.config.get_setting("terminal", "preferred_terminal", "auto")
        
        if preferred != "auto" and shutil.which(preferred):
            return preferred
        
        # Auto-detect best available terminal
        terminal_priority = [
            'gnome-terminal',
            'konsole',
            'xfce4-terminal',
            'mate-terminal',
            'terminator',
            'kitty',
            'alacritty',
            'tilix',
            'xterm',
            'urxvt',
            'rxvt'
        ]
        
        for terminal in terminal_priority:
            if terminal in self.available_terminals:
                return terminal
        
        return self.available_terminals[0] if self.available_terminals else None
    
    def _build_terminal_command(self, terminal: str, script_path: str, title: str) -> List[str]:
        """Build terminal launch command for specific terminal emulator"""
        commands = {
            'gnome-terminal': [
                'gnome-terminal',
                '--title', title,
                '--',
                'bash', script_path
            ],
            'konsole': [
                'konsole',
                '--title', title,
                '-e', 'bash', script_path
            ],
            'xfce4-terminal': [
                'xfce4-terminal',
                '--title', title,
                '--command', f'bash {script_path}'
            ],
            'mate-terminal': [
                'mate-terminal',
                '--title', title,
                '--command', f'bash {script_path}'
            ],
            'terminator': [
                'terminator',
                '--title', title,
                '-x', 'bash', script_path
            ],
            'kitty': [
                'kitty',
                '--title', title,
                'bash', script_path
            ],
            'alacritty': [
                'alacritty',
                '--title', title,
                '-e', 'bash', script_path
            ],
            'tilix': [
                'tilix',
                '--title', title,
                '-e', 'bash', script_path
            ],
            'xterm': [
                'xterm',
                '-title', title,
                '-e', 'bash', script_path
            ],
            'urxvt': [
                'urxvt',
                '-title', title,
                '-e', 'bash', script_path
            ],
            'rxvt': [
                'rxvt',
                '-title', title,
                '-e', 'bash', script_path
            ]
        }
        
        return commands.get(terminal, ['xterm', '-e', 'bash', script_path])
    
    def _create_launch_script(
        self, 
        tool_command: str, 
        tool_name: str, 
        working_dir: str = None
    ) -> Optional[str]:
        """Create a bash script to launch the tool"""
        working_dir = working_dir or os.path.expanduser("~")
        
        script_content = f"""#!/bin/bash
# M4SEC Toolkit - Tool Launch Script
# Tool: {tool_name}
# Generated: {self.config.get_setting('application', 'utc', 'Unknown')}

echo "████████████████████████████████████████████████████████████████████████████████"
echo "█  M4SEC Ultimate CTF & Security Toolkit Manager                              █"
echo "█  Launching: {tool_name:<60} █"
echo "█  Command: {tool_command[:62]:<62} █"
echo "████████████████████████████████████████████████████████████████████████████████"
echo ""

# Change to working directory
cd "{working_dir}" || echo "Warning: Could not change to working directory"

# Display current directory
echo "Working directory: $(pwd)"
echo "Command: {tool_command}"
echo ""

# Launch the tool
echo "Starting {tool_name}..."
echo "----------------------------------------"
{tool_command}

# Keep terminal open
exit_code=$?
echo ""
echo "----------------------------------------"
echo "{tool_name} finished with exit code: $exit_code"
echo "Press Enter to close this window..."
read -r
"""
        
        return FileManager.create_temp_script(script_content, ".sh")
    
    def build_tool_command(
        self, 
        tool_config: Dict[str, Any], 
        parameters: Dict[str, str]
    ) -> Optional[str]:
        """Build the complete tool command with parameters"""
        try:
            command_template = tool_config.get("command_template", "")
            if not command_template:
                logger.error("No command template found for tool")
                return None
            
            # Start with the template
            command = command_template
            
            # Replace parameters in template
            for param_name, param_value in parameters.items():
                if param_value:
                    # Handle boolean parameters (flags)
                    if param_value.lower() in ['true', 'yes', '1']:
                        # For boolean true, replace with flag or empty string
                        flag_name = f"{param_name}_flag"
                        if f"{{{flag_name}}}" in command:
                            command = command.replace(f"{{{flag_name}}}", f"--{param_name.replace('_', '-')}")
                        else:
                            command = command.replace(f"{{{param_name}}}", f"--{param_name.replace('_', '-')}")
                    elif param_value.lower() in ['false', 'no', '0']:
                        # For boolean false, remove flag
                        flag_name = f"{param_name}_flag"
                        command = command.replace(f"{{{flag_name}}}", "")
                        command = command.replace(f"{{{param_name}}}", "")
                    else:
                        # Handle special flag formatting
                        flag_name = f"{param_name}_flag"
                        if f"{{{flag_name}}}" in command:
                            if param_name in ['data', 'cookie']:
                                command = command.replace(f"{{{flag_name}}}", f"--{param_name} '{param_value}'")
                            elif param_name == 'technique':
                                command = command.replace(f"{{{flag_name}}}", f"--technique {param_value}")
                            else:
                                command = command.replace(f"{{{flag_name}}}", f"--{param_name.replace('_', '-')} {param_value}")
                        else:
                            # Direct parameter replacement
                            command = command.replace(f"{{{param_name}}}", param_value)
                else:
                    # Remove empty parameters and their flags
                    flag_name = f"{param_name}_flag"
                    command = command.replace(f"{{{flag_name}}}", "")
                    command = command.replace(f"{{{param_name}}}", "")
            
            # Clean up extra spaces
            command = " ".join(command.split())
            
            return command
            
        except Exception as e:
            logger.error(f"Error building tool command: {e}")
            return None
    
    def launch_tool(
        self, 
        tool_name: str, 
        tool_config: Dict[str, Any], 
        parameters: Dict[str, str]
    ) -> bool:
        """Launch a tool in a new terminal window"""
        try:
            if not self.preferred_terminal:
                logger.error("No terminal emulator available")
                return False
            
            # Build the tool command
            tool_command = self.build_tool_command(tool_config, parameters)
            if not tool_command:
                logger.error("Failed to build tool command")
                return False
            
            # Validate command (basic security check)
            if not self._validate_command(tool_command):
                logger.error("Command failed security validation")
                return False
            
            # Create launch script
            script_path = self._create_launch_script(tool_command, tool_name)
            if not script_path:
                logger.error("Failed to create launch script")
                return False
            
            # Build terminal command
            terminal_title = f"M4SEC - {tool_name}"
            terminal_command = self._build_terminal_command(
                self.preferred_terminal, 
                script_path, 
                terminal_title
            )
            
            # Launch terminal
            logger.info(f"Launching {tool_name} in {self.preferred_terminal}")
            logger.debug(f"Terminal command: {' '.join(terminal_command)}")
            
            process = subprocess.Popen(
                terminal_command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )
            
            # Don't wait for the process to complete as it's in a new terminal
            logger.info(f"Successfully launched {tool_name} (PID: {process.pid})")
            return True
            
        except Exception as e:
            logger.error(f"Error launching tool {tool_name}: {e}")
            return False
    
    def _validate_command(self, command: str) -> bool:
        """Basic command validation for security"""
        # Check for potentially dangerous characters/patterns
        dangerous_patterns = [
            ';', '&&', '||', '|',  # Command chaining
            '$(', '`',  # Command substitution
            '>', '>>', '<',  # Redirection (might be legitimate for some tools)
            'rm -rf', 'dd if=', 'mkfs',  # Dangerous commands
            'sudo', 'su',  # Privilege escalation
        ]
        
        # Allow legitimate redirection for security tools
        safe_redirections = ['>', '>>', '2>', '2>&1']
        
        for pattern in dangerous_patterns:
            if pattern in command:
                # Allow some safe redirections
                if pattern in safe_redirections:
                    continue
                logger.warning(f"Potentially dangerous pattern '{pattern}' in command: {command}")
                # For now, just warn but don't block
                # In production, you might want to be more restrictive
        
        return True
    
    def get_terminal_info(self) -> Dict[str, Any]:
        """Get information about available terminals"""
        return {
            "preferred": self.preferred_terminal,
            "available": self.available_terminals,
            "count": len(self.available_terminals),
            "supported": [
                'gnome-terminal', 'konsole', 'xfce4-terminal', 
                'mate-terminal', 'terminator', 'kitty', 
                'alacritty', 'tilix', 'xterm', 'urxvt', 'rxvt'
            ]
        }
    
    def test_terminal(self, terminal_name: str = None) -> bool:
        """Test if terminal emulator works"""
        test_terminal = terminal_name or self.preferred_terminal
        
        if not test_terminal:
            return False
        
        try:
            # Create a simple test script
            test_script_content = """#!/bin/bash
echo "M4SEC Terminal Test - SUCCESS"
echo "Terminal: """ + test_terminal + """"
sleep 2
"""
            script_path = FileManager.create_temp_script(test_script_content, ".sh")
            if not script_path:
                return False
            
            # Try to launch terminal with test script
            terminal_command = self._build_terminal_command(
                test_terminal, 
                script_path, 
                "M4SEC Terminal Test"
            )
            
            process = subprocess.Popen(
                terminal_command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True
            )
            
            logger.info(f"Terminal test launched for {test_terminal}")
            return True
            
        except Exception as e:
            logger.error(f"Terminal test failed for {test_terminal}: {e}")
            return False
    
    def cleanup_temp_files(self) -> int:
        """Clean up temporary launch scripts"""
        return FileManager.cleanup_temp_files("m4sec_*.sh")