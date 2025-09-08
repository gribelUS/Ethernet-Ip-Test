import rtde_io
import rtde_receive
from UR.URconfig import ur_ip

class UR:
    """
    Class to handle communication with the UR robot.
    """
    def __init__(self):
        self.ur_ip = ur_ip
        self.rtde_io = None
        self.rtde_receive = None

    def connect(self):
        """
        Establish connection with the UR robot.
        :return: True on success, False on failure
        """
        try:
            self.rtde_io = rtde_io.RTDEIOInterface(self.ur_ip)
            self.rtde_receive = rtde_receive.RTDEReceiveInterface(self.ur_ip)
            print(f"Connection established with UR robot at IP: {self.ur_ip}")
            return True
        except Exception as e:
            print(f"Failed to connect to UR robot at IP: {self.ur_ip}")
            print("Error:", e)
            return False

    def read_digital_output(self, pin: int) -> int:
        """
        Reads the state of a digital output pin on the UR robot.
        :param pin: The digital output pin number to read.
        :return: The state of the digital output pin (1 for high, 0 for low).
        """
        if self.rtde_receive and self.rtde_receive.isConnected():
            return self.rtde_receive.getDigitalOut(pin)
        else:
            raise ConnectionError("Not connected to UR robot.")

    def write_digital_input(self, pin: int, value: int):
        """
        Sets the state of a digital input pin on the UR robot.
        :param pin: The digital input pin number to set.
        :param value: The value to set the pin to (1 for high, 0 for low).
        """
        if self.rtde_io and self.rtde_io.isConnected():
            self.rtde_io.setDigitalIn(pin, value)
        else:
            raise ConnectionError("Not connected to UR robot.")

    def disconnect(self):
        """
        Disconnects from the UR robot.
        """
        if self.rtde_io:
            self.rtde_io.disconnect()
            self.rtde_io = None
        if self.rtde_receive:
            self.rtde_receive.disconnect()
            self.rtde_receive = None