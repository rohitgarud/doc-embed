"""Setup file for the doc-embed"""

from pathlib import Path

from setuptools import find_packages, setup

import versioneer

# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

DEPS = []

setup(
    name="doc-embed",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Collection of different document embedding techniques using various NLP libraries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rohitgarud/doc-embed",
    author="Rohit Garud",
    author_email="rohit.garuda1992@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords=["Document-embedding", "Natural Language Processing", "Machine Learning"],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    python_requires=">=3.6",
    install_requires=[],
    extras_require={"all": DEPS, "test": ["pytest"] + DEPS},
    project_urls={
        "Bug Reports": "https://github.com/rohitgarud/doc-embed/issues",
        "Source": "https://github.com/rohitgarud/doc-embed",
    },
)
