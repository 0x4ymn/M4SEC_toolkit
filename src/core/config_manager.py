#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
JSON-based configuration file management

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
"""

import os
import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from core.utils import logger, FileManager


class ConfigManager:
    """Configuration manager for M4SEC Toolkit"""
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.tools_config_path = self.config_dir / "tools.json"
        self.settings_config_path = self.config_dir / "settings.json"
        
        # Ensure config directory exists
        FileManager.ensure_directory(str(self.config_dir))
        
        # Initialize default configurations
        self._initialize_configs()
    
    def _initialize_configs(self) -> None:
        """Initialize default configuration files if they don't exist"""
        if not self.tools_config_path.exists():
            self._create_default_tools_config()
        
        if not self.settings_config_path.exists():
            self._create_default_settings_config()
    
    def _create_default_tools_config(self) -> None:
        """Create default tools configuration"""
        default_tools = {
            "categories": {
                "1": {
                    "name": "Web Application Testing",
                    "description": "Tools for web application security testing",
                    "tools": {
                        "gobuster": {
                            "name": "gobuster",
                            "description": "Fast directory/file brute-forcer",
                            "command": "gobuster",
                            "parameters": {
                                "mode": {
                                    "type": "choice",
                                    "choices": ["dir", "dns", "vhost"],
                                    "default": "dir",
                                    "description": "Gobuster mode"
                                },
                                "target": {
                                    "type": "input",
                                    "required": True,
                                    "description": "Target URL/IP/Domain"
                                },
                                "wordlist": {
                                    "type": "input",
                                    "default": "/usr/share/wordlists/dirb/common.txt",
                                    "description": "Wordlist path"
                                },
                                "extensions": {
                                    "type": "input",
                                    "default": "php,html,txt",
                                    "description": "File extensions (comma-separated)"
                                },
                                "threads": {
                                    "type": "input",
                                    "default": "10",
                                    "description": "Number of threads"
                                }
                            },
                            "command_template": "gobuster {mode} -u {target} -w {wordlist} -x {extensions} -t {threads}",
                            "examples": [
                                "gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt",
                                "gobuster dns -d target.com -w /usr/share/wordlists/subdomains.txt"
                            ]
                        },
                        "sqlmap": {
                            "name": "sqlmap",
                            "description": "Automatic SQL injection testing tool",
                            "command": "sqlmap",
                            "parameters": {
                                "target": {
                                    "type": "input",
                                    "required": True,
                                    "description": "Target URL"
                                },
                                "data": {
                                    "type": "input",
                                    "description": "POST data (optional)"
                                },
                                "cookie": {
                                    "type": "input",
                                    "description": "HTTP Cookie header value"
                                },
                                "technique": {
                                    "type": "choice",
                                    "choices": ["B", "E", "U", "S", "T"],
                                    "description": "SQL injection techniques"
                                },
                                "batch": {
                                    "type": "boolean",
                                    "default": True,
                                    "description": "Never ask for user input, use default behavior"
                                }
                            },
                            "command_template": "sqlmap -u {target} {data_flag} {cookie_flag} {technique_flag} {batch_flag}",
                            "examples": [
                                "sqlmap -u 'http://target.com/vulnerable.php?id=1' --batch",
                                "sqlmap -u 'http://target.com/login.php' --data='username=admin&password=admin'"
                            ]
                        },
                        "nikto": {
                            "name": "nikto",
                            "description": "Web server vulnerability scanner",
                            "command": "nikto",
                            "parameters": {
                                "host": {
                                    "type": "input",
                                    "required": True,
                                    "description": "Target host"
                                },
                                "port": {
                                    "type": "input",
                                    "default": "80",
                                    "description": "Target port"
                                },
                                "ssl": {
                                    "type": "boolean",
                                    "default": False,
                                    "description": "Use SSL/HTTPS"
                                }
                            },
                            "command_template": "nikto -h {host} -p {port} {ssl_flag}",
                            "examples": [
                                "nikto -h target.com",
                                "nikto -h target.com -p 443 -ssl"
                            ]
                        }
                    }
                },
                "2": {
                    "name": "Network Reconnaissance & Scanning",
                    "description": "Network discovery and reconnaissance tools",
                    "tools": {
                        "nmap": {
                            "name": "nmap",
                            "description": "Network discovery and security auditing",
                            "command": "nmap",
                            "parameters": {
                                "target": {
                                    "type": "input",
                                    "required": True,
                                    "description": "Target IP/Network/Host"
                                },
                                "scan_type": {
                                    "type": "choice",
                                    "choices": ["-sS", "-sT", "-sU", "-sA", "-sV", "-sC"],
                                    "default": "-sS",
                                    "description": "Scan type"
                                },
                                "ports": {
                                    "type": "input",
                                    "default": "1-1000",
                                    "description": "Port range"
                                },
                                "timing": {
                                    "type": "choice",
                                    "choices": ["-T0", "-T1", "-T2", "-T3", "-T4", "-T5"],
                                    "default": "-T4",
                                    "description": "Timing template"
                                }
                            },
                            "command_template": "nmap {scan_type} -p {ports} {timing} {target}",
                            "examples": [
                                "nmap -sS -p 1-1000 target.com",
                                "nmap -sV -sC -p- target.com"
                            ]
                        },
                        "masscan": {
                            "name": "masscan",
                            "description": "Fast port scanner",
                            "command": "masscan",
                            "parameters": {
                                "target": {
                                    "type": "input",
                                    "required": True,
                                    "description": "Target IP/Network"
                                },
                                "ports": {
                                    "type": "input",
                                    "default": "1-1000",
                                    "description": "Port range"
                                },
                                "rate": {
                                    "type": "input",
                                    "default": "1000",
                                    "description": "Packets per second"
                                }
                            },
                            "command_template": "masscan {target} -p {ports} --rate {rate}",
                            "examples": [
                                "masscan 10.0.0.0/8 -p 80,443 --rate 1000"
                            ]
                        }
                    }
                },
                "3": {
                    "name": "Binary Analysis & Reverse Engineering",
                    "description": "Tools for binary analysis and reverse engineering",
                    "tools": {
                        "radare2": {
                            "name": "radare2",
                            "description": "Reverse engineering framework",
                            "command": "r2",
                            "parameters": {
                                "file": {
                                    "type": "input",
                                    "required": True,
                                    "description": "Binary file to analyze"
                                },
                                "analyze": {
                                    "type": "boolean",
                                    "default": True,
                                    "description": "Perform automatic analysis"
                                }
                            },
                            "command_template": "r2 {analyze_flag} {file}",
                            "examples": [
                                "r2 -A binary_file",
                                "r2 -c 'aaa; pdf' binary_file"
                            ]
                        },
                        "strings": {
                            "name": "strings",
                            "description": "Extract printable strings from files",
                            "command": "strings",
                            "parameters": {
                                "file": {
                                    "type": "input",
                                    "required": True,
                                    "description": "File to analyze"
                                },
                                "min_length": {
                                    "type": "input",
                                    "default": "4",
                                    "description": "Minimum string length"
                                }
                            },
                            "command_template": "strings -n {min_length} {file}",
                            "examples": [
                                "strings binary_file",
                                "strings -n 8 binary_file"
                            ]
                        }
                    }
                },
                "4": {
                    "name": "Forensics & Steganography",
                    "description": "Digital forensics and steganography tools",
                    "tools": {
                        "binwalk": {
                            "name": "binwalk",
                            "description": "Firmware analysis tool",
                            "command": "binwalk",
                            "parameters": {
                                "file": {
                                    "type": "input",
                                    "required": True,
                                    "description": "File to analyze"
                                },
                                "extract": {
                                    "type": "boolean",
                                    "default": False,
                                    "description": "Extract found files"
                                }
                            },
                            "command_template": "binwalk {extract_flag} {file}",
                            "examples": [
                                "binwalk firmware.bin",
                                "binwalk -e firmware.bin"
                            ]
                        },
                        "exiftool": {
                            "name": "exiftool",
                            "description": "Metadata reader/writer",
                            "command": "exiftool",
                            "parameters": {
                                "file": {
                                    "type": "input",
                                    "required": True,
                                    "description": "File to analyze"
                                }
                            },
                            "command_template": "exiftool {file}",
                            "examples": [
                                "exiftool image.jpg",
                                "exiftool -all= clean_image.jpg"
                            ]
                        }
                    }
                },
                "5": {
                    "name": "Cryptography & Password Cracking",
                    "description": "Cryptography and password cracking tools",
                    "tools": {
                        "john": {
                            "name": "john",
                            "description": "John the Ripper password cracker",
                            "command": "john",
                            "parameters": {
                                "hashfile": {
                                    "type": "input",
                                    "required": True,
                                    "description": "Hash file to crack"
                                },
                                "wordlist": {
                                    "type": "input",
                                    "default": "/usr/share/wordlists/rockyou.txt",
                                    "description": "Wordlist path"
                                },
                                "format": {
                                    "type": "input",
                                    "description": "Hash format (optional)"
                                }
                            },
                            "command_template": "john {format_flag} --wordlist={wordlist} {hashfile}",
                            "examples": [
                                "john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt",
                                "john --format=md5 hashes.txt"
                            ]
                        },
                        "hashcat": {
                            "name": "hashcat",
                            "description": "Advanced password recovery",
                            "command": "hashcat",
                            "parameters": {
                                "attack_mode": {
                                    "type": "choice",
                                    "choices": ["0", "1", "3"],
                                    "default": "0",
                                    "description": "Attack mode (0=dict, 1=combinator, 3=mask)"
                                },
                                "hash_type": {
                                    "type": "input",
                                    "default": "0",
                                    "description": "Hash type (0=MD5, 1000=NTLM, etc.)"
                                },
                                "hashfile": {
                                    "type": "input",
                                    "required": True,
                                    "description": "Hash file"
                                },
                                "wordlist": {
                                    "type": "input",
                                    "default": "/usr/share/wordlists/rockyou.txt",
                                    "description": "Wordlist path"
                                }
                            },
                            "command_template": "hashcat -m {hash_type} -a {attack_mode} {hashfile} {wordlist}",
                            "examples": [
                                "hashcat -m 0 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt",
                                "hashcat -m 1000 -a 0 ntlm_hashes.txt wordlist.txt"
                            ]
                        }
                    }
                }
            }
        }
        
        # Add more categories for remaining tools...
        for i in range(6, 13):
            default_tools["categories"][str(i)] = {
                "name": f"Category {i}",
                "description": f"Security tools category {i}",
                "tools": {}
            }
        
        FileManager.write_json_file(str(self.tools_config_path), default_tools)
        logger.info("Created default tools configuration")
    
    def _create_default_settings_config(self) -> None:
        """Create default settings configuration"""
        default_settings = {
            "application": {
                "name": "M4SEC Ultimate CTF & Security Toolkit Manager",
                "version": "3.0.0",
                "build": "20250801-182338",
                "author": "0x4ymn",
                "team": "m4sec.team",
                "utc": "2025-08-01 18:23:38",
                "user": "0x4ymn"
            },
            "ui": {
                "show_banner": True,
                "use_colors": True,
                "menu_timeout": 300,
                "clear_screen": True
            },
            "terminal": {
                "preferred_terminal": "auto",
                "keep_open": True,
                "working_directory": "~"
            },
            "logging": {
                "enabled": True,
                "level": "INFO",
                "file_rotation": True,
                "max_log_files": 10
            },
            "security": {
                "allow_root": False,
                "sanitize_input": True,
                "timeout_commands": 300
            },
            "paths": {
                "wordlists_dir": "/usr/share/wordlists",
                "tools_dir": "/usr/bin",
                "temp_dir": "/tmp",
                "output_dir": "~/m4sec_output"
            }
        }
        
        FileManager.write_json_file(str(self.settings_config_path), default_settings)
        logger.info("Created default settings configuration")
    
    def get_tools_config(self) -> Optional[Dict[str, Any]]:
        """Get tools configuration"""
        return FileManager.read_json_file(str(self.tools_config_path))
    
    def get_settings_config(self) -> Optional[Dict[str, Any]]:
        """Get settings configuration"""
        return FileManager.read_json_file(str(self.settings_config_path))
    
    def get_tool_config(self, category: str, tool_name: str) -> Optional[Dict[str, Any]]:
        """Get specific tool configuration"""
        tools_config = self.get_tools_config()
        if not tools_config:
            return None
        
        try:
            return tools_config["categories"][category]["tools"][tool_name]
        except KeyError:
            logger.error(f"Tool {tool_name} not found in category {category}")
            return None
    
    def get_categories(self) -> Optional[Dict[str, Any]]:
        """Get all tool categories"""
        tools_config = self.get_tools_config()
        if not tools_config:
            return None
        
        return tools_config.get("categories", {})
    
    def get_category_tools(self, category: str) -> Optional[Dict[str, Any]]:
        """Get tools for a specific category"""
        categories = self.get_categories()
        if not categories:
            return None
        
        try:
            return categories[category]["tools"]
        except KeyError:
            logger.error(f"Category {category} not found")
            return None
    
    def update_setting(self, section: str, key: str, value: Any) -> bool:
        """Update a specific setting"""
        settings = self.get_settings_config()
        if not settings:
            return False
        
        try:
            if section not in settings:
                settings[section] = {}
            settings[section][key] = value
            return FileManager.write_json_file(str(self.settings_config_path), settings)
        except Exception as e:
            logger.error(f"Error updating setting {section}.{key}: {e}")
            return False
    
    def get_setting(self, section: str, key: str, default: Any = None) -> Any:
        """Get a specific setting value"""
        settings = self.get_settings_config()
        if not settings:
            return default
        
        try:
            return settings.get(section, {}).get(key, default)
        except Exception:
            return default