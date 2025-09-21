# Project Website Generator

A simple Python script to generate the Bau Lab projects website from YAML data and an HTML template.

## Quick Start
Ensure you have Python 3 installed. Then:

1. Install dependencies:

   Use either uv:
   ```bash
   uv sync
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
  description: Just a description...
  authors: [Author1]
```

A full project can have the following:

```yaml
- name: Project Name
  image: /image.png
  project_url: https://project-url.baulab.info/
  paper_title: "Project Name: Full Paper Title"
  paper_url: https://arxiv.org/abs/xxxx.xxxxx
  conference_name: Workshop or Conference Name, Year, etc.
  authors:
    - Author One
    - Author Two
    - D Bau
  description: |
    Main project description text...
  extra: |
    Additional details that appear when expanded...
```

Remember to add quotations around any fields that have colons or other YAML restricted characters.

The `description` and `extra` fields can contain some simple HTML (links, etc.) that will be sanitized to remove any potentially harmful code.
