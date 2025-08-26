"""
Fullstack Django + React template
"""
from textwrap import dedent
from typing import Dict, Any, List
from .base import ProjectTemplate

class FullstackTemplate(ProjectTemplate):
    """Django + React fullstack template"""
    
    @property
    def name(self) -> str:
        return "fullstack"
    
    @property
    def description(self) -> str:
        return "Django + React fullstack"
    
    def get_dependencies(self) -> Dict[str, Any]:
        return {
            'frontend': {
                'packages': ['react', 'react-dom', 'axios'],
                'dev_packages': ['typescript', '@types/react', '@types/react-dom', 'vite', '@vitejs/plugin-react', 'eslint']
            },
            'python': {
                'packages': ['django', 'djangorestframework', 'django-cors-headers', 'python-decouple']
            }
        }
    
    def get_files(self) -> Dict[str, str]:
        return {
            'backend/manage.py': self._get_manage_py(),
            'frontend/index.html': self._get_index_html(),
            'frontend/src/main.tsx': self._get_main_tsx(),
            'frontend/src/App.tsx': self._get_app_tsx(),
            'frontend/vite.config.ts': self._get_vite_config(),
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
    
    def _get_index_html(self) -> str:
        return dedent("""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Fullstack App</title>
            </head>
            <body>
                <div id="root"></div>
                <script type="module" src="/src/main.tsx"></script>
            </body>
            </html>
        """)
    
    def _get_main_tsx(self) -> str:
        return dedent("""
            import React from 'react';
            import ReactDOM from 'react-dom/client';
            import App from './App.tsx';
            import './index.css';

            ReactDOM.createRoot(document.getElementById('root')!).render(
                <React.StrictMode>
                    <App />
                </React.StrictMode>,
            );
        """)
    
    def _get_app_tsx(self) -> str:
        return dedent("""
            function App() {
                return (
                    <div>
                        <h1>Fullstack App</h1>
                        <p>Django backend + React frontend</p>
                    </div>
                );
            }

            export default App;
        """)
    
    def _get_vite_config(self) -> str:
        return dedent("""
            import { defineConfig } from 'vite'
            import react from '@vitejs/plugin-react'

            export default defineConfig({
              plugins: [react()],
              server: {
                proxy: {
                  '/api': {
                    target: 'http://localhost:8000',
                    changeOrigin: true,
                  },
                },
              },
            })
        """)
    
    def _get_env_example(self) -> str:
        return dedent("""
            # Backend (Django)
            DEBUG=True
            SECRET_KEY=your-secret-key-here
            DATABASE_URL=sqlite:///db.sqlite3
            ALLOWED_HOSTS=localhost,127.0.0.1
            CORS_ALLOWED_ORIGINS=http://localhost:5173
            
            # Frontend
            VITE_API_BASE_URL=http://localhost:8000/api
        """)
