from setuptools import setup, find_packages

setup(
    name="hinglishswd",
    version="0.1.0",
    description="A Python library for Hinglish (Hindi+English code-mixed) NLP: detection, tokenization, transliteration, stop-word removal.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="ICICI Project",
    packages=find_packages(),
    install_requires=[
        "indic-transliteration>=2.0.0",
    ],
    extras_require={
        "spacy": ["spacy>=3.0.0"],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Linguistic",
    ],
)
