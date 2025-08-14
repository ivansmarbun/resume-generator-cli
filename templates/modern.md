# Modern Template

A modern, clean resume template with colored accents and pill-shaped skill tags.

## Required JSON Fields

### Basic Structure
```json
{
  "personal": {
    "name": "string (required)",
    "email": "string (required)", 
    "phone": "string (required)",
    "location": "string (required)"
  },
  "summary": "string (optional)",
  "experience": [
    {
      "title": "string (required)",
      "company": "string (required)",
      "duration": "string (required)",
      "description": "string (required)"
    }
  ],
  "education": [
    {
      "degree": "string (required)",
      "school": "string (required)", 
      "year": "string (required)"
    }
  ],
  "skills": ["string", "string"] // Simple array of skill names
}
```

## Special Features

- **Colored Design**: Blue accent colors and borders
- **Pill Skills**: Skills displayed as rounded pill-shaped tags
- **Right-aligned Dates**: Duration and years aligned to the right
- **Clean Typography**: Modern Arial font with good spacing

## Example Usage
```bash
resume-generator generate --json my_resume.json --template modern --output resume.pdf
```