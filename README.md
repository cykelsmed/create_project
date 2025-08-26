# Project Creator

Automatisk projekt setup med AI-konfiguration

## Installation

```bash
# Installer dependencies
pip install -r requirements.txt

# Eller installer som package
pip install -e .
```

## Brug

```bash
# Opret et nyt projekt
python main.py <projekt_navn> [type]

# Eksempler
python main.py my-react-app react
python main.py my-django-api django
python main.py my-python-tool python
python main.py my-fullstack-app fullstack
```

## Tilgængelige projekttyper

- **react**: React/TypeScript frontend projekt
- **django**: Django web application
- **python**: Python application/script
- **fullstack**: Django + React fullstack

## Funktioner

- ✅ Automatisk projektstruktur
- ✅ AI assistant konfiguration (.cursorrules, .claudeignore)
- ✅ Virtual environment setup
- ✅ Dependency installation
- ✅ Git initialisering
- ✅ Komplet dokumentation
- ✅ Progress tracking
- ✅ Error handling
- ✅ Validering

## Projektstruktur

```
project_creator/
├── __init__.py
├── main.py              # Main application class
├── cli.py               # Command-line interface
├── config/
│   ├── __init__.py
│   └── settings.py      # Configuration management
├── templates/
│   ├── __init__.py      # Template registry
│   ├── base.py          # Base template class
│   ├── react.py         # React template
│   ├── django.py        # Django template
│   ├── python.py        # Python template
│   └── fullstack.py     # Fullstack template
├── generators/
│   ├── __init__.py
│   ├── ai_config.py     # AI configuration generator
│   ├── docs.py          # Documentation generator
│   └── setup.py         # Setup generator
└── utils/
    ├── __init__.py
    ├── exceptions.py    # Custom exceptions
    ├── validation.py    # Validation utilities
    ├── logging.py       # Logging and progress tracking
    └── file_ops.py      # File operations
```

## Udvikling

```bash
# Installer i development mode
pip install -e .

# Kør tests (når implementeret)
pytest

# Kør linting (når implementeret)
flake8 project_creator/
```

## Licens

MIT License

