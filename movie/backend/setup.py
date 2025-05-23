from setuptools import setup, find_packages

setup(
    name="backend",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Flask>=2.0.0",
        "flask_cors>=3.0.0",  # Ensure this line has a comma at the end
    ],
    extras_require={
        "dev": ["pytest", "flake8"]
    },
)  # Ensure only one closing parenthesis here
