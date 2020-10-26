import setuptools


# Required packages
REQUIRED = ["numpy", "pandas", "sklearn"]

# Grabs description from README as our long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-hcmead",
    version="0.0.3",
    author="hcmead",
    description="A collection of data science functions",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Explains type of format long description has
    url="https://github.com/hmead15/lambdata",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Version of python we are running
)