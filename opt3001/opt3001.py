import smbus

# Constants
I2C_LS_REG_RESULT = 0x00
I2C_LS_REG_CONFIG = 0x01
I2C_LS_REG_MANUFACTURERID = 0x7E
I2C_LS_REG_DEVICEID = 0x7F

I2C_LS_CONFIG_CONT_FULL_800MS = 0xcc10 # Configdata for Register "Configuration"
                                       # Bit 15..12 Automatic Full-Scale Setting Mode 
                                       # Bit 11 Conversion timefield: 800ms# Erzeugen einer I2C-Instanz und Öffnen des Busses Bit
                                       # 10..9 Mode of conversion: Continuous conversionsbus = smbus.SMBus(1)
                                       # Bit 4 Latch fieldtime.sleep(1)

bus = smbus.SMBus(1)

def read_register_16bit(address, adr):
    values = bus.read_i2c_block_data(address, adr, 2)
    data = (values[0] << 8) | values[1] 
    return data

def write_register_16bit(address, adr, data):
    d1 = (data >> 8)
    d0 = data & 0xFF
    return bus.write_i2c_block_data(address, adr, [d1, d0])

def write_config_reg(address, data):
    return write_register_16bit(address, I2C_LS_REG_CONFIG, data)

def read_lux(address):
    # Register Value
    req_value = read_register_16bit(address, I2C_LS_REG_RESULT)
    print("REQ_VALUE: " + str(req_value))
    print("REQ_VALUE_HEX: " + hex(req_value))
 
    # Convert to LUX
    mantisse = req_value & 0x0fff
    exponent = (req_value & 0xf000) >> 12

    return 2**exponent * mantisse * 0.01 # mantisse << exponent * 0.01;