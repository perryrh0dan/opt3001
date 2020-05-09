import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="opt3001",
    version="1.0.4",
    author="Thomas Poehlmann",
    author_email="thomaspoehlmann96@googlemail.com",
    description="Support library for the light sensor OPT3001 from Texas Instruments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/perryrh0dan/opt3001",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
