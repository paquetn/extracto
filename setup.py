from setuptools import setup, find_packages

setup(
    name="extracto",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "extracto=extracto.extract_structure:main",
        ],
    },
    install_requires=[],
    author="Nicolas Paquet",
    author_email="nick@averagecadmanager.ca",
    description="A tool to extract folder structure and save it as a JSON file.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/folder_structure_extractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
