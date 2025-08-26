#!/usr/bin/env python3
"""
Script to run the Project Creator GUI
"""
import sys
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, str(Path(__file__).parent))

from project_creator.gui import main

if __name__ == "__main__":
    main()
