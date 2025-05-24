from setuptools import setup, find_packages

# Constant for editable install flag in requirements
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path):
    """
    Reads a requirements file and returns a list of requirements,
    removing the editable install flag if present.
    """
    requirements = []
    with open(file_path, "r") as f:
        requirements = f.readlines()
        # Remove newline characters from each requirement
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

# Read the long description from README.md
with open("README.md", "r", encoding="UTF-8") as f:
    long_description_text = f.read()

# Setup configuration for the package
setup(
    name="Database_Connector",  # Package name
    version="0.0.1",  # Initial version
    author="Saurav Sabu",  # Author name
    author_email="saurav.sabu9@gmail.com",  # Author email
    description="python package to connect with database",  # Short description
    long_description=long_description_text,  # Long description from README
    long_description_content_type="text/markdown",  # Content type for long description
    url="https://github.com/saurav-sabu/Database_Connector",  # Project URL
    project_urls={
        "Bug Tracker": "https://github.com/saurav-sabu/Database_Connector/issues"
    },  # Additional project URLs
    package_dir={"": "src"},  # Source directory for packages
    packages=find_packages(where="src"),  # Find all packages in src
    install_requires=get_requirements("requirements_dev.txt")  # Install dependencies
)