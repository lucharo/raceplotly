from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

    
    
setup(
    name="raceplotly",
    version="0.1.1",
    author="Luis Chaves",
    author_email="lc5415@ic.ac.uk",
    description="Tiny package to make 'race' barplots using plotly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lc5415/raceplotly",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'plotly',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
