"""
AI configuration generators
"""
from pathlib import Path
from ..templates.base import ProjectTemplate

class AIConfigGenerator:
    """Generate AI assistant configuration files"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
    
    def create_cursor_rules(self, template: ProjectTemplate) -> None:
        """Create .cursorrules file with project-specific rules"""
        
        base_rules = """
# Cursor AI Rules for this project
# These rules help Cursor's AI understand the project context and coding style

## General Guidelines
- Use TypeScript for all JavaScript/React code
- Follow PEP 8 for Python code
- Write descriptive commit messages
- Include docstrings for all functions
- Use meaningful variable names

## Code Style
- Use 4 spaces for Python indentation
- Use 2 spaces for JS/TS/JSX indentation
- Use single quotes in JavaScript/TypeScript
- Use double quotes in Python

## AI Assistant Instructions
- Always explain complex logic with comments
- Suggest tests for new functionality
- Consider performance implications
- Follow security best practices
"""

        type_specific_rules = {
            'react': """
## React Specific
- Use functional components with hooks
- Prefer TypeScript interfaces over types
- Use proper prop validation
- Follow React best practices for state management
- Use CSS modules or styled-components for styling
""",
            'django': """
## Django Specific  
- Use Django best practices (fat models, thin views)
- Follow Django's naming conventions
- Use proper serializers for API endpoints
- Include proper error handling
- Use Django's built-in security features
""",
            'python': """
## Python Specific
- Use type hints where appropriate
- Follow SOLID principles
- Include proper exception handling
- Use virtual environments
- Write unit tests with pytest
""",
            'fullstack': """
## Full Stack Specific
- Keep API endpoints RESTful
- Use proper authentication/authorization
- Handle CORS properly
- Use environment variables for configuration
- Separate frontend and backend concerns clearly
"""
        }
        
        rules_content = base_rules + type_specific_rules.get(template.name, '')
        
        with open(self.project_path / '.cursorrules', 'w') as f:
            f.write(rules_content)
    
    def create_claude_ignore(self, template: ProjectTemplate) -> None:
        """Create .claudeignore file"""
        ignore_patterns = [
            "node_modules/",
            "venv/",
            ".env*",
            "*.pyc",
            "__pycache__/",
            ".git/",
            "dist/",
            "build/",
            "coverage/",
            "*.log",
            ".DS_Store"
        ]
        
        if template.has_frontend_dependencies():
            ignore_patterns.extend([
                "package-lock.json",
                "yarn.lock",
                ".next/",
                "out/"
            ])
        
        with open(self.project_path / '.claudeignore', 'w') as f:
            f.write('\n'.join(ignore_patterns))
