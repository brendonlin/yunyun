from setuptools import setup, find_packages

setup(
    name="yunyun",
    version="0.1.1",
    author="Brendon Lin",
    author_email="brendon.lin@outlook.com",
    description="A library to help people make decisions.",
    packages=find_packages(),
    install_requires=["tabulate>=0.8.6"],
    entry_points={"console_scripts": ["yunyun = yunyun.think:main"]},
)
