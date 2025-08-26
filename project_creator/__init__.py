"""
Project Creator - Automatisk projekt setup med AI-konfiguration
"""

__version__ = "1.0.0"
__author__ = "Your Name"

from .main import ProjectCreator
from .templates import get_template, list_templates

__all__ = ["ProjectCreator", "get_template", "list_templates"]
