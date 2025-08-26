"""
Main application class
"""
from pathlib import Path
from typing import Optional
import subprocess

from .config.settings import Config
from .templates import get_template
from .generators.ai_config import AIConfigGenerator
from .generators.docs import DocumentationGenerator
from .generators.setup import SetupGenerator
from .utils.file_ops import FileManager, DependencyManager
from .utils.validation import ProjectValidator
from .utils.logging import ProjectLogger, ProgressTracker
from .utils.exceptions import ProjectCreatorError

class ProjectCreator:
    """Main project creation class"""
    
    def __init__(self, config: Config):
        self.config = config
        self.logger = ProjectLogger(config.get('logging_level', 'INFO'))
        self.file_manager = None
        self.dependency_manager = None
        self.setup_generator = None
    
    def create_project(self, 
                      name: str,
                      project_type: str,
                      path: Path,
                      install_deps: bool = True,
                      init_git: bool = True,
                      force: bool = False) -> None:
        """Main project creation method"""
        
        progress = ProgressTracker(6)  # Total steps
        
        try:
            # Step 1: Validation
            progress.step("Validating project parameters...")
            self._validate_project(name, project_type, path, force)
            
            # Step 2: Initialize managers
            progress.step("Initializing project managers...")
            self._initialize_managers(path)
            
            # Step 3: Get template
            progress.step("Loading project template...")
            template = get_template(project_type)
            
            # Step 4: Create project structure
            progress.step("Creating project structure...")
            self._create_project_structure(template)
            
            # Step 5: Generate configuration
            progress.step("Generating AI configuration...")
            self._generate_configuration(template)
            
            # Step 6: Setup development environment
            progress.step("Setting up development environment...")
            self._setup_development_environment(template, install_deps, init_git)
            
            self.logger.info(f"Project '{name}' created successfully!")
            
        except Exception as e:
            self.logger.error(f"Failed to create project: {e}")
            raise
    
    def _validate_project(self, name: str, project_type: str, path: Path, force: bool = False) -> None:
        """Validate project parameters"""
        ProjectValidator.validate_project_name(name)
        ProjectValidator.validate_project_path(path, force)
        ProjectValidator.validate_template_name(project_type, ['react', 'django', 'python', 'fullstack'])
    
    def _initialize_managers(self, path: Path) -> None:
        """Initialize file and dependency managers"""
        self.file_manager = FileManager(path)
        self.dependency_manager = DependencyManager(path)
        self.setup_generator = SetupGenerator(path)
    
    def _create_project_structure(self, template) -> None:
        """Create the basic project structure"""
        # Create main directory
        self.file_manager.project_path.mkdir(parents=True, exist_ok=True)
        
        # Create virtual environment for Python projects
        if template.has_python_dependencies():
            self.setup_generator.create_virtual_environment()
        
        # Create files from template
        files = template.get_files()
        for file_path, content in files.items():
            self.file_manager.create_file(file_path, content)
    
    def _generate_configuration(self, template) -> None:
        """Generate AI configuration and documentation"""
        # Generate AI configuration
        ai_generator = AIConfigGenerator(self.file_manager.project_path)
        ai_generator.create_cursor_rules(template)
        ai_generator.create_claude_ignore(template)
        
        # Generate documentation
        doc_generator = DocumentationGenerator(self.file_manager.project_path)
        doc_generator.create_readme(self.file_manager.project_path.name, template)
    
    def _setup_development_environment(self, template, install_deps: bool, init_git: bool) -> None:
        """Setup development environment"""
        if install_deps:
            self._install_dependencies(template)
        
        if init_git:
            self.setup_generator.create_git_setup()
    
    def _install_dependencies(self, template) -> None:
        """Install project dependencies"""
        deps = template.get_dependencies()
        
        if deps.get('python', {}).get('packages'):
            self.dependency_manager.install_python_dependencies(deps['python']['packages'])
        
        if deps.get('frontend'):
            self.dependency_manager.install_node_dependencies(deps['frontend'])
