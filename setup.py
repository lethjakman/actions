import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="actions",
    version="0.0.1",
    author="Alexander Kardos",
    description="A package that allows for actions to be added to a database and parsed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
)
