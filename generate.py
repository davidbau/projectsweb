#!/usr/bin/env python3
"""
Generate static HTML from template and YAML data using Jinja2.
Install dependencies with: `pip install jinja2 pyyaml` or run `uv sync`.
"""

import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def generate_site():
    # Read and parse the projects YAML file
    with open('projects.yaml', 'r', encoding='utf-8') as f:
        projects = yaml.safe_load(f)

    # Set up Jinja2 environment to load templates from current directory
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Render the template with project data
    final_html = template.render(projects=projects)

    # Ensure the public directory exists
    Path('public').mkdir(exist_ok=True)

    # Write the final HTML to the public directory
    with open('public/index.html', 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"✅ Successfully generated public/index.html")
    print(f"📄 Generated HTML for {len(projects)} project(s)")


if __name__ == "__main__":
    try:
        generate_site()
    except Exception as e:
        print(f"❌ Error generating site: {e}")
        exit(1)
