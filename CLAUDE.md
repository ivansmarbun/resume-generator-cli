# Resume Generator CLI

A Python command-line tool that generates professional PDF resumes from JSON data using HTML templates.

## Project Structure

```
resume-generator-cli/
├── resume_generator/
│   ├── __init__.py
│   ├── cli.py          # Main CLI interface using click
│   ├── generator.py    # Core resume generation logic
│   └── utils.py        # Helper functions
├── templates/
│   ├── modern.html     # Sample HTML template
│   └── classic.html    # Alternative template
├── examples/
│   └── sample_resume.json  # Example JSON data
├── requirements.txt
├── setup.py
├── CLAUDE.md           # This file
└── README.md
```

## Features

- JSON-driven data input
- Multiple HTML template support
- PDF output generation
- Command-line interface
- Print-optimized templates
- Professional PDF formatting

## Dependencies

- **Jinja2**: Template rendering
- **click**: CLI framework
- **weasyprint**: HTML to PDF conversion

## Development Commands

### Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

### Usage
```bash
# Generate resume from JSON
resume-generator --json examples/sample_resume.json --template modern --output my_resume.pdf

# Use default template
resume-generator --json my_data.json --output resume.pdf

# List available templates
resume-generator --list-templates
```

### Testing
```bash
# Test with sample data
resume-generator --json examples/sample_resume.json --output test_output.pdf

# Validate JSON structure
python -m resume_generator.utils validate examples/sample_resume.json
```

## Implementation Plan

1. ✅ Create CLAUDE.md documentation file
2. ✅ Setup project structure (directories and __init__.py files)
3. ✅ Create requirements.txt with dependencies
4. ✅ Create setup.py for package installation
5. ✅ Create HTML templates with PDF-optimized CSS
6. ✅ Implement core generator logic with Jinja2 and WeasyPrint
7. ✅ Develop CLI interface using click
8. ✅ Create sample JSON resume data
9. ✅ Test with various inputs and validate PDF output

**Project Complete!** The resume generator CLI is fully functional with:
- Two professional templates (modern & classic)
- JSON validation and error handling
- Command-line interface with help documentation
- PDF generation from HTML templates
- Package installation and console script entry points

## JSON Structure Example

```json
{
  "personal": {
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+1-234-567-8900",
    "location": "City, State"
  },
  "summary": "Professional summary here...",
  "experience": [
    {
      "title": "Software Engineer",
      "company": "Tech Corp",
      "duration": "2020-2023",
      "description": "Job responsibilities and achievements..."
    }
  ],
  "education": [
    {
      "degree": "Bachelor of Science in Computer Science",
      "school": "University Name",
      "year": "2020"
    }
  ],
  "skills": ["Python", "JavaScript", "SQL"]
}
```