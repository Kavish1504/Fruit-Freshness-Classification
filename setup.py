from setuptools import setup, find_packages

setup(
    name="cnnClassifier",
    version="0.0.0",
    author="Kavish1504",
    author_email="kavishg36@gmail.com",
    description="Fruit Freshness Classification",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.8,<3.11",
)
