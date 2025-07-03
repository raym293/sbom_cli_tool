# Project Health Analyzer

A CLI tool for analyzing Python project dependencies, generating SBOMs, visualizing dependency/license relationships, and identifying security and license risks.

## Features
- **Dependency Analysis:**
  - Scans Python project dependencies
  - Outputs dependency tree (`dependancies.txt`)
  - Extracts license information (`licenses.txt`, `licenses.json`)
- **SBOM Generation:**
  - Generates CycloneDX and SPDX SBOMs (planned)
- **Visualization:**
  - Visualizes dependency graphs (planned)
- **Risk Analysis:**
  - Detects vulnerable and outdated packages (planned)

## Usage
1. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the main tool:**
   ```bash
   python main.py
   ```
   This will generate `dependancies.txt`, `licenses.txt`, and `licenses.json` for the current environment.

3. **Sample Project:**
   - See `sample_project/` for a minimal Flask app to test the tool.
   - To set up the sample project:
     ```bash
     cd sample_project
     python3 -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt
     ```

## Project Structure
- `main.py` – Main script for dependency and license analysis
- `setup.py` – (WIP) Script for automating venv and requirements installation
- `requirements.txt` – Tool dependencies (pipdeptree, pip-licenses, etc.)
- `dependancies.txt` – Output: dependency tree
- `licenses.txt` – Output: license table
- `licenses.json` – Output: license info (deduplicated, JSON)
- `sample_project/` – Example Python project for testing

## Requirements
- Python 3.8+
- Linux (tested)

## Planned Extensions
- SBOM generation (CycloneDX, SPDX)
- Dependency graph visualization (pydeps, Graphviz)
- Security/risk analysis (safety, pip-audit)
- CI/CD integration
- Web interface (Flask/Django)

## Limitations
- Only supports pip-based projects currently
- Some outputs (SBOM, visualization, risk analysis) are not yet implemented
- See `limitations.txt` for more details

## License
MIT
