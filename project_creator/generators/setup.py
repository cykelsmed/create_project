"""
Setup and initialization generators
"""
from pathlib import Path
import subprocess
from ..templates.base import ProjectTemplate

class SetupGenerator:
    """Generate setup and initialization files"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
    
    def create_git_setup(self) -> None:
        """Initialize Git repository and create .gitignore"""
        # Initialize Git (or reinitialize if exists)
        try:
            subprocess.run(["git", "init"], cwd=self.project_path, check=True)
        except subprocess.CalledProcessError:
            # Git repo might already exist, try to reinitialize
            subprocess.run(["git", "init"], cwd=self.project_path, check=True)
        
        # Create .gitignore
        gitignore_content = """
# Dependencies
node_modules/
venv/

# Environment variables
.env
.env.local
.env.production

# Build outputs
dist/
build/
out/

# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# IDEs
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Logs
*.log
"""
        with open(self.project_path / '.gitignore', 'w') as f:
            f.write(gitignore_content.strip())
        
        # Add and commit only if there are changes
        try:
            subprocess.run(["git", "add", "."], cwd=self.project_path, check=True)
            # Check if there are changes to commit
            result = subprocess.run(["git", "status", "--porcelain"], cwd=self.project_path, capture_output=True, text=True, check=True)
            if result.stdout.strip():
                subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=self.project_path, check=True)
        except subprocess.CalledProcessError:
            # Git operations might fail, but that's okay
            pass
    
    def create_virtual_environment(self) -> None:
        """Create Python virtual environment"""
        import sys
        subprocess.run([sys.executable, "-m", "venv", "venv"], cwd=self.project_path, check=True)
