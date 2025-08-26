"""
Logging and progress tracking utilities
"""
import logging
from typing import Optional

class ProjectLogger:
    """Centralized logging for project creator"""
    
    def __init__(self, level: str = "INFO"):
        self.logger = logging.getLogger("project_creator")
        self.logger.setLevel(getattr(logging, level.upper()))
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def info(self, message: str):
        """Log info message"""
        self.logger.info(message)
    
    def error(self, message: str):
        """Log error message"""
        self.logger.error(message)
    
    def debug(self, message: str):
        """Log debug message"""
        self.logger.debug(message)

class ProgressTracker:
    """Track progress of project creation"""
    
    def __init__(self, total_steps: int):
        self.total_steps = total_steps
        self.current_step = 0
    
    def step(self, message: str):
        """Increment step and show progress"""
        self.current_step += 1
        print(f"[{self.current_step}/{self.total_steps}] {message}")
