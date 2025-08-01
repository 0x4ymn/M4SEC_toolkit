# Contributing to M4SEC Ultimate CTF & Security Toolkit Manager

[![Version](https://img.shields.io/badge/version-3.0.0-blue.svg)](https://github.com/0x4ymn/M4SEC_toolkit)
[![Team](https://img.shields.io/badge/team-m4sec.team-red.svg)](https://m4sec.team)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Thank you for your interest in contributing to M4SEC Toolkit! This document provides comprehensive guidelines for contributing to our professional security toolkit manager.

## 🎯 Vision & Mission

**Mission**: To provide cybersecurity professionals and CTF participants with a comprehensive, user-friendly, and professional toolkit manager that streamlines security testing workflows.

**Vision**: To become the standard toolkit manager for security professionals worldwide, supporting ethical hacking, penetration testing, and cybersecurity education.

## 🤝 Ways to Contribute

### 1. Code Contributions
- **New Features**: Implement new functionality
- **Bug Fixes**: Resolve existing issues
- **Performance**: Optimize existing code
- **Documentation**: Improve code documentation

### 2. Tool Integration
- **New Tools**: Add support for additional security tools
- **Tool Configs**: Improve existing tool configurations
- **Categories**: Suggest new tool categories
- **Examples**: Provide usage examples

### 3. Documentation
- **User Guides**: Improve user documentation
- **Installation**: Enhance installation instructions
- **Tutorials**: Create learning materials
- **API Docs**: Document code APIs

### 4. Testing & Quality Assurance
- **Bug Reports**: Identify and report issues
- **Testing**: Test on different platforms
- **Validation**: Verify tool configurations
- **Security Review**: Review security implications

### 5. Community Support
- **Help Users**: Answer questions and provide support
- **Tutorials**: Create video or written tutorials
- **Translations**: Translate documentation
- **Advocacy**: Promote the project

## 🚀 Getting Started

### Development Environment Setup

1. **Fork the Repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/M4SEC_toolkit.git
   cd M4SEC_toolkit
   ```

2. **Set Up Development Environment**
   ```bash
   # Install dependencies
   pip3 install -r requirements.txt
   
   # Install development dependencies
   pip3 install pytest black flake8 mypy
   
   # Set up pre-commit hooks (optional)
   pip3 install pre-commit
   pre-commit install
   ```

3. **Create a Branch**
   ```bash
   # Create a feature branch
   git checkout -b feature/your-feature-name
   
   # Or a bug fix branch
   git checkout -b fix/bug-description
   ```

4. **Test Your Setup**
   ```bash
   # Run basic tests
   python3 src/main.py --version
   python3 src/main.py --health
   
   # Run unit tests (when available)
   pytest tests/
   ```

### Development Workflow

1. **Create an Issue** (for significant changes)
2. **Fork & Clone** the repository
3. **Create a Branch** for your changes
4. **Make Changes** following our guidelines
5. **Test Thoroughly** on multiple platforms
6. **Submit a Pull Request** with detailed description
7. **Respond to Feedback** and iterate as needed

## 📁 Project Structure

```
M4SEC_toolkit/
├── src/                    # Main source code
│   ├── core/              # Core functionality
│   │   ├── config_manager.py
│   │   ├── tool_manager.py
│   │   ├── terminal_launcher.py
│   │   └── utils.py
│   ├── ui/                # User interface
│   │   ├── colors.py
│   │   ├── banner.py
│   │   └── menu.py
│   └── main.py            # Entry point
├── config/                # Configuration files
│   ├── tools.json         # Tool definitions
│   └── settings.json      # Application settings
├── scripts/               # Installation scripts
│   ├── install.sh
│   └── uninstall.sh
├── docs/                  # Documentation
│   ├── INSTALLATION.md
│   ├── USER_GUIDE.md
│   └── CONTRIBUTING.md
├── tests/                 # Test files (future)
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup
└── README.md             # Project README
```

## 💻 Coding Standards

### Python Code Style

We follow PEP 8 with some modifications:

```python
# Good: Clear, descriptive names
def launch_security_tool(tool_name: str, parameters: Dict[str, str]) -> bool:
    """Launch a security tool with given parameters."""
    pass

# Good: Type hints for better maintainability
class ToolManager:
    def __init__(self, config: ConfigManager) -> None:
        self.config = config
        self.tools: Dict[str, Any] = {}

# Good: Comprehensive docstrings
def validate_tool_parameters(
    tool_config: Dict[str, Any], 
    user_params: Dict[str, str]
) -> Tuple[bool, List[str]]:
    """
    Validate user parameters against tool configuration.
    
    Args:
        tool_config: Tool configuration from tools.json
        user_params: User-provided parameters
        
    Returns:
        Tuple of (is_valid, error_messages)
        
    Raises:
        ConfigError: If tool configuration is invalid
    """
    pass
```

### Code Formatting

Use these tools to maintain consistent formatting:

```bash
# Format code with black
black src/

# Check style with flake8
flake8 src/

# Type checking with mypy
mypy src/
```

### Error Handling

Always implement comprehensive error handling:

```python
# Good: Specific exception handling
try:
    tool_config = self.config.get_tool_config(category, tool_name)
    if not tool_config:
        raise ToolNotFoundError(f"Tool {tool_name} not found")
except ToolNotFoundError as e:
    logger.error(f"Tool configuration error: {e}")
    return False
except Exception as e:
    logger.error(f"Unexpected error loading tool: {e}")
    return False
```

### Logging

Use the centralized logging system:

```python
from core.utils import logger

# Different log levels
logger.debug("Detailed debug information")
logger.info("General information")
logger.warning("Warning message")
logger.error("Error occurred")
logger.critical("Critical system error")
```

## 🛠️ Adding New Tools

### 1. Tool Configuration

Add tool definition to `config/tools.json`:

```json
{
  "new_tool": {
    "name": "new_tool",
    "description": "Brief description of the tool",
    "command": "actual_command_name",
    "parameters": {
      "target": {
        "type": "input",
        "required": true,
        "description": "Target host or IP"
      },
      "port": {
        "type": "input",
        "default": "80",
        "description": "Target port"
      },
      "verbose": {
        "type": "boolean",
        "default": false,
        "description": "Enable verbose output"
      },
      "method": {
        "type": "choice",
        "choices": ["GET", "POST", "PUT"],
        "default": "GET",
        "description": "HTTP method"
      }
    },
    "command_template": "new_tool -t {target} -p {port} {verbose_flag} --method {method}",
    "examples": [
      "new_tool -t example.com -p 80",
      "new_tool -t 192.168.1.1 -p 443 --verbose"
    ]
  }
}
```

### 2. Parameter Types

Supported parameter types:

- **input**: Free text input
- **boolean**: True/false flags
- **choice**: Multiple choice selection
- **file**: File path input

### 3. Command Template Variables

- `{parameter_name}`: Direct parameter substitution
- `{parameter_name_flag}`: For flags (boolean parameters)
- Special handling for different parameter types

### 4. Testing New Tools

```bash
# Test tool detection
python3 src/main.py --health

# Test tool configuration
python3 src/main.py --tool new_tool

# Test in interactive mode
python3 src/main.py
```

## 🧪 Testing Guidelines

### Manual Testing

1. **Cross-Platform Testing**
   - Test on Ubuntu, Debian, CentOS, Arch Linux
   - Test with different terminal emulators
   - Test with different Python versions (3.8+)

2. **Feature Testing**
   - Test all menu navigation
   - Test parameter configuration
   - Test tool launching
   - Test error handling

3. **Security Testing**
   - Test input validation
   - Test command injection prevention
   - Test file path validation

### Automated Testing (Future)

```bash
# Unit tests
pytest tests/unit/

# Integration tests
pytest tests/integration/

# System tests
pytest tests/system/
```

## 📝 Documentation Standards

### Code Documentation

```python
class ToolManager:
    """
    Manages security tool detection, verification, and execution.
    
    This class provides comprehensive tool management functionality including:
    - Tool installation detection
    - Version information retrieval
    - Tool configuration validation
    - Execution environment setup
    
    Attributes:
        config: Configuration manager instance
        tool_cache: Cache of tool status information
        
    Example:
        >>> config = ConfigManager()
        >>> tool_mgr = ToolManager(config)
        >>> is_installed = tool_mgr.check_tool_installed("nmap")
    """
    
    def check_tool_installed(self, tool_name: str) -> bool:
        """
        Check if a security tool is installed and available.
        
        Args:
            tool_name: Name of the tool to check
            
        Returns:
            True if tool is installed and accessible, False otherwise
            
        Raises:
            ToolError: If tool checking fails
            
        Example:
            >>> tool_mgr.check_tool_installed("nmap")
            True
        """
        pass
```

### User Documentation

- Use clear, concise language
- Provide practical examples
- Include screenshots where helpful
- Structure with headers and sections
- Use consistent formatting

## 🔄 Pull Request Process

### Before Submitting

1. **Test Thoroughly**
   - Test on multiple platforms
   - Test all affected functionality
   - Verify no regressions

2. **Update Documentation**
   - Update relevant documentation
   - Add examples if needed
   - Update changelog (future)

3. **Code Quality**
   - Run formatting tools
   - Fix any linting issues
   - Add type hints

### Pull Request Template

```markdown
## Description
Brief description of changes made.

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tested on Ubuntu 20.04
- [ ] Tested on other distributions
- [ ] All menu functions work
- [ ] Tool launching works
- [ ] No regressions found

## Screenshots (if applicable)
Add screenshots of UI changes.

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No console errors
```

### Review Process

1. **Automated Checks** (future)
   - Code formatting
   - Linting
   - Basic functionality tests

2. **Manual Review**
   - Code quality assessment
   - Security review
   - Functionality verification
   - Documentation review

3. **Testing**
   - Cross-platform testing
   - Integration testing
   - User experience testing

## 🐛 Bug Reports

### Bug Report Template

```markdown
**Bug Description**
Clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. Select option '...'
3. Enter parameter '...'
4. See error

**Expected Behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Ubuntu 20.04]
- Python Version: [e.g., 3.9.2]
- Terminal: [e.g., gnome-terminal]
- M4SEC Version: [e.g., 3.0.0]

**Additional Context**
Any other context about the problem.

**Logs**
Paste relevant log entries from logs/m4sec_*.log
```

### Security Vulnerabilities

For security issues:
1. **Do NOT** create public issues
2. **Email directly**: security@m4sec.team
3. **Include details**: How to reproduce, impact assessment
4. **Wait for response** before public disclosure

## 🌟 Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the proposed feature.

**Use Case**
Describe the problem this feature would solve.

**Proposed Solution**
Describe how you envision this working.

**Alternatives Considered**
Other solutions you've considered.

**Additional Context**
Any other context, screenshots, or examples.

**Implementation Ideas**
If you have technical implementation ideas.
```

## 🏆 Recognition

### Contributors

We recognize contributors in several ways:

1. **GitHub Contributors**: Listed automatically
2. **Documentation**: Contributors mentioned in docs
3. **Releases**: Contributors credited in release notes
4. **Hall of Fame**: Top contributors featured on website

### Levels of Contribution

- **Bronze**: Bug reports, documentation improvements
- **Silver**: Code contributions, new features
- **Gold**: Significant features, architectural improvements
- **Platinum**: Long-term contributors, core team members

## 📞 Communication

### Official Channels

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: General questions and ideas
- **Email**: admin@m4sec.team for direct contact
- **Discord**: Coming soon for real-time chat

### Code of Conduct

We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/):

- **Be respectful** and inclusive
- **Be collaborative** and constructive
- **Be patient** with newcomers
- **Focus on the project** goals

## 🎓 Learning Resources

### For New Contributors

- **Git/GitHub**: [GitHub Skills](https://skills.github.com/)
- **Python**: [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- **Security Tools**: [Kali Linux Documentation](https://www.kali.org/docs/)

### For the Project

- **Architecture**: Study the code structure
- **Tools**: Learn about security tools we support
- **CTF**: Practice with Capture The Flag challenges

## 📋 Roadmap

### Short-term Goals (v3.1)
- [ ] Unit test framework
- [ ] CI/CD pipeline
- [ ] Docker support
- [ ] More tool integrations

### Medium-term Goals (v3.5)
- [ ] Web interface
- [ ] Plugin system
- [ ] Cloud tool support
- [ ] Mobile app testing tools

### Long-term Goals (v4.0)
- [ ] Team collaboration features
- [ ] Reporting system
- [ ] Integration with security platforms
- [ ] AI-powered recommendations

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License. See [LICENSE](LICENSE) file for details.

---

**Thank you for contributing to M4SEC Toolkit!**

Your contributions make the cybersecurity community stronger and more capable. Together, we're building the future of security testing tools.

*Version: 3.0.0 | Build: 20250801-182338 | Team: m4sec.team*

🔐 **Happy Contributing!**