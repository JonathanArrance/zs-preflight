import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zspreflight",
    version="0.0.3",
    author="Jonathan Arrance",
    author_email="jonathan@zerostack.com",
    description="The Zerostack preflight check will validate if your hardware is Zerostack ready.",
    long_description=long_description,
    url="https://github.com/Zerostack-open/zs-preflight.git",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
