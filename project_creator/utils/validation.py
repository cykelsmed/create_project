"""
Validation utilities for project creation
"""
import re
from pathlib import Path
from typing import Optional
from .exceptions import InvalidProjectNameError, ProjectExistsError, TemplateNotFoundError

class ProjectValidator:
    """Validation utilities for project creation"""
    
    @staticmethod
    def validate_project_name(name: str) -> None:
        """Validate project name follows conventions"""
        if not name:
            raise InvalidProjectNameError("Project name cannot be empty")
        
        if len(name) > 50:
            raise InvalidProjectNameError("Project name too long (max 50 characters)")
        
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):
            raise InvalidProjectNameError(
                "Project name must start with a letter and contain only letters, numbers, hyphens, and underscores"
            )
        
        # Check for reserved names
        reserved_names = {'test', 'tmp', 'temp', 'node_modules', 'venv', 'src', 'dist'}
        if name.lower() in reserved_names:
            raise InvalidProjectNameError(f"'{name}' is a reserved name")
    
    @staticmethod
    def validate_project_path(path: Path, force: bool = False) -> None:
        """Validate project path is safe and available"""
        if path.exists() and not force:
            raise ProjectExistsError(f"Project directory '{path}' already exists")
        
        # Prevent overwriting system directories
        forbidden_paths = ['/usr', '/etc', '/root', '/bin', '/sbin', '/var', '/tmp']
        path_str = str(path)
        for forbidden_path in forbidden_paths:
            if path_str.startswith(forbidden_path):
                raise InvalidProjectNameError("Cannot create project in system directories")
    
    @staticmethod
    def validate_template_name(template_name: str, available_templates: list[str]) -> None:
        """Validate template exists"""
        if template_name not in available_templates:
            raise TemplateNotFoundError(
                f"Template '{template_name}' not found. Available: {', '.join(available_templates)}"
            )
