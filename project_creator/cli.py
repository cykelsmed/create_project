"""
Command-line interface
"""
import click
import sys
from pathlib import Path
from typing import Optional

from .config.settings import Config
from .main import ProjectCreator
from .utils.validation import ProjectValidator
from .utils.exceptions import ProjectCreatorError

@click.command()
@click.argument('project_name')
@click.option('--type', '-t', 'project_type', 
              default='python', 
              help='Project type (react, django, python, fullstack)')
@click.option('--path', '-p', 'project_path',
              help='Custom project path')
@click.option('--force', '-f', is_flag=True,
              help='Force overwrite existing directory')
@click.option('--no-deps', is_flag=True,
              help='Skip dependency installation')
@click.option('--no-git', is_flag=True,
              help='Skip Git initialization')
@click.option('--config', '-c', 'config_file',
              help='Custom configuration file')
def create_project(project_name: str, 
                  project_type: str,
                  project_path: Optional[str],
                  force: bool,
                  no_deps: bool,
                  no_git: bool,
                  config_file: Optional[str]):
    """Create a new development project with AI configuration"""
    
    try:
        # Load configuration
        config_path = Path(config_file) if config_file else None
        config = Config(config_path)
        
        # Validation
        ProjectValidator.validate_project_name(project_name)
        
        # Determine project path
        base_path = Path(project_path or config.get('default_project_path'))
        full_project_path = base_path / project_name
        
        ProjectValidator.validate_project_path(full_project_path, force)
        
        # Create project
        creator = ProjectCreator(config)
        creator.create_project(
            name=project_name,
            project_type=project_type,
            path=full_project_path,
            install_deps=not no_deps,
            init_git=not no_git,
            force=force
        )
        
        click.echo(f"✅ Project '{project_name}' created successfully!")
        click.echo(f"📁 Location: {full_project_path}")
        
        # Show next steps
        click.echo(f"\nNext steps:")
        if project_type in ['django', 'python', 'fullstack']:
            click.echo(f"  cd {full_project_path}")
            click.echo(f"  source venv/bin/activate")
            if not no_deps:
                click.echo(f"  pip install -r requirements.txt")
        
        if project_type in ['react', 'fullstack'] and not no_deps:
            click.echo(f"  npm install")
        
    except ProjectCreatorError as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Unexpected error: {e}", err=True)
        sys.exit(1)

if __name__ == "__main__":
    create_project()
