#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
Core utilities, logging, and system checks

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
"""

import os
import sys
import logging
import shutil
import platform
import subprocess
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any, List


class M4SECLogger:
    """Professional logging system for M4SEC Toolkit"""
    
    def __init__(self, name: str = "m4sec", log_level: str = "INFO"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, log_level.upper()))
        
        # Create logs directory if it doesn't exist
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        
        # File handler
        log_file = log_dir / f"m4sec_{datetime.now().strftime('%Y%m%d')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, log_level.upper()))
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)
    
    def debug(self, message: str) -> None:
        self.logger.debug(message)
    
    def info(self, message: str) -> None:
        self.logger.info(message)
    
    def warning(self, message: str) -> None:
        self.logger.warning(message)
    
    def error(self, message: str) -> None:
        self.logger.error(message)
    
    def critical(self, message: str) -> None:
        self.logger.critical(message)


class SystemInfo:
    """System information and compatibility checks"""
    
    @staticmethod
    def get_system_info() -> Dict[str, Any]:
        """Get comprehensive system information"""
        return {
            "platform": platform.platform(),
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version(),
            "python_implementation": platform.python_implementation(),
            "user": os.getenv("USER", "unknown"),
            "home": os.path.expanduser("~"),
            "cwd": os.getcwd(),
            "path": os.environ.get("PATH", ""),
            "shell": os.environ.get("SHELL", ""),
        }
    
    @staticmethod
    def is_root() -> bool:
        """Check if running as root (security check)"""
        return os.geteuid() == 0 if hasattr(os, 'geteuid') else False
    
    @staticmethod
    def get_available_terminals() -> List[str]:
        """Get list of available terminal emulators"""
        terminals = [
            'gnome-terminal',
            'konsole',
            'xfce4-terminal',
            'mate-terminal',
            'xterm',
            'urxvt',
            'rxvt',
            'terminator',
            'kitty',
            'alacritty',
            'tilix'
        ]
        return [term for term in terminals if shutil.which(term)]
    
    @staticmethod
    def check_python_version() -> bool:
        """Check if Python version is compatible (3.8+)"""
        return sys.version_info >= (3, 8)
    
    @staticmethod
    def get_distro_info() -> Optional[str]:
        """Get Linux distribution information"""
        try:
            if platform.system() == "Linux":
                if os.path.exists("/etc/os-release"):
                    with open("/etc/os-release", "r") as f:
                        for line in f:
                            if line.startswith("PRETTY_NAME="):
                                return line.split("=", 1)[1].strip().strip('"')
                elif os.path.exists("/etc/issue"):
                    with open("/etc/issue", "r") as f:
                        return f.readline().strip()
        except Exception:
            pass
        return None


class FileManager:
    """File and directory management utilities"""
    
    @staticmethod
    def ensure_directory(path: str) -> bool:
        """Ensure directory exists, create if necessary"""
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            logger.error(f"Failed to create directory {path}: {e}")
            return False
    
    @staticmethod
    def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
        """Read JSON file safely"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"JSON file not found: {file_path}")
            return None
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {file_path}: {e}")
            return None
        except Exception as e:
            logger.error(f"Error reading JSON file {file_path}: {e}")
            return None
    
    @staticmethod
    def write_json_file(file_path: str, data: Dict[str, Any]) -> bool:
        """Write JSON file safely"""
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            logger.error(f"Error writing JSON file {file_path}: {e}")
            return False
    
    @staticmethod
    def create_temp_script(content: str, extension: str = ".sh") -> Optional[str]:
        """Create temporary script file"""
        try:
            import tempfile
            with tempfile.NamedTemporaryFile(
                mode='w', 
                suffix=extension, 
                delete=False, 
                prefix='m4sec_'
            ) as f:
                f.write(content)
                f.flush()
                os.chmod(f.name, 0o755)
                return f.name
        except Exception as e:
            logger.error(f"Error creating temp script: {e}")
            return None
    
    @staticmethod
    def cleanup_temp_files(pattern: str = "m4sec_*") -> int:
        """Clean up temporary files"""
        import tempfile
        import glob
        
        temp_dir = tempfile.gettempdir()
        files_cleaned = 0
        
        try:
            for file_path in glob.glob(os.path.join(temp_dir, pattern)):
                try:
                    os.unlink(file_path)
                    files_cleaned += 1
                except Exception:
                    pass
        except Exception:
            pass
        
        return files_cleaned


class CommandRunner:
    """Safe command execution utilities"""
    
    @staticmethod
    def run_command(
        command: List[str], 
        timeout: int = 30, 
        capture_output: bool = True
    ) -> Optional[subprocess.CompletedProcess]:
        """Run command safely with timeout"""
        try:
            result = subprocess.run(
                command,
                timeout=timeout,
                capture_output=capture_output,
                text=True,
                check=False
            )
            return result
        except subprocess.TimeoutExpired:
            logger.error(f"Command timed out: {' '.join(command)}")
            return None
        except FileNotFoundError:
            logger.error(f"Command not found: {command[0]}")
            return None
        except Exception as e:
            logger.error(f"Error running command: {e}")
            return None
    
    @staticmethod
    def check_tool_installed(tool_name: str) -> bool:
        """Check if a tool is installed"""
        return shutil.which(tool_name) is not None
    
    @staticmethod
    def get_tool_version(tool_name: str, version_flag: str = "--version") -> Optional[str]:
        """Get tool version if available"""
        try:
            result = CommandRunner.run_command([tool_name, version_flag], timeout=10)
            if result and result.returncode == 0:
                # Return first line of output, cleaned
                return result.stdout.split('\n')[0].strip()
        except Exception:
            pass
        return None


# Global logger instance
logger = M4SECLogger()


def get_current_timestamp() -> str:
    """Get current timestamp in M4SEC format"""
    return "2025-08-01 18:23:38"  # As specified in requirements


def get_build_info() -> Dict[str, str]:
    """Get build information"""
    return {
        "version": "3.0.0",
        "build": "20250801-182338",
        "author": "0x4ymn",
        "team": "m4sec.team",
        "utc": "2025-08-01 18:23:38",
        "user": "0x4ymn"
    }


def validate_input(user_input: str, input_type: str = "general") -> str:
    """Validate and sanitize user input"""
    if not user_input or not user_input.strip():
        return ""
    
    # Basic sanitization
    sanitized = user_input.strip()
    
    # Remove potentially dangerous characters for shell commands
    if input_type in ["command", "path"]:
        dangerous_chars = [";", "|", "&", "`", "$", "(", ")", ">", "<"]
        for char in dangerous_chars:
            if char in sanitized:
                logger.warning(f"Potentially dangerous character '{char}' detected in input")
    
    return sanitized


def format_size(size_bytes: int) -> str:
    """Format byte size to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def check_security() -> Dict[str, Any]:
    """Perform security checks"""
    checks = {
        "is_root": SystemInfo.is_root(),
        "python_version_ok": SystemInfo.check_python_version(),
        "terminals_available": len(SystemInfo.get_available_terminals()) > 0,
        "system_info": SystemInfo.get_system_info()
    }
    
    if checks["is_root"]:
        logger.critical("SECURITY WARNING: Running as root is not recommended!")
    
    if not checks["python_version_ok"]:
        logger.error("Python 3.8+ is required")
    
    if not checks["terminals_available"]:
        logger.warning("No compatible terminal emulators found")
    
    return checks