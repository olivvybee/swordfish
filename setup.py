import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="swordfish",
    version="0.0.1",
    author="Liv Asch",
    author_email="olivia.c.asch@gmail.com",
    description="Library for displaying 3D printer status on an OLED display",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olivvysaur/swordfish",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
