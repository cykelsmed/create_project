# Project Creator

Automatisk projekt setup med AI-konfiguration

## Installation

```bash
# Installer dependencies
pip install -r requirements.txt

# Eller installer som package
pip install -e .
```

### macOS Desktop App

#### Light Version (Anbefalet)
- **Størrelse**: ~88MB
- **Dependencies**: Minimal (ingen YAML, ingen Click)
- **Funktioner**: Alle core funktioner
- **Build**: `./build_light_app.sh`

#### Full Version
- **Størrelse**: ~103MB  
- **Dependencies**: Komplet (YAML, Click, etc.)
- **Funktioner**: Alle funktioner inklusive CLI
- **Build**: `./build_app.sh`

Begge versioner giver samme GUI oplevelse for projekt oprettelse.

## Brug

### GUI App (Anbefalet)
```bash
# Byg og installer light GUI app til Desktop (anbefalet)
./build_light_app.sh
cp -r dist/ProjectCreatorLight.app ~/Desktop/

# Eller byg full version
./build_app.sh
./install_to_desktop.sh

# Eller kør GUI direkte
python3 run_gui_light.py  # Light version
python3 run_gui.py        # Full version
```

### Command Line
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

### GUI App
- 🖥️ **Brugervenlig interface** med tkinter
- 📝 **Projektbeskrivelse** input for bedre AI kontekst
- 🎯 **Visuel projekttype** valg (dropdown)
- 📁 **Browse funktion** til projektsti
- ⚙️ **Avancerede options** (dependencies, Git, force)
- 📊 **Progress tracking** med status updates
- 🎨 **Moderne design** med temaer

### Core Features
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

