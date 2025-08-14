# Classic Template

A traditional, conservative resume template with serif fonts and simple formatting.

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
  "skills": ["string", "string"] // Simple array separated by bullets
}
```

## Special Features

- **Traditional Design**: Times New Roman font, black and white
- **Conservative Layout**: Professional formatting suitable for any industry
- **Bullet Separated Skills**: Skills displayed in paragraph format with bullet separators
- **Flexbox Headers**: Job titles and dates properly aligned

## Example Usage
```bash
resume-generator generate --json my_resume.json --template classic --output resume.pdf
```