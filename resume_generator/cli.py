"""Command-line interface for resume generator using click."""

import sys
from pathlib import Path

import click

from .generator import ResumeGenerator


@click.command()
@click.option(
    '--json', 'json_file',
    required=True,
    type=click.Path(exists=True, path_type=Path),
    help='Path to JSON file containing resume data'
)
@click.option(
    '--template',
    default='modern',
    help='Template to use (default: modern)'
)
@click.option(
    '--output', 'output_file',
    required=True,
    type=click.Path(path_type=Path),
    help='Output PDF file path'
)
@click.option(
    '--templates-dir',
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    help='Custom templates directory (optional)'
)
def generate(json_file, template, output_file, templates_dir):
    """Generate a PDF resume from JSON data using HTML templates."""
    try:
        # Initialize generator
        if templates_dir:
            generator = ResumeGenerator(str(templates_dir))
        else:
            generator = ResumeGenerator()
        
        # Check if template exists
        available_templates = generator.get_available_templates()
        if template not in available_templates:
            click.echo(f"Error: Template '{template}' not found.", err=True)
            click.echo(f"Available templates: {', '.join(available_templates)}", err=True)
            sys.exit(1)
        
        # Generate resume
        click.echo(f"Generating resume using '{template}' template...")
        generator.generate_resume(str(json_file), str(output_file), template)
        
        click.echo(f"Resume generated successfully: {output_file}")
        
    except FileNotFoundError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        sys.exit(1)


@click.command()
@click.option(
    '--templates-dir',
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    help='Custom templates directory (optional)'
)
def list_templates(templates_dir):
    """List available resume templates."""
    try:
        if templates_dir:
            generator = ResumeGenerator(str(templates_dir))
        else:
            generator = ResumeGenerator()
        
        templates = generator.get_available_templates()
        
        if not templates:
            click.echo("No templates found.")
            return
        
        click.echo("Available templates:")
        for template in templates:
            click.echo(f"  - {template}")
            
    except Exception as e:
        click.echo(f"Error listing templates: {e}", err=True)
        sys.exit(1)


@click.command()
@click.argument('template_name')
@click.option(
    '--templates-dir',
    type=click.Path(exists=True, file_okay=False, path_type=Path),
    help='Custom templates directory (optional)'
)
def template_info(template_name, templates_dir):
    """Show JSON requirements and features for a specific template."""
    try:
        if templates_dir:
            generator = ResumeGenerator(str(templates_dir))
            templates_path = Path(templates_dir)
        else:
            generator = ResumeGenerator()
            package_dir = Path(__file__).parent.parent
            templates_path = package_dir / "templates"
        
        # Check if template exists
        available_templates = generator.get_available_templates()
        if template_name not in available_templates:
            click.echo(f"Error: Template '{template_name}' not found.", err=True)
            click.echo(f"Available templates: {', '.join(available_templates)}", err=True)
            sys.exit(1)
        
        # Look for documentation file
        doc_file = templates_path / f"{template_name}.md"
        
        if doc_file.exists():
            with open(doc_file, 'r', encoding='utf-8') as f:
                click.echo(f.read())
        else:
            click.echo(f"No documentation found for template '{template_name}'.")
            click.echo("This template uses the standard JSON structure:")
            click.echo(_get_basic_json_structure())
            
    except Exception as e:
        click.echo(f"Error getting template info: {e}", err=True)
        sys.exit(1)


def _get_basic_json_structure():
    """Return basic JSON structure documentation."""
    return '''
{
  "personal": {
    "name": "Your Name",
    "email": "email@example.com",
    "phone": "+1-234-567-8900",
    "location": "City, State"
  },
  "summary": "Professional summary...",
  "experience": [
    {
      "title": "Job Title",
      "company": "Company Name",
      "duration": "2020-2023",
      "description": "Job description..."
    }
  ],
  "education": [
    {
      "degree": "Degree Name",
      "school": "University Name",
      "year": "2020"
    }
  ],
  "skills": ["Skill1", "Skill2", "Skill3"]
}'''


@click.group()
def cli():
    """Resume Generator CLI - Generate professional PDF resumes from JSON data."""
    pass


# Add commands to group
cli.add_command(generate)
cli.add_command(list_templates, name='list-templates')
cli.add_command(template_info, name='template-info')


def main():
    """Main entry point for the CLI."""
    cli()


if __name__ == '__main__':
    main()