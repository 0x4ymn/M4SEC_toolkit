#!/usr/bin/env python3
"""
M4SEC Ultimate CTF & Security Toolkit Manager
Setup configuration for package installation

Version: 3.0.0
Build: 20250801-182338
Author: 0x4ymn
Team: m4sec.team
UTC: 2025-08-01 18:23:38
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "M4SEC Ultimate CTF & Security Toolkit Manager"

# Read requirements
def read_requirements():
    try:
        with open("requirements.txt", "r", encoding="utf-8") as fh:
            return [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        return []

setup(
    name="m4sec-toolkit",
    version="3.0.0",
    author="0x4ymn",
    author_email="admin@m4sec.team",
    description="Ultimate CTF & Security Toolkit Manager - Professional All-in-One Launcher",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/0x4ymn/M4SEC_toolkit",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.910",
        ],
    },
    entry_points={
        "console_scripts": [
            "m4sec=main:main",
            "m4sec-toolkit=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["config/*.json", "scripts/*.sh", "docs/*.md"],
    },
    keywords="security, ctf, penetration-testing, tools, hacking, cybersecurity",
    project_urls={
        "Bug Reports": "https://github.com/0x4ymn/M4SEC_toolkit/issues",
        "Source": "https://github.com/0x4ymn/M4SEC_toolkit",
        "Documentation": "https://github.com/0x4ymn/M4SEC_toolkit/blob/main/README.md",
        "Team": "https://m4sec.team",
    },
)