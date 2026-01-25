import setuptools

# Try to read README, but don't fail if it doesn't exist
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Fruit Freshness Classification using CNN"

__version__ = "0.0.0"
REPO_NAME = "Fruit-Freshness-Classification"
AUTHOR_USER_NAME = "Kavish1504"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "kavishg36@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Fixed typo: content_type not content
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8,<3.13",  # Added Python version constraint
    install_requires=[  # Added dependencies
        'Flask',
        'Flask-Cors',
        'tensorflow',
        'numpy',
        'Pillow',
        'python-box',
        'PyYAML',
    ]
)