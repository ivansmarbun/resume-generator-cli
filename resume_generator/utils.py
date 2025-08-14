"""Utility functions for resume generator."""

import json
import sys
from pathlib import Path
from typing import Dict, Any


def validate_json_file(json_file: str) -> bool:
    """Validate JSON file structure for resume data.
    
    Args:
        json_file: Path to JSON file to validate
        
    Returns:
        True if valid, False otherwise
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check required fields
        if 'personal' not in data:
            print("Error: Missing 'personal' section in JSON", file=sys.stderr)
            return False
        
        personal = data['personal']
        required_personal = ['name', 'email']
        
        for field in required_personal:
            if field not in personal:
                print(f"Error: Missing required personal field '{field}'", file=sys.stderr)
                return False
        
        print("JSON file is valid!")
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found", file=sys.stderr)
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error validating JSON: {e}", file=sys.stderr)
        return False


def print_json_structure() -> None:
    """Print example JSON structure for resume data."""
    example = {
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
    
    print("Example JSON structure:")
    print(json.dumps(example, indent=2))


def main():
    """Command line utility for validation."""
    if len(sys.argv) != 3:
        print("Usage: python -m resume_generator.utils <command> <file>")
        print("Commands:")
        print("  validate <file>  - Validate JSON file structure")
        print("  example          - Show example JSON structure")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "validate":
        json_file = sys.argv[2]
        if validate_json_file(json_file):
            sys.exit(0)
        else:
            sys.exit(1)
    elif command == "example":
        print_json_structure()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()