"""
Template registry and management
"""
from typing import Dict, Type
from .base import ProjectTemplate
from .react import ReactTemplate
from .django import DjangoTemplate
from .python import PythonTemplate
from .fullstack import FullstackTemplate

_TEMPLATES: Dict[str, Type[ProjectTemplate]] = {
    'react': ReactTemplate,
    'django': DjangoTemplate,
    'python': PythonTemplate,
    'fullstack': FullstackTemplate
}

def get_template(template_name: str) -> ProjectTemplate:
    """Get template by name"""
    if template_name not in _TEMPLATES:
        from ..utils.exceptions import TemplateNotFoundError
        raise TemplateNotFoundError(f"Template '{template_name}' not found")
    
    return _TEMPLATES[template_name]()

def list_templates() -> list[str]:
    """List all available templates"""
    return list(_TEMPLATES.keys())

def register_template(name: str, template_class: Type[ProjectTemplate]):
    """Register a new template"""
    _TEMPLATES[name] = template_class
