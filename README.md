# Resume Generator CLI

A Python command-line tool that generates professional PDF resumes from JSON data using HTML templates.

## Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

## Quick Start

Generate a resume using the professional template:
```bash
resume-generator generate --json examples/professional_resume.json --template professional --output my_resume.pdf
```

## Commands

### Generate Resume
```bash
resume-generator generate --json <json_file> --template <template_name> --output <output_file>
```

### List Available Templates
```bash
resume-generator list-templates
```

### Get Template Information
```bash
resume-generator template-info <template_name>
```

## Templates

- **modern**: Clean design with blue accents, pill-shaped skills, and modern typography
- **classic**: Traditional serif design with conservative black & white styling
- **professional**: Advanced template with bullet points, star ratings, social links, and GPA support

### Template-Specific Features

Each template supports different JSON structures. Use `resume-generator template-info <template>` to see requirements:

```bash
resume-generator template-info professional  # Shows JSON structure and features
resume-generator template-info modern        # Shows modern template requirements
resume-generator template-info classic       # Shows classic template requirements
```

## Examples

The `examples/` directory contains sample JSON files:
- `sample_resume.json` - Basic structure for modern/classic templates
- `professional_resume.json` - Advanced structure with all professional template features

## JSON Structure

Basic structure supported by all templates:
```json
{
  "personal": {
    "name": "Your Name",
    "email": "email@example.com",
    "phone": "+1-234-567-8900",
    "location": "City, State"
  },
  "summary": "Professional summary...",
  "experience": [...],
  "education": [...],
  "skills": [...]
}
```

For template-specific requirements and advanced features, use the `template-info` command.