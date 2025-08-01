#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
Main package initialization

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
"""

__version__ = "3.0.0"
__build__ = "20250801-182338"
__author__ = "0x4ymn"
__team__ = "m4sec.team"
__utc__ = "2025-08-01 18:23:38"

from .core.config_manager import ConfigManager
from .core.tool_manager import ToolManager
from .core.terminal_launcher import TerminalLauncher
from .core.utils import logger, get_build_info, check_security
from .ui.menu import MenuSystem
from .ui.colors import ColorFormatter
from .ui.banner import BannerManager

__all__ = [
    'ConfigManager',
    'ToolManager', 
    'TerminalLauncher',
    'MenuSystem',
    'ColorFormatter',
    'BannerManager',
    'logger',
    'get_build_info',
    'check_security'
]