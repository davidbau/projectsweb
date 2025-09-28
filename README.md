# Project Website

David Bau's lab project list website.

This repo uses a simple Python script to generate the Bau Lab projects website from YAML data and an HTML template.

## Regenerating Website
Ensure you have Python 3 and uv installed. Then:

1. Install dependencies:

   Use either uv to set up a local venv:
   ```bash
   uv sync
   source .venv/bin/activate
   ```

   Or pip:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the generator:
   ```bash
   python generate.py
   ```

3. The generated HTML will be saved to `public/index.html`. **Make sure you check in everything in `public`, and add any other pictures, etc. that you want to include.**

## Adding Projects
Add projects in the `projects.yaml` file. Some of the fields are optional and can be omitted. Try to have at minimum:

```yaml
- name: Sample Project
  project_url: https://project-url.baulab.info/
  paper_url: "#" # link that goes nowhere for now
  description: Just a description...
  authors: [Author1]
```

A full project can have the following:

```yaml
- name: Project Name
  image_url: /image.png
  project_url: https://project-url.baulab.info/
  paper_title: "Project Name: Full Paper Title"
  paper_url: https://arxiv.org/abs/xxxx.xxxxx
  conference_name: Workshop or Conference Name, Year, etc.
  authors:
    - Author One
    - Author Two
    - D Bau # This exact spelling will be highlighted
  description: |
    Main project description text...
  extra: |
    Additional details that appear when expanded...
```

Remember to add quotations around any fields that have colons or other YAML restricted characters.

The `description` and `extra` fields can contain some simple HTML (links, etc.) that will be sanitized to remove any potentially harmful code.
