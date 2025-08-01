#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
Tool detection, installation, verification, and management

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
"""

import shutil
import subprocess
from typing import Dict, List, Optional, Tuple, Any
from .utils import logger, CommandRunner, SystemInfo
from .config_manager import ConfigManager


class ToolManager:
    """Manages security tools detection, verification, and status"""
    
    def __init__(self, config_manager: ConfigManager):
        self.config = config_manager
        self.tool_status_cache = {}
        
        # Special cases for tool detection
        self.special_tools = {
            "radare2": ["r2", "radare2"],
            "john": ["john", "john-the-ripper"],
            "ghidra": ["ghidra", "ghidraRun"],
            "volatility3": ["vol", "volatility3", "volatility"],
            "metasploit": ["msfconsole", "msfvenom"],
            "burpsuite": ["burpsuite", "burp"],
            "wireshark": ["wireshark", "tshark"],
            "sqlmap": ["sqlmap", "sqlmap.py"]
        }
    
    def check_tool_installed(self, tool_name: str) -> bool:
        """Check if a tool is installed"""
        # Check cache first
        if tool_name in self.tool_status_cache:
            return self.tool_status_cache[tool_name]
        
        # Check special cases
        if tool_name in self.special_tools:
            for variant in self.special_tools[tool_name]:
                if shutil.which(variant):
                    self.tool_status_cache[tool_name] = True
                    return True
        
        # Standard check
        is_installed = shutil.which(tool_name) is not None
        self.tool_status_cache[tool_name] = is_installed
        return is_installed
    
    def get_tool_version(self, tool_name: str) -> Optional[str]:
        """Get tool version information"""
        if not self.check_tool_installed(tool_name):
            return None
        
        version_commands = {
            "nmap": ["nmap", "--version"],
            "gobuster": ["gobuster", "version"],
            "sqlmap": ["sqlmap", "--version"],
            "nikto": ["nikto", "-Version"],
            "masscan": ["masscan", "--version"],
            "john": ["john", "--version"],
            "hashcat": ["hashcat", "--version"],
            "radare2": ["r2", "-version"],
            "binwalk": ["binwalk", "--help"],  # binwalk shows version in help
            "exiftool": ["exiftool", "-ver"],
            "strings": ["strings", "--version"],
            "ffuf": ["ffuf", "-V"],
            "dirb": ["dirb"],  # Shows version at startup
            "whatweb": ["whatweb", "--version"],
            "enum4linux": ["enum4linux"],  # Shows version in help
            "dnsrecon": ["dnsrecon", "--version"]
        }
        
        if tool_name in version_commands:
            try:
                result = CommandRunner.run_command(
                    version_commands[tool_name], 
                    timeout=10
                )
                if result and result.returncode == 0:
                    # Get first non-empty line
                    lines = result.stdout.strip().split('\n')
                    for line in lines:
                        if line.strip():
                            return line.strip()[:100]  # Limit length
                elif result and result.stderr:
                    # Some tools output version to stderr
                    lines = result.stderr.strip().split('\n')
                    for line in lines:
                        if line.strip():
                            return line.strip()[:100]
            except Exception as e:
                logger.debug(f"Error getting version for {tool_name}: {e}")
        
        return "Version unknown"
    
    def get_tool_path(self, tool_name: str) -> Optional[str]:
        """Get full path to tool executable"""
        # Check special cases first
        if tool_name in self.special_tools:
            for variant in self.special_tools[tool_name]:
                path = shutil.which(variant)
                if path:
                    return path
        
        return shutil.which(tool_name)
    
    def get_all_tools_status(self) -> Dict[str, Dict[str, Any]]:
        """Get status of all tools in all categories"""
        status = {}
        categories = self.config.get_categories()
        
        if not categories:
            return status
        
        for cat_id, category in categories.items():
            status[cat_id] = {
                "name": category.get("name", f"Category {cat_id}"),
                "description": category.get("description", ""),
                "tools": {}
            }
            
            tools = category.get("tools", {})
            for tool_name, tool_config in tools.items():
                command = tool_config.get("command", tool_name)
                is_installed = self.check_tool_installed(command)
                
                status[cat_id]["tools"][tool_name] = {
                    "name": tool_config.get("name", tool_name),
                    "description": tool_config.get("description", ""),
                    "command": command,
                    "installed": is_installed,
                    "version": self.get_tool_version(command) if is_installed else None,
                    "path": self.get_tool_path(command) if is_installed else None
                }
        
        return status
    
    def get_category_tools_status(self, category_id: str) -> Optional[Dict[str, Any]]:
        """Get status of tools in a specific category"""
        all_status = self.get_all_tools_status()
        return all_status.get(category_id)
    
    def get_installed_tools_count(self) -> Tuple[int, int]:
        """Get count of installed vs total tools"""
        all_status = self.get_all_tools_status()
        total_tools = 0
        installed_tools = 0
        
        for category in all_status.values():
            for tool_status in category["tools"].values():
                total_tools += 1
                if tool_status["installed"]:
                    installed_tools += 1
        
        return installed_tools, total_tools
    
    def get_missing_tools(self) -> List[Dict[str, str]]:
        """Get list of missing tools"""
        missing = []
        all_status = self.get_all_tools_status()
        
        for cat_id, category in all_status.items():
            for tool_name, tool_status in category["tools"].items():
                if not tool_status["installed"]:
                    missing.append({
                        "category": category["name"],
                        "category_id": cat_id,
                        "name": tool_name,
                        "description": tool_status["description"],
                        "command": tool_status["command"]
                    })
        
        return missing
    
    def suggest_installation_command(self, tool_name: str) -> Optional[str]:
        """Suggest installation command for a tool"""
        # Common installation commands for popular tools
        installation_commands = {
            "nmap": "sudo apt install nmap",
            "gobuster": "sudo apt install gobuster",
            "sqlmap": "sudo apt install sqlmap",
            "nikto": "sudo apt install nikto",
            "masscan": "sudo apt install masscan",
            "john": "sudo apt install john",
            "hashcat": "sudo apt install hashcat",
            "radare2": "sudo apt install radare2",
            "binwalk": "sudo apt install binwalk",
            "exiftool": "sudo apt install exiftool",
            "strings": "sudo apt install binutils",
            "ffuf": "go install github.com/ffuf/ffuf@latest",
            "dirb": "sudo apt install dirb",
            "whatweb": "sudo apt install whatweb",
            "enum4linux": "sudo apt install enum4linux",
            "dnsrecon": "sudo apt install dnsrecon",
            "rustscan": "cargo install rustscan",
            "gdb": "sudo apt install gdb",
            "ghidra": "Download from NSA GitHub",
            "steghide": "sudo apt install steghide",
            "foremost": "sudo apt install foremost",
            "volatility3": "pip3 install volatility3",
            "openssl": "sudo apt install openssl",
            "hydra": "sudo apt install hydra",
            "wpscan": "gem install wpscan",
            "amass": "sudo apt install amass",
            "subfinder": "go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest"
        }
        
        return installation_commands.get(tool_name, f"Search for '{tool_name}' installation instructions")
    
    def validate_tool_config(self, tool_name: str, category_id: str) -> bool:
        """Validate tool configuration"""
        tool_config = self.config.get_tool_config(category_id, tool_name)
        if not tool_config:
            return False
        
        required_fields = ["name", "description", "command", "parameters"]
        for field in required_fields:
            if field not in tool_config:
                logger.error(f"Tool {tool_name} missing required field: {field}")
                return False
        
        return True
    
    def get_system_health(self) -> Dict[str, Any]:
        """Get overall system health information"""
        installed_count, total_count = self.get_installed_tools_count()
        missing_tools = self.get_missing_tools()
        system_info = SystemInfo.get_system_info()
        available_terminals = SystemInfo.get_available_terminals()
        
        health = {
            "tools": {
                "total": total_count,
                "installed": installed_count,
                "missing": len(missing_tools),
                "percentage": (installed_count / total_count * 100) if total_count > 0 else 0
            },
            "system": {
                "platform": system_info.get("platform", "Unknown"),
                "python_version": system_info.get("python_version", "Unknown"),
                "is_root": SystemInfo.is_root(),
                "python_compatible": SystemInfo.check_python_version()
            },
            "terminals": {
                "available": available_terminals,
                "count": len(available_terminals),
                "has_terminal": len(available_terminals) > 0
            },
            "missing_tools": missing_tools[:10],  # Top 10 missing tools
            "status": "healthy" if installed_count > total_count * 0.5 else "needs_attention"
        }
        
        return health
    
    def clear_cache(self) -> None:
        """Clear tool status cache"""
        self.tool_status_cache.clear()
        logger.debug("Tool status cache cleared")
    
    def refresh_tool_status(self, tool_name: str = None) -> None:
        """Refresh tool status (clear cache for specific tool or all)"""
        if tool_name:
            self.tool_status_cache.pop(tool_name, None)
        else:
            self.clear_cache()
        logger.debug(f"Tool status refreshed for: {tool_name or 'all tools'}")