Mermaid Support

This repository includes a small helper to render Mermaid diagrams found in
Markdown files into SVG images.

Options

- Quick (VS Code): Install the "Markdown Preview Mermaid Support" or
  "Markdown Preview Enhanced" extension in VS Code to render Mermaid
  diagrams directly in the editor preview.

- Command-line (recommended for project-generated diagrams):

  1. Install Node.js (if not already installed).
  2. From the repo root run:

```powershell
npm install
npm run render-mermaid
```

  The script will scan `.md` files, render any ```mermaid blocks into SVGs
  under `diagrams/mermaid_generated/` and print suggested image links to
  place into your Markdown.

Notes

- The renderer uses `@mermaid-js/mermaid-cli` via `npx`. First run may take
  longer while dependencies are installed.
- The script will not modify your Markdown files automatically; it only
  generates images and suggests links so you can review before committing.
