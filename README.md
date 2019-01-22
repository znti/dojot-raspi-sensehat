# Raspberry Pi + Sense Hat and dojot
This project aims to provide a simple way of integrating the data collected by raspberry pi and [sense hat](https://www.raspberrypi.org/products/sense-hat/) combination, storing all the values on the [dojot IoT platform](www.dojot.com.br).

This codebase utilizes the [SenseEmu](https://sense-emu.readthedocs.io/en/v1.1/) emulator to simplify access to those who doesn't have the actual hardware.

## Executing the code on an emulator

### Install the emulator packages

The first step is to install the tools provided by the SenseEmu team. The instructions can be found on the [installation document](https://sense-emu.readthedocs.io/en/v1.1/install.htm).

The following commands are needed

```
sudo add-apt-repository ppa://waveform/ppa
sudo apt-get update
sudo apt-get install python-sense-emu python3-sense-emu sense-emu-tools
```

### Install the project dependencies

After checking out the code, install the packages listed on [requirements.txt](https://github.com/znti/dojot-raspi-sensehat/blob/master/requirements.txt) file.
Use pip3 to do so:

`pip3 install -r ./requirements.txt`

After installation is complete, you can already execute the main code:

`python3 main.py`

## Deploy to a raspberry pi
On the [main.py file]:

Change `from sense_emu import SenseHat` to `from sense_hat import SenseHat`
