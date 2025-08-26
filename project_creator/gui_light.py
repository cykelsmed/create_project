"""
Light GUI application for Project Creator (no external dependencies)
"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path
import sys
import os

# Add the project root to the path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from project_creator.config.simple_settings import SimpleConfig
from project_creator.main import ProjectCreator
from project_creator.utils.validation import ProjectValidator
from project_creator.utils.exceptions import ProjectCreatorError

class ProjectCreatorLightGUI:
    """Light GUI application for creating projects"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Project Creator")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Load configuration
        self.config = SimpleConfig()
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="🚀 Project Creator", 
                               font=("Helvetica", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Project name
        ttk.Label(main_frame, text="Project Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.project_name_var = tk.StringVar()
        self.project_name_entry = ttk.Entry(main_frame, textvariable=self.project_name_var, width=40)
        self.project_name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Project description
        ttk.Label(main_frame, text="Description:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.description_text = tk.Text(main_frame, height=4, width=40)
        self.description_text.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Project type
        ttk.Label(main_frame, text="Project Type:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.project_type_var = tk.StringVar(value="python")
        project_types = ["python", "react", "django", "fullstack"]
        self.project_type_combo = ttk.Combobox(main_frame, textvariable=self.project_type_var, 
                                              values=project_types, state="readonly", width=37)
        self.project_type_combo.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        
        # Project path
        ttk.Label(main_frame, text="Location:").grid(row=4, column=0, sticky=tk.W, pady=5)
        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        path_frame.columnconfigure(0, weight=1)
        
        self.project_path_var = tk.StringVar(value=self.config.get('default_project_path'))
        self.path_entry = ttk.Entry(path_frame, textvariable=self.project_path_var)
        self.path_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        browse_btn = ttk.Button(path_frame, text="Browse", command=self.browse_path)
        browse_btn.grid(row=0, column=1, padx=(5, 0))
        
        # Options frame
        options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
        options_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=20)
        options_frame.columnconfigure(1, weight=1)
        
        # Checkboxes
        self.install_deps_var = tk.BooleanVar(value=True)
        self.init_git_var = tk.BooleanVar(value=True)
        self.force_var = tk.BooleanVar(value=False)
        
        ttk.Checkbutton(options_frame, text="Install dependencies", 
                       variable=self.install_deps_var).grid(row=0, column=0, sticky=tk.W)
        ttk.Checkbutton(options_frame, text="Initialize Git repository", 
                       variable=self.init_git_var).grid(row=1, column=0, sticky=tk.W)
        ttk.Checkbutton(options_frame, text="Force overwrite existing directory", 
                       variable=self.force_var).grid(row=2, column=0, sticky=tk.W)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=20)
        
        create_btn = ttk.Button(button_frame, text="Create Project", 
                               command=self.create_project, style="Accent.TButton")
        create_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        cancel_btn = ttk.Button(button_frame, text="Cancel", command=self.root.quit)
        cancel_btn.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress_var = tk.StringVar(value="Ready to create project")
        self.progress_label = ttk.Label(main_frame, textvariable=self.progress_var)
        self.progress_label.grid(row=7, column=0, columnspan=2, pady=(10, 0))
        
        # Focus on project name entry
        self.project_name_entry.focus()
        
    def browse_path(self):
        """Browse for project directory"""
        directory = filedialog.askdirectory(initialdir=self.project_path_var.get())
        if directory:
            self.project_path_var.set(directory)
    
    def create_project(self):
        """Create the project"""
        try:
            # Get values
            project_name = self.project_name_var.get().strip()
            description = self.description_text.get("1.0", tk.END).strip()
            project_type = self.project_type_var.get()
            project_path = Path(self.project_path_var.get())
            install_deps = self.install_deps_var.get()
            init_git = self.init_git_var.get()
            force = self.force_var.get()
            
            # Validate
            if not project_name:
                messagebox.showerror("Error", "Please enter a project name")
                return
            
            # Update progress
            self.progress_var.set("Validating project parameters...")
            self.root.update()
            
            # Validate project name and path
            ProjectValidator.validate_project_name(project_name)
            full_project_path = project_path / project_name
            ProjectValidator.validate_project_path(full_project_path, force)
            
            # Update progress
            self.progress_var.set("Creating project...")
            self.root.update()
            
            # Create project
            creator = ProjectCreator(self.config)
            creator.create_project(
                name=project_name,
                project_type=project_type,
                path=full_project_path,
                install_deps=install_deps,
                init_git=init_git,
                force=force
            )
            
            # Update progress
            self.progress_var.set("Project created successfully!")
            self.root.update()
            
            # Show success message
            messagebox.showinfo("Success", 
                              f"Project '{project_name}' created successfully!\n\n"
                              f"Location: {full_project_path}\n\n"
                              f"Next steps:\n"
                              f"1. cd {full_project_path}\n"
                              f"2. source venv/bin/activate (if Python project)\n"
                              f"3. Start coding!")
            
            # Clear form
            self.clear_form()
            
        except ProjectCreatorError as e:
            messagebox.showerror("Error", str(e))
            self.progress_var.set("Error occurred")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")
            self.progress_var.set("Error occurred")
    
    def clear_form(self):
        """Clear the form"""
        self.project_name_var.set("")
        self.description_text.delete("1.0", tk.END)
        self.project_type_var.set("python")
        self.project_path_var.set(self.config.get('default_project_path'))
        self.install_deps_var.set(True)
        self.init_git_var.set(True)
        self.force_var.set(False)
        self.progress_var.set("Ready to create project")
        self.project_name_entry.focus()
    
    def run(self):
        """Run the GUI application"""
        self.root.mainloop()

def main():
    """Main function to run the GUI"""
    app = ProjectCreatorLightGUI()
    app.run()

if __name__ == "__main__":
    main()
