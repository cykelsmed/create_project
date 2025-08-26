"""
Custom exceptions for project creator
"""

class ProjectCreatorError(Exception):
    """Base exception for project creator"""
    pass

class InvalidProjectNameError(ProjectCreatorError):
    """Raised when project name is invalid"""
    pass

class ProjectExistsError(ProjectCreatorError):
    """Raised when project directory already exists"""
    pass

class TemplateNotFoundError(ProjectCreatorError):
    """Raised when template is not found"""
    pass

class DependencyInstallError(ProjectCreatorError):
    """Raised when dependency installation fails"""
    pass

class ValidationError(ProjectCreatorError):
    """Raised when validation fails"""
    pass
