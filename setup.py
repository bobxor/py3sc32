from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="py3ssc32", 
    version="0.0.1",
    author="Robert McManus",
    author_email="robert.mcmanus@gmail.com",
    description="A Python 3 version of the PySSC32 ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bobxor/py3ssc32",
#    packages=setuptools.find_packages(),
	packages=['py3ssc32'],
	zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
