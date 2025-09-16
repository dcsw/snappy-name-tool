#!/usr/bin/env python3
"""
SBOM Generator for s14l project
Generates a CycloneDX SBOM from project dependencies
"""

import json
import subprocess
import sys
from pathlib import Path

def get_python_version():
    """Get Python version information"""
    version = sys.version_info
    return f"{version.major}.{version.minor}.{version.micro}"

def get_standard_libs():
    """Get list of standard library modules"""
    return list(sys.builtin_module_names)

def generate_sbom():
    """Generate CycloneDX SBOM"""
    sbom = {
        "bomFormat": "CycloneDX",
        "specVersion": "1.4",
        "serialNumber": "urn:uuid:3e671683-40d8-4a8f-9e5b-8a5a3a7b3e7b",
        "version": 1,
        "components": []
    }
    
    # Add Python runtime as a component
    python_component = {
        "type": "platform",
        "name": f"Python {get_python_version()}",
        "version": get_python_version(),
        "purl": "pkg:python/python",
        "externalReferences": [
            {
                "type": "documentation",
                "url": "https://www.python.org/"
            }
        ]
    }
    sbom["components"].append(python_component)
    
    # Add the s14l application itself
    app_component = {
        "type": "application",
        "name": "s14l",
        "version": "0.1.0",
        "purl": "pkg:pypi/s14l@0.1.0",
        "licenses": [{"license": {"name": "MIT"}}],
        "externalReferences": [
            {
                "type": "documentation",
                "url": "https://github.com/dcsw/snappy-name-tool"
            }
        ]
    }
    sbom["components"].append(app_component)
    
    # Add standard library dependencies
    std_libs = get_standard_libs()
    for lib in sorted(std_libs)[:20]:  # Limit to first 20 to keep SBOM manageable
        lib_component = {
            "type": "library",
            "name": lib,
            "version": get_python_version(),
            "purl": f"pkg:python/{lib}@{get_python_version()}",
            "scope": "required"
        }
        sbom["components"].append(lib_component)
    
    # Write SBOM to file
    with open("sbom.json", "w") as f:
        json.dump(sbom, f, indent=2)
    
    print("SBOM generated successfully: sbom.json")

if __name__ == "__main__":
    generate_sbom()
