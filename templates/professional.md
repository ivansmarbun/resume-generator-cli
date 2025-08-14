# Professional Template

A clean, professional resume template with sections for experience, education, skills, and social links.

## Required JSON Fields

### Basic Structure
```json
{
  "personal": {
    "name": "string (required)",
    "title": "string (optional)",
    "email": "string (required)", 
    "phone": "string (required)",
    "location": "string (optional)",
    "websites": [
      {
        "name": "string",
        "url": "string"
      }
    ]
  },
  "summary": "string (optional)",
  "experience": [
    {
      "title": "string (required)",
      "company": "string (required)",
      "duration": "string (required)",
      "location": "string (optional)",
      "bullets": ["string", "string"] // Use either bullets OR description
      "description": "string (optional)"
    }
  ],
  "education": [
    {
      "degree": "string (required)",
      "school": "string (required)", 
      "year": "string (required)",
      "gpa": "string (optional)"
    }
  ],
  "skills": [
    {
      "name": "string (required)",
      "rating": "integer 1-5 (optional)"
    }
  ]
}
```

## Special Features

- **Bullet Points**: Use `bullets` array in experience for bulleted lists
- **Star Ratings**: Use `rating` field in skills (1-5 stars)
- **Social Links**: Use `websites` array in personal section
- **GPA Display**: Include `gpa` field in education to show GPA

## Example Usage
```bash
resume-generator generate --json my_resume.json --template professional --output resume.pdf
```