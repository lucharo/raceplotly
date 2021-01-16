import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="raceplotly",
    version="0.1.4",
    author="Luis Chaves",
    author_email="lc5415@ic.ac.uk",
    description="Tiny package to make 'race' barplots using plotly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lc5415/raceplotly",
    packages=setuptools.find_packages(),
    setup_requires=["numpy"],
    install_requires=[
        "pandas",
        "numpy < 1.20" if sys.version_info < (3, 7) else "numpy",
        "plotly",
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)