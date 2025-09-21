# Project Website Generator

A simple Python script to generate a static project listing website from YAML data and an HTML template.

## Quick Start

1. Install dependencies:
   ```bash
   pip install jinja2 pyyaml
   ```

   Or install from requirements file:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the generator:
   ```bash
   python generate.py
   ```

3. The generated HTML will be saved to `public/index.html`

## How it Works

The script reads:
- `template.html` - The base HTML template with Bootstrap styling
- `projects.yaml` - Project data including names, URLs, descriptions, authors, etc.

It then uses Jinja2 templating to generate HTML for each project and inserts it into the template where the `<!--Insert content here-->` comment is located.

## Project Data Format

Each project in `projects.yaml` should have the following structure:

```yaml
- name: Project Name
  image: /path/to/image.png
  project_url: https://project-name.baulab.info/
  paper_title: "Project Name: Full Paper Title"
  paper_url: https://arxiv.org/abs/xxxx.xxxxx
  conference_name: Conference Name
  authors:
    - Author One
    - Author Two
    - D Bau  # This author will be highlighted
  description: |
    Main project description text...
  extra: |
    Additional details that appear when expanded...
```

Remember to add quotations around any fields that have colons or other YAML restricted characters.

The `description` and `extra` fields can contain some simple HTML (links, etc.) that will be sanitized to remove any potentially harmful code.

Some of the fields are optional and can be omitted:

```yaml
- name: Simple Project
  project_url: https://project.com
  description: Just a description...
  authors: [Author1]
```

## Generated HTML Structure

Each project generates a paragraph (`<p>`) with:
- Project image with `class="projpic"`
- Project link with the name
- Description text
- Expandable "more" section with extra details
- Paper citation with authors, title, and venue

The "D Bau" author is automatically wrapped in `<span class="me">` for highlighting.

## Customization

- Modify `template.html` to change the overall page structure and styling
- Edit the project template in `generate.py` to change how individual projects are rendered
- Add new projects by editing `projects.yaml`

## Dependencies

- Python 3.6+
- Jinja2 (templating engine)
- PyYAML (YAML parsing)
