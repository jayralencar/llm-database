from setuptools import setup, find_packages

print(find_packages())
setup(
    name='nm-spine',
    version='0.0.0.1',
    packages=find_packages(),
    install_requires=[
        "openai",
        "instructor",
        "pydantic",
        "sqlite3"
    ]
)
