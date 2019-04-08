from microbit import i2c

PCA9554A_I2C_ADDRESS = 0x38
PCA9554A_REG_INPUT_PORT = 0x00
PCA9554A_REG_OUTPUT_PORT = 0x01
PCA9554A_REG_POL_INVERSION = 0x02
PCA9554A_REG_CONFIG = 0x03

PCA9554A_CONF_OUTPUT = 0x00
PCA9554A_CONF_INPUT = 0xFF

PCA9554A_ALL_OUTPUTS_OFF = 0x00

class OC13:
    
    def __init__(self, addr=PCA9554A_I2C_ADDRESS):
        self.addr = addr
     
    def init(self, state=False):
        self.writePin(0, state)
        self.writePin(1, state)
        self.writePin(2, state)
        self.writePin(3, state)
        self.writePin(4, state)
        i2c.write(self.addr, bytearray([PCA9554A_REG_CONFIG, PCA9554A_CONF_OUTPUT]))
        return True
    
    def writePin(self, channel, state):
        port_status = self.getStatus() & 0xFF
        pinNo = 1 << channel
        
        if state is True:
            i2c.write(self.addr, bytearray([PCA9554A_REG_OUTPUT_PORT, (pinNo | port_status)]))
        elif state is False:
            i2c.write(self.addr, bytearray([PCA9554A_REG_OUTPUT_PORT, ((~pinNo) & port_status)]))
    
    def getStatus(self):
        i2c.write(self.addr, bytearray([PCA9554A_REG_OUTPUT_PORT]))
        pin_state = i2c.read(self.addre, 1)
        return pin_state[0]
