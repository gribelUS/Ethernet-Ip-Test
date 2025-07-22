# Ethernet-Ip-Test
    This Python program can be used to test UR Cobot program being controled by external variables by using MODBUS communication protocol to send the robot a new value to a specific variable.

## IP Address
    To use MODBUS communication it is recommended to set a fixed IP address (192.168.1.10 is being used for the UR5e at SCIAI) to the robot so that it can be easily reachable from the software. Both robot and computer running the python code need to be in the same sub mask (255.255.255.0 is the one being used for SCIAI)

    For the communication to work it is also necessary for the computer and UR5e to be connected via Ethernet cable

    The port (502) being used is the default for MODBUS communication protocol with this specific robot, for other communication protocols such as Ethernet/IP and fieldbus uses different ports