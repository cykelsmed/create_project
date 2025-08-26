"""
Base template class
"""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, List

class ProjectTemplate(ABC):
    """Base class for all project templates"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Template name"""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Template description"""
        pass
    
    @abstractmethod
    def get_dependencies(self) -> Dict[str, Any]:
        """Get project dependencies"""
        pass
    
    @abstractmethod
    def get_files(self) -> Dict[str, str]:
        """Get template files"""
        pass
    
    @abstractmethod
    def get_init_commands(self) -> List[str]:
        """Get initialization commands"""
        pass
    
    def has_python_dependencies(self) -> bool:
        """Check if template has Python dependencies"""
        deps = self.get_dependencies()
        return bool(deps.get('python', {}).get('packages', []))
    
    def has_frontend_dependencies(self) -> bool:
        """Check if template has frontend dependencies"""
        deps = self.get_dependencies()
        return bool(deps.get('frontend', {}).get('packages', []))
