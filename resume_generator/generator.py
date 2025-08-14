"""Core resume generation logic using Jinja2 and WeasyPrint."""

import json
import os
from pathlib import Path
from typing import Dict, Any

from jinja2 import Environment, FileSystemLoader, select_autoescape
from weasyprint import HTML, CSS


class ResumeGenerator:
    """Generates PDF resumes from JSON data using HTML templates."""
    
    def __init__(self, templates_dir: str = None):
        """Initialize the generator with template directory.
        
        Args:
            templates_dir: Path to templates directory. If None, uses package default.
        """
        if templates_dir is None:
            # Use templates directory relative to package
            package_dir = Path(__file__).parent.parent
            templates_dir = package_dir / "templates"
        
        self.templates_dir = Path(templates_dir)
        
        # Initialize Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            autoescape=select_autoescape(['html', 'xml'])
        )
    
    def load_json_data(self, json_file: str) -> Dict[str, Any]:
        """Load resume data from JSON file.
        
        Args:
            json_file: Path to JSON file containing resume data
            
        Returns:
            Dictionary containing resume data
            
        Raises:
            FileNotFoundError: If JSON file doesn't exist
            json.JSONDecodeError: If JSON is invalid
            ValueError: If required fields are missing
        """
        json_path = Path(json_file)
        
        if not json_path.exists():
            raise FileNotFoundError(f"JSON file not found: {json_file}")
        
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Validate required fields
        self._validate_json_data(data)
        
        return data
    
    def _validate_json_data(self, data: Dict[str, Any]) -> None:
        """Validate that required fields are present in JSON data.
        
        Args:
            data: Resume data dictionary
            
        Raises:
            ValueError: If required fields are missing
        """
        required_fields = ['personal']
        
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Required field '{field}' missing from JSON data")
        
        # Validate personal info
        personal = data['personal']
        required_personal = ['name', 'email']
        
        for field in required_personal:
            if field not in personal:
                raise ValueError(f"Required personal field '{field}' missing from JSON data")
    
    def get_available_templates(self) -> list:
        """Get list of available template names.
        
        Returns:
            List of template names (without .html extension)
        """
        templates = []
        
        if not self.templates_dir.exists():
            return templates
        
        for file in self.templates_dir.glob("*.html"):
            templates.append(file.stem)
        
        return sorted(templates)
    
    def generate_html(self, data: Dict[str, Any], template_name: str = "modern") -> str:
        """Generate HTML from template and data.
        
        Args:
            data: Resume data dictionary
            template_name: Name of template to use (without .html extension)
            
        Returns:
            Rendered HTML string
            
        Raises:
            FileNotFoundError: If template doesn't exist
        """
        template_file = f"{template_name}.html"
        
        try:
            template = self.env.get_template(template_file)
        except Exception as e:
            raise FileNotFoundError(f"Template '{template_name}' not found: {e}")
        
        return template.render(**data)
    
    def generate_pdf(self, html_content: str, output_file: str) -> None:
        """Convert HTML to PDF and save to file.
        
        Args:
            html_content: HTML content to convert
            output_file: Path where PDF should be saved
            
        Raises:
            OSError: If output directory doesn't exist or isn't writable
        """
        output_path = Path(output_file)
        
        # Create output directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Convert HTML to PDF
        html_doc = HTML(string=html_content)
        html_doc.write_pdf(str(output_path))
    
    def generate_resume(self, json_file: str, output_file: str, template_name: str = "modern") -> None:
        """Generate complete resume PDF from JSON data.
        
        Args:
            json_file: Path to JSON file containing resume data
            output_file: Path where PDF should be saved
            template_name: Name of template to use
            
        Raises:
            FileNotFoundError: If JSON file or template doesn't exist
            ValueError: If JSON data is invalid
            OSError: If output cannot be written
        """
        # Load and validate JSON data
        data = self.load_json_data(json_file)
        
        # Generate HTML from template
        html_content = self.generate_html(data, template_name)
        
        # Convert to PDF
        self.generate_pdf(html_content, output_file)