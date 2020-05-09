import smbus

# Constants
I2C_LS_REG_RESULT = 0x00
I2C_LS_REG_CONFIG = 0x01
I2C_LS_REG_LOWLIMIT = 0x02
I2C_LS_REG_HIGHLIMIT = 0x03
I2C_LS_REG_MANUFACTURERID = 0x7E
I2C_LS_REG_DEVICEID = 0x7F

# Configdata for Register "Configuration"
I2C_LS_CONFIG_DEFAULT = 0xc810
# Bit 15..12 Automatic Full-Scale Setting Mode
# Bit 11 Conversion time field: 800ms
# Bit 10..9 Mode of conversion: Shutdown
# Bit 4 Latch field

# Configdata for Register "Configuration"
I2C_LS_CONFIG_CONT_FULL_800MS = 0xcc10
# Bit 15..12 Automatic Full-Scale Setting Mode
# Bit 11 Conversion timefield: 800ms
# 10..9 Mode of conversion: Continuous conversions
# Bit 4 Latch field

bus = None


def init(com=1):
    global bus
    bus = smbus.SMBus(com)


def read_register_16bit(address, adr):
    """ -----------------------------------------------
    Name: read_register_16bit

    Description:  reads a register of the opt3001

    Input:  address
              i2c address of the opt3001
            adr
              registeradress to read from

    Ausgang: data
    """
    values = bus.read_i2c_block_data(address, adr, 2)
    data = (values[0] << 8) | values[1]
    return data


def write_register_16bit(address, adr, data):
    """ -----------------------------------------------
    Name: write_register_16bit

    Description:  write to a register of the opt3001

    Input:  address
              i2c address of the opt3001
            adr
              registeradress to write to
            data
              data to write to register

    Ausgang: void
    """
    d1 = (data >> 8)
    d0 = data & 0xFF
    return bus.write_i2c_block_data(address, adr, [d1, d0])


def write_config_reg(address, data):
    """ -----------------------------------------------
    Name: write_config_req

    Description:  write to config register

    Input:  address
              i2c address of the opt3001
            data
              data to write to register

    Ausgang: void
    """
    return write_register_16bit(address, I2C_LS_REG_CONFIG, data)


def read_manufacture_id(address):
    """ -----------------------------------------------
    Name: read_manufacture_id

    Description:  read manufacture id of the opt3001

    Input:  address
              i2c address of the opt3001

    Ausgang: manufacture id
    """
    return read_register_16bit(address, I2C_LS_REG_MANUFACTURERID)


def read_device_id(address):
    """ -----------------------------------------------
    Name: read_device_id

    Description:  read device id of the opt3001

    Input:  address
              i2c address of the opt3001

    Ausgang: manufacture id
    """
    return read_register_16bit(address, I2C_LS_REG_DEVICEID)


def read_lux_fixpoint(address):
    """ -----------------------------------------------
    Name: read_lux_fixpoint

    Description:  read the brightness of the opt3001 with two fixed decimal places

    Input:  address
              i2c address of the opt3001

    Ausgang: manufacture id
    """
    # Register Value
    req_value = read_register_16bit(address, I2C_LS_REG_RESULT)

    # Convert to LUX
    mantisse = req_value & 0x0fff
    exponent = (req_value & 0xf000) >> 12

    return 2**exponent * mantisse  # mantisse << exponent;


def read_lux_float(address):
    """ -----------------------------------------------
    Name: read_lux_float

    Description:  read the brightness of the opt3001 as float

    Input:  address
              i2c address of the opt3001

    Ausgang: manufacture id
    """
    # Register Value
    req_value = read_register_16bit(address, I2C_LS_REG_RESULT)

    # Convert to LUX
    mantisse = req_value & 0x0fff
    exponent = (req_value & 0xf000) >> 12

    return 2**exponent * mantisse * 0.01  # mantisse << exponent * 0.01;
