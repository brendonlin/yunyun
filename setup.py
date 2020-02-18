import io
import re
from setuptools import setup, find_packages

with io.open("Readme.md", "rt", encoding="utf8") as f:
    readme = f.read()

with io.open("yunyun/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="yunyun",
    version=version,
    author="Brendon Lin",
    author_email="brendon.lin@outlook.com",
    description="A library to help people make decisions.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["tabulate>=0.8.6"],
    entry_points={"console_scripts": ["yunyun = yunyun.think:main"]},
)
