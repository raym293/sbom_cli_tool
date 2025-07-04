# Project Health Analyzer

A hands-on project to learn about SBOMs, dependency graphs, and Python supply chain security by building a practical CLI tool.

---

## Objectives
- Scan and analyze Python project dependencies
- Generate SBOMs in multiple formats (CycloneDX, SPDX)
- Visualize dependency and license relationshipsError loading webview: Error: Could not register service worker: InvalidStateError: Failed to register a ServiceWorker: The document is in an invalid state..
- Identify security and license risks

---

## Implementation Plan

### 1. Dependency Analysis
**Tools:** pipdeptree, pip-licenses

- [x] Create a new Python project with a `requirements.txt`:
  ```
  flask
  blinker
  requests
  pandas
  ```
- [x] Write a script to:
  - [ ] Set up a virtual environment and install dependencies
  - [x] Run `pipdeptree` → save as `dependencies.txt`
  - [x] Run `pip-licenses` → save as `licenses.json`

### 2. SBOM Generation
**Tools:** cyclonedx-python, spdx-tools

- [ ] Extend the script to:
  - [ ] Generate a CycloneDX SBOM (`sbom.xml`)
  - [ ] Generate an SPDX SBOM (`sbom.spdx`)
  - [ ] Compare the two formats

### 3. Visualization
**Tools:** pydeps, Graphviz

- [ ] Add features to:
  - [ ] Generate a PNG dependency graph with pydeps
  - [ ] Color-code licenses (e.g., red for GPL, green for MIT)
  - [ ] Output an HTML report summarizing findings

### 4. Risk Analysis
**Tools:** safety, pip-audit

- [ ] Integrate:
  - [ ] `pip-audit` for vulnerability scanning
  - [ ] Outdated package detection
  - [ ] Highlight restrictive licenses (GPL, AGPL)

---

## Example Outputs
- **Console Report:**
  - Dependency count, outdated/vulnerable packages, restricted licenses
- **Visuals:**
  - Dependency tree diagram
  - License distribution pie chart
  - Update urgency heatmap

---

## Advanced Extensions
- Support for Poetry (`pyproject.toml`), Conda, Docker
- CI/CD integration: fail on critical issues, comment graphs on PRs, track changes
- Web interface (Flask/Django): upload requirements, view graphs, SBOM analysis

---

## Learning Outcomes
- Practical experience with SBOM and dependency tools
- Understanding of Python packaging and supply chain security
- Skills in visualization and risk analysis