import rtde_io
import rtde_receive
import time
from UR.URconfig import ur_ip

rtde_io = None
rtde_receive = None

def ur_connect():
    """
    Establish connection with the UR robot and returns a boolean indicating success or failure.
    """
    global rtde_io, rtde_receive
    try:
        rtde_io = rtde_io.RTDEIOInterface(ur_ip)
        rtde_receive = rtde_receive.RTDEReceiveInterface(ur_ip)
        print("Connection established with UR robot at IP:", ur_ip)
        return True
    except Exception as e:
        print("Failed to connect to UR robot at IP:", ur_ip)
        print("Error:", e)
        return False
    
def read_digital_output(pin: int) -> int:
    """
    Reads the state of a digital output pin on the UR robot.
    
    Args:
        pin (int): The digital output pin number to read.
        
    Returns:
        int: The state of the digital output pin (1 for high, 0 for low).
    """
    if rtde_receive and rtde_receive.isConnected():
        return rtde_receive.getDigitalOut(pin)
    else:
        raise ConnectionError("Not connected to UR robot.")
    
def write_digital_input(pin: int, value: int):
    """
    Sets the state of a digital input pin on the UR robot.
    
    Args:
        pin (int): The digital input pin number to set.
        value (int): The value to set the pin to (1 for high, 0 for low).
    """
    if rtde_io and rtde_io.isConnected():
        rtde_io.setDigitalIn(pin, value)
    else:
        raise ConnectionError("Not connected to UR robot.")

def ur_disconnect():
    """
    Disconnects from the UR robot.
    """
    global rtde_io, rtde_receive
    if rtde_io:
        rtde_io.disconnect()
        rtde_io = None
    if rtde_receive:
        rtde_receive.disconnect()
        rtde_receive = None