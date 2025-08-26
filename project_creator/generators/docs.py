"""
Documentation generators
"""
from pathlib import Path
import platform
from ..templates.base import ProjectTemplate

class DocumentationGenerator:
    """Generate project documentation"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
    
    def create_readme(self, project_name: str, template: ProjectTemplate) -> None:
        """Create comprehensive README with AI context"""
        activation_cmd = "venv\\Scripts\\activate" if platform.system() == 'Windows' else "source venv/bin/activate"
        
        readme_content = f"""# {project_name}

{template.description}

## Setup

### Development Environment
```bash
# Aktiver virtual environment
{activation_cmd}

# Installer dependencies
{"pip install -r requirements.txt" if template.has_python_dependencies() else ""}
{"npm install" if template.has_frontend_dependencies() else ""}
```

## AI Assistant Context

Dette projekt er et **{template.description}**.

### Projektstruktur
- Følger {'Django' if 'django' in template.name else 'moderne'} konventioner
- Bruger {'TypeScript/React' if template.name in ['react', 'fullstack'] else 'Python'} som primært sprog
- {'API backend med Django REST framework' if 'django' in template.name else ''}
- {'Fullstack setup med separate frontend/backend folders' if template.name == 'fullstack' else ''}

### Vigtige noter til AI:
- Projektet bruger virtual environment (venv/) for Python dependencies
- {'TypeScript er preferred over JavaScript' if template.name in ['react', 'fullstack'] else ''}
- {'Django REST framework til API endpoints' if 'django' in template.name else ''}
- {'Vite som build tool og dev server' if template.name in ['react', 'fullstack'] else ''}
- {'CORS konfiguration for frontend/backend kommunikation' if template.name == 'fullstack' else ''}
- Følg established coding standards i .cursorrules
- Environment variables skal defineres i .env (se .env.example)

## Development

### Running the project
```bash
{"# Backend (Django)" if template.name in ['django', 'fullstack'] else ""}
{"python manage.py runserver  # Port 8000" if template.name in ['django', 'fullstack'] else ""}

{"# Frontend (React)" if template.name in ['react', 'fullstack'] else ""}
{"npm run dev  # Port 5173" if template.name in ['react', 'fullstack'] else ""}

{"# Python script" if template.name == 'python' else ""}
{"python main.py" if template.name == 'python' else ""}
```

### Project Structure
{"- `frontend/` - React TypeScript application" if template.name == 'fullstack' else ""}
{"- `backend/` - Django REST API" if template.name == 'fullstack' else ""}
{"- `src/` - React components og logic" if template.name == 'react' else ""}
{"- `main.py` - Application entry point" if template.name == 'python' else ""}
- `.cursorrules` - AI assistant regler og context
- `.claudeignore` - Filer Claude Code skal ignorere
- `requirements.txt` - Python dependencies
{"- `package.json` - Node.js dependencies" if template.name in ['react', 'fullstack'] else ""}

### Environment Setup
1. Kopier `.env.example` til `.env`
2. Udfyld relevante værdier i `.env`
3. {"Kør `python manage.py migrate` (Django projekter)" if template.name in ['django', 'fullstack'] else ""}

## Testing
{"- Python: `pytest`" if template.has_python_dependencies() else ""}
{"- TypeScript: `npm test` (setup required)" if template.has_frontend_dependencies() else ""}
"""
        
        with open(self.project_path / 'README.md', 'w') as f:
            f.write(readme_content)
