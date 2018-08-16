# zs-preflight
A preflight checklist script that will help an admin determine if the hardware they want to use for Zerostack is compatible.

This is an automated preflight checklist that will work on a base ubuntu OS (14.04,16.04), and requires a minimum of python 2.7.

The preflight check will ensure that your physical server will work with the Zerostack ZCOS. Once this script is run, and
all of the checks are varified, you will be able to install the ZCOS.

The preflight check will make sure the following adhears to the Zerostack minimal viable hardware spec.

1. Overall system configuration
2. CPU architecture
3. Storage requierments
4. Networking

Please check the Ubuntu HCL to verify your results.
[Ubuntu Server HCL](https://certification.ubuntu.com/server/)

Once all of the results have been verified, please send your output file to support@zerostack.com

Install
GIT - development / nightly
* git clone https://github.com/JonathanArrance/zsdev.git
* cd zspreflight
* python setup.py

PIP - test build
python -m pip install --index-url https://test.pypi.org/simple/ zspreflight

PIP - stable build
pip install zspreflight

Operation
$ python ~/.local/lib/python2.7/site-packages/zspreflight/preflight.py
