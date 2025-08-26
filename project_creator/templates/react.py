"""
React/TypeScript template
"""
from textwrap import dedent
from typing import Dict, Any, List
from .base import ProjectTemplate

class ReactTemplate(ProjectTemplate):
    """React/TypeScript frontend template"""
    
    @property
    def name(self) -> str:
        return "react"
    
    @property
    def description(self) -> str:
        return "React/TypeScript frontend projekt"
    
    def get_dependencies(self) -> Dict[str, Any]:
        return {
            'frontend': {
                'packages': ['react', 'react-dom'],
                'dev_packages': ['typescript', '@types/react', '@types/react-dom', 'vite', '@vitejs/plugin-react', 'eslint', '@typescript-eslint/parser', 'eslint-plugin-react-hooks', 'eslint-plugin-react-refresh']
            },
            'python': {}
        }
    
    def get_files(self) -> Dict[str, str]:
        return {
            'index.html': self._get_index_html(),
            'src/main.tsx': self._get_main_tsx(),
            'src/App.tsx': self._get_app_tsx(),
            'src/index.css': self._get_index_css(),
            'vite.config.ts': self._get_vite_config(),
            'tsconfig.json': self._get_tsconfig(),
            'tsconfig.node.json': self._get_tsconfig_node()
        }
    
    def get_init_commands(self) -> List[str]:
        return ['npm init -y']
    
    def _get_index_html(self) -> str:
        return dedent("""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Vite + React + TS</title>
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
                        <h1>Hello, React!</h1>
                        <p>This is a basic React/TypeScript setup.</p>
                    </div>
                );
            }

            export default App;
        """)
    
    def _get_index_css(self) -> str:
        return dedent("""
            :root {
              font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
              line-height: 1.5;
              font-weight: 400;
              
              color-scheme: light dark;
              color: rgba(255, 255, 255, 0.87);
              background-color: #242424;
              
              font-synthesis: none;
              text-rendering: optimizeLegibility;
              -webkit-font-smoothing: antialiased;
              -moz-osx-font-smoothing: grayscale;
              -webkit-text-size-adjust: 100%;
            }

            body {
              margin: 0;
              display: flex;
              place-items: center;
              min-width: 320px;
              min-height: 100vh;
            }

            #root {
              max-width: 1280px;
              margin: 0 auto;
              padding: 2rem;
              text-align: center;
            }

            h1 {
              font-size: 3.2em;
              line-height: 1.1;
            }

            @media (prefers-color-scheme: light) {
              :root {
                color: #213547;
                background-color: #ffffff;
              }
            }
        """)
    
    def _get_vite_config(self) -> str:
        return dedent("""
            import { defineConfig } from 'vite'
            import react from '@vitejs/plugin-react'

            export default defineConfig({
              plugins: [react()],
            })
        """)
    
    def _get_tsconfig(self) -> str:
        return dedent("""
            {
                "compilerOptions": {
                    "target": "ES2020",
                    "useDefineForClassFields": true,
                    "lib": ["ES2020", "DOM", "DOM.Iterable"],
                    "module": "ESNext",
                    "skipLibCheck": true,
                    "moduleResolution": "bundler",
                    "allowImportingTsExtensions": true,
                    "resolveJsonModule": true,
                    "isolatedModules": true,
                    "noEmit": true,
                    "jsx": "react-jsx",
                    "strict": true,
                    "noUnusedLocals": true,
                    "noUnusedParameters": true,
                    "noFallthroughCasesInSwitch": true
                },
                "include": ["src"],
                "references": [{ "path": "./tsconfig.node.json" }]
            }
        """)
    
    def _get_tsconfig_node(self) -> str:
        return dedent("""
            {
              "compilerOptions": {
                "composite": true,
                "skipLibCheck": true,
                "module": "ESNext",
                "moduleResolution": "bundler",
                "allowSyntheticDefaultImports": true
              },
              "include": ["vite.config.ts"]
            }
        """)
