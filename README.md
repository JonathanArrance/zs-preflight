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

## Install
### GIT - development / nightly
1. git clone https://github.com/Zerostack-open/zs-preflight.git
2. cd zspreflight
3. python setup.py bdist_wheel

### PIP - Development
1. sudo python -m pip install --upgrade pip setuptools wheel
2. sudo python -m pip install tqdm
3. sudo python -m pip install --user --upgrade twine

### PIP - test build
Upload to Test PIP

1. $ twine upload --repository-url https://test.pypi.org/legacy/ dist/*
2. $ python -m pip install --index-url https://test.pypi.org/simple/ zs-preflight

### PIP - stable build

* $ pip install zs-preflight

### Operation

1. $ zspreflight
2. Say yes to run the test.
3. Add in the IP, Username, and password of the hosts you want to check.
4. Let the test run and check the output