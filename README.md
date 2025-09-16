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
