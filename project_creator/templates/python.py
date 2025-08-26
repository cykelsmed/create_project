"""
Python template
"""
from textwrap import dedent
from typing import Dict, Any, List
from .base import ProjectTemplate

class PythonTemplate(ProjectTemplate):
    """Python application template"""
    
    @property
    def name(self) -> str:
        return "python"
    
    @property
    def description(self) -> str:
        return "Python application/script"
    
    def get_dependencies(self) -> Dict[str, Any]:
        return {
            'frontend': {},
            'python': {
                'packages': ['requests', 'pytest']
            }
        }
    
    def get_files(self) -> Dict[str, str]:
        return {
            'main.py': self._get_main_py(),
            '.env.example': self._get_env_example()
        }
    
    def get_init_commands(self) -> List[str]:
        return []
    
    def _get_main_py(self) -> str:
        return dedent("""
            \"\"\"
            Main application entry point
            \"\"\"
            
            def main():
                print("Hello, Python!")
                print("This is your new Python project!")

            if __name__ == "__main__":
                main()
        """)
    
    def _get_env_example(self) -> str:
        return dedent("""
            # Environment variables for your Python application
            DEBUG=True
            API_KEY=your-api-key-here
        """)
