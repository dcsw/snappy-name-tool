# s14l - Name Shortener

## Description
A simple tool that shortens names by taking the first letter, counting non-whitespace characters, and appending the last letter, rendering names strings like "k8s" for "kubernetes" and similar.

## How to use

For example: "John Doe" becomes "j5e" when running:
```
s14l.py "John Doe"
```
...or (if your python is somewhere else than /usr/bin/python), use this:

```
python s14l.py "John Doe"
```
...or even:
```
<full path to python> s14l.py "John Doe"
```

Both of these return the same results:
```
j5e
```

### Multiple Names
Shorten multiple names using spaces as follows:
```
s14l.py "Jane Doe" "Alice Doe"
```
This returns:
```
j5e
a6e
```

### Names with Spaces
Note that the names in the examples above have spaces in their names and that each are surrounded by quotation marks to allow the whole name to be shortened.

Omitting the quotation marks will process each word as a name as follows:
```
j2e
d1e
a3e
d1e
```
Using quotaton marks around names with spaces will yield results as above.

## Installation
### Prerequisites
This project's only requirements are Python v3.8 or higher.
Once python is installed, no additonal installs are required.

## CI/CD Pipeline
This project uses GitHub Actions for continuous integration and deployment. The CI/CD pipeline is triggered on:

- Push to the `main` branch
- Pull requests targeting the `main` branch

### Pipeline Steps
1. **Code Checkout**: The latest code is checked out from the repository
2. **Python Setup**: Python is installed and configured
3. **Dependency Installation**: Project dependencies are installed from `requirements.txt`
4. **Test Execution**: Unit tests are run using `python -m unittest discover -s .`
5. **SBOM Generation**: A Software Bill of Materials (SBOM) is generated using the `generate_sbom.py` script
6. **Artifact Upload**: The generated SBOM is uploaded as a build artifact for download

### Artifacts
After each pipeline run, the SBOM (`sbom.json`) is available as an artifact that can be downloaded from the Actions tab in the GitHub repository.

## SBOM (Software Bill of Materials)
This project includes an SBOM (Software Bill of Materials) to provide transparency about its dependencies and components.

### Generating SBOM
To generate an SBOM for this project, run:
```
python scripts/generate_sbom.py
```

This will create a `sbom.json` file in the project root containing a CycloneDX-formatted SBOM.

### SBOM in CI
The SBOM is automatically generated during CI/CD pipeline runs and is available as an artifact for download.

### SBOM Contents
The generated SBOM (`sbom.json`) contains the following components:

1. **Python Runtime**: The Python interpreter is listed as a platform component with version information and documentation links.

2. **s14l Application**: The main application component with metadata including:
   - Type: Application
   - Name: s14l
   - Version: 0.1.0
   - Package URL (purl): pkg:pypi/s14l@0.1.0
   - License: MIT
   - Documentation link to the GitHub repository

3. **Standard Library Modules**: A selection of Python standard library modules (limited to the first 20 for manageability) are included as library components with:
   - Type: Library
   - Scope: Required
   - Version matching the Python runtime
   - Package URLs using the Python package naming convention

The SBOM follows CycloneDX specification 1.4 and provides a comprehensive view of the software components used in this project, enabling better supply chain security and dependency management.