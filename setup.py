import pathlib
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

# The directory containing this file
ROOT_DIR = pathlib.Path(__file__).parent

# The text of the README file
README = (ROOT_DIR / "README.md").read_text()


setup(
    name="makewords",
    long_description=README,
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    entry_points={"console_scripts": ["makewords=makewords.__main__:main"]},
    version="0.1.0",
)
