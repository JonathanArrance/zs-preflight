import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zs-preflight",
    version="0.0.5b",
    scripts=['zspreflight/zspreflight','zspreflight/preflight'] ,
    author="Jonathan Arrance",
    author_email="jonathan@zerostack.com",
    description="The ZeroStack preflight check will validate if your hardware is ZeroStack ready.",
    long_description=long_description,
    url="https://github.com/Zerostack-open/zs-preflight.git",
    packages=setuptools.find_packages(),
    install_requires=[
          'paramiko',
          'gspread',
          'oauth2client'
      ],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
