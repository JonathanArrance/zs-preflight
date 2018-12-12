# ZeroStack preflight system check

The ZeroStack pre-flight system check can be used by an administrator or ZeroStack SE to determine if the hardware in question is compatible with the ZeroStack cloud operating system.
<br />

The preflight check will ensure that your physical server will work with the Zerostack ZCOS. Once this script is run, and
all of the checks are varified, you will be able to install the ZCOS.
<br />

The preflight check will make sure the hardware adhears to the Zerostack minimal viable hardware spec.
<br />

1. Overall system configuration
2. CPU architecture
3. Storage requierments
4. Networking
<br />

Please check the Ubuntu HCL to verify your results.
[Ubuntu Server HCL](https://certification.ubuntu.com/server/)
<br />

Once all of the results have been verified, please send them to your SE.
<br />

## Getting Started

In order to get the preflight check working, you will need to make sure python 2.7 or 3.x is installed on the system the preflight check will run on.
<br />

PIP will also be requierd in order to install zs-precheck and the supporting packages.
<br />

### Prerequisites

In order to get the zspreflight system working you will need to install the following packages on the sytstem you are running the preflight check from.
<br />

$ pip install paramiko
<br />
$ pip install gspread
<br />
$ pip install oauth2client

### Installing

To install the preflight check on the system, follow these steps. Make sure all of the pre-requisite packages have been installed.
<br />

$ pip install zs-preflight

## Running the tests

Run the pre-flight check with the following command.
<br />

$ preflight

## Deployment

Add additional notes about how to deploy this on a live system

## Build and submit
### GIT - development / nightly

1. git clone https://github.com/Zerostack-open/zs-preflight.git
2. cd zspreflight
3. python setup.py bdist_wheel

### PIP - Development

1. sudo python -m pip install --upgrade pip setuptools wheel
2. sudo python -m pip install tqdm
3. sudo python -m pip install --user --upgrade twine

### TODO
1. Upload data to Gsheet
2. Fire off preflight from zspreflight on a remote system

## Authors

* **Jonathan Arrance** - *Initial work* - [Zerostack-open](https://github.com/Zerostack-open)

See also the list of [contributors](https://github.com/JonathanArrance) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details