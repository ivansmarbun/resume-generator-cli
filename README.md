# Resume Generator CLI

A Python command-line tool that generates professional PDF resumes from JSON data using HTML templates.

## Installation

```bash
pip install -e .
```

## Usage

Generate a resume:
```bash
resume-generator generate --json examples/sample_resume.json --template modern --output my_resume.pdf
```

List available templates:
```bash
resume-generator list-templates
```

## Templates

- **modern**: Clean design with blue accents and modern typography
- **classic**: Traditional serif design with conservative styling