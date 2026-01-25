from setuptools import setup, find_packages

setup(
    name="cnnClassifier",
    version="0.0.0",
    author="Kavish1504",
    author_email="kavishg36@gmail.com",
    description="Fruit Freshness Classification",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8,<3.14",
)