<h1 align="center">
    Opt3001
</h1>

<h4 align="center">
    Python support library for the light sensor OPT3001 from Texas Instruments
</h4>

## Description

## Contents

- [Description](#description)
- [Contents](#contents)
- [Install](#install)
- [Usage](#usage)
- [Flight Manual](#flight-manual)
- [Development](#development)
- [Team](#team)
- [License](#license)

## Install

- sudo apt-get install -y python-smbus
- pip install opt3001

## Usage

```python
import opt3001 from opt3001

address = 0x44

opt = opt3001.OPT3001(address) 

# Configure to run in Continuous conversions mode
opt3001.write_config_reg(opt3001.I2C_LS_CONFIG_CONT_FULL_800MS)

while(True):
  print(opt3001.read_lux_float())
  time.sleep(1)
```

### Raspberry pi

Add following line to `/etc/modules` to start i2c module on startup:
``` bash
i2c_dev
```

Run following commands to start the i2c modules manually:
``` bash
$ modprobe i2c-bcm2708
$ modprobe i2c_dev
```

Install `i2c-tools` to test with the terminal

``` bash
$ sudo apt-get install i2c-tools
```

Run following command to get the address of the opt3001

``` bash
$ i2cdetect -y 1

     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- 44 -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --
```

Run the following command to test the opt30001
``` bash
$ i2cget -y 1 0x44 0x00

0x0b
```

## Flight Manual

### Constants

### OPT3001

#### constructor(address, bus = 1)

#### write_config_reg()

#### read_lux_fixpoint()

#### read_lux_float

## Development

### Build
python setup.py sdist bdist_wheel

### Upload
twine upload dist/*

## Team

- Thomas Pöhlmann [(@perryrh0dan)](https://github.com/perryrh0dan)

## Licence

[MIT](https://github.com/perryrh0dan/opt3001/blob/master/license.md)

This repository was generated by [charon](https://github.com/perryrh0dan/charon)
