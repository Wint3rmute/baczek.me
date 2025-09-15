# Copilot Instructions for baczek.me

## Application Goal
Personal website and digital garden that creates semantic connections between blog posts and thoughts. The site automatically generates interactive visual maps showing relationships between content using machine learning.

## Architecture

### Frontend (Static Site)
- **Zola** static site generator - processes Markdown content files
- **Templates** in `templates/` define page layouts
- **Static assets** in `static/` (CSS, JS, images)
- **Content** in `content/` as Markdown files with frontmatter

### Backend (Content Processing)
- **Python package `exocortex`** - processes content before site generation
- **Sentence embeddings** via `sentence-transformers` to analyze post similarity
- **UMAP** for dimensionality reduction of embeddings
- **Graphviz** generates SVG maps of content relationships
- **RSS feed generation** and recent posts tracking

### Build Pipeline
1. `poetry run python -m exocortex` - processes content and generates maps
2. `zola build` - generates static site in `public/`

## Key Development Guidelines

### Project Structure
- Content files: `content/*.md` - blog posts and pages
- Backend logic: `exocortex/` Python package
- Build scripts: `scripts/build.sh`, `scripts/build_docker.sh`
- Config: `config.toml` (Zola), `pyproject.toml` (Python deps)

### Code Style
- Python: Use Ruff for linting and formatting
- Follow existing patterns in `exocortex/` modules
- Keep content processing separate from site generation

### Dependencies
- Use Poetry: `poetry add <package>` for new Python deps
- Main deps include: `sentence-transformers`, `umap-learn`, `graphviz`, `matplotlib`
- Dev deps: `ruff` for code quality

## Testing Requirements (AI Agents)

Before completing work, ensure these checks pass:

### Python Code Quality
```bash
poetry run ruff format --check .    # Code formatting
poetry run ruff check --select I .  # Import sorting  
poetry run ruff check .              # Linting
```

### Build Validation
```bash
poetry run python -m exocortex      # Content processing succeeds
zola build                           # Static site generation succeeds
```

### Manual Verification
- New content appears correctly in generated site
- Semantic maps render without errors (check SVGs in `static/`)
- RSS feed validates if content changes affect it
- Visual inspection of any UI changes

### Docker Build (if system changes)
```bash
./scripts/build_docker.sh           # Full containerized build
```

Always test the complete build pipeline when modifying the backend processing logic or content structure.