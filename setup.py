import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easylogger",
    version="2.1.0",
    author="AARMN",
    author_email="aarmn80@gmail.com",
    description="A tiny logger , make life a little easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/public-aarmn-simple/easylogger",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
