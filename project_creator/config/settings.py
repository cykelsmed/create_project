"""
Configuration management for project creator
"""
from pathlib import Path
from typing import Dict, Any
import yaml

class Config:
    """Centralized configuration management"""
    
    def __init__(self, config_path: Path = None):
        self.config_path = config_path or Path.home() / ".create_project" / "config.yaml"
        self._config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        if self.config_path.exists():
            with open(self.config_path) as f:
                return yaml.safe_load(f)
        return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            'default_project_path': str(Path.home() / "Development"),
            'preferred_package_manager': 'npm',
            'auto_install_dependencies': True,
            'create_git_repo': True,
            'ai_assistant_enabled': True,
            'logging_level': 'INFO'
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        self._config[key] = value
        self._save_config()
    
    def _save_config(self):
        """Save configuration to file"""
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_path, 'w') as f:
            yaml.dump(self._config, f)
