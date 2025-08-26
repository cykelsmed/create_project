"""
File operations and dependency management
"""
from pathlib import Path
from typing import Dict, Any, List
import subprocess
import shutil
import json
from .exceptions import DependencyInstallError

class FileManager:
    """Handle file and directory operations"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
    
    def create_directory_structure(self, structure: Dict[str, Any]) -> None:
        """Create directory structure recursively"""
        for path, content in structure.items():
            full_path = self.project_path / path
            
            if isinstance(content, dict):
                # Directory
                full_path.mkdir(parents=True, exist_ok=True)
                self.create_directory_structure(content)
            else:
                # File
                full_path.parent.mkdir(parents=True, exist_ok=True)
                with open(full_path, 'w') as f:
                    f.write(content)
    
    def create_file(self, relative_path: str, content: str) -> None:
        """Create a single file with content"""
        file_path = self.project_path / relative_path
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, 'w') as f:
            f.write(content)
    
    def copy_template_files(self, template_dir: Path) -> None:
        """Copy template files to project directory"""
        if template_dir.exists():
            shutil.copytree(template_dir, self.project_path, dirs_exist_ok=True)

class DependencyManager:
    """Handle dependency installation"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
    
    def install_python_dependencies(self, requirements: List[str]) -> None:
        """Install Python dependencies"""
        if not requirements:
            return
        
        requirements_file = self.project_path / "requirements.txt"
        with open(requirements_file, 'w') as f:
            f.write('\n'.join(requirements))
        
        try:
            subprocess.run([
                f"{self.project_path}/venv/bin/pip", 
                "install", "-r", "requirements.txt"
            ], cwd=self.project_path, check=True)
        except subprocess.CalledProcessError as e:
            raise DependencyInstallError(f"Failed to install Python dependencies: {e}")
    
    def install_node_dependencies(self, packages: Dict[str, list]) -> None:
        """Install Node.js dependencies"""
        if not packages:
            return
        
        package_json = {
            "name": self.project_path.name,
            "version": "1.0.0",
            "type": "module",
            "scripts": {
                "dev": "vite",
                "build": "vite build",
                "preview": "vite preview"
            },
            "dependencies": {pkg: "*" for pkg in packages.get('packages', [])},
            "devDependencies": {pkg: "*" for pkg in packages.get('dev_packages', [])}
        }
        
        with open(self.project_path / "package.json", 'w') as f:
            json.dump(package_json, f, indent=2)
        
        try:
            subprocess.run(["npm", "install"], cwd=self.project_path, check=True)
        except subprocess.CalledProcessError as e:
            raise DependencyInstallError(f"Failed to install Node.js dependencies: {e}")
