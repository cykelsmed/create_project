"""
Django template
"""
from textwrap import dedent
from typing import Dict, Any, List
from .base import ProjectTemplate

class DjangoTemplate(ProjectTemplate):
    """Django web application template"""
    
    @property
    def name(self) -> str:
        return "django"
    
    @property
    def description(self) -> str:
        return "Django web application"
    
    def get_dependencies(self) -> Dict[str, Any]:
        return {
            'frontend': {},
            'python': {
                'packages': ['django', 'djangorestframework', 'python-decouple', 'django-cors-headers']
            }
        }
    
    def get_files(self) -> Dict[str, str]:
        return {
            'manage.py': self._get_manage_py(),
            '.env.example': self._get_env_example()
        }
    
    def get_init_commands(self) -> List[str]:
        return []
    
    def _get_manage_py(self) -> str:
        return dedent("""
            #!/usr/bin/env python
            \"\"\"Django's command-line utility for administrative tasks.\"\"\"
            import os
            import sys

            if __name__ == '__main__':
                os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
                try:
                    from django.core.management import execute_from_command_line
                except ImportError as exc:
                    raise ImportError(
                        "Couldn't import Django. Are you sure it's installed and "
                        "available on your PYTHONPATH environment variable? Did you "
                        "forget to activate a virtual environment?"
                    ) from exc
                execute_from_command_line(sys.argv)
        """)
    
    def _get_env_example(self) -> str:
        return dedent("""
            DEBUG=True
            SECRET_KEY=your-secret-key-here
            DATABASE_URL=sqlite:///db.sqlite3
            ALLOWED_HOSTS=localhost,127.0.0.1
        """)
