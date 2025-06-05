# setup.py - Package configuration

from setuptools import setup, find_packages

setup(
    name="simple-calculator",
    version="1.0.0",
    description="A simple calculator for Jenkins CI/CD demonstration",
    author="Your Name",
    author_email="your.email@example.com",
    py_modules=["main"],
    python_requires=">=3.6",
    install_requires=[
        # Add runtime dependencies here if needed
    ],
    extras_require={
        "dev": [
            "flake8>=5.0.0",
            "black>=22.0.0",
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "console_scripts": [
            "simple-calc=main:main",
        ],
    },
)
