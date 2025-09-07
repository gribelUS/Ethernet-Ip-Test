from PLC.PLC import connect, read_tag, write_tag, disconnect
from UR.UR import ur_connect, read_digital_output, write_digital_input, ur_disconnect
import time

def main():
    # Connect to PLC
    plc_connected = connect()
    if not plc_connected:
        print("Exiting due to PLC connection failure.")
        return
    
    # Connect to UR Robot
    ur_connected = ur_connect()
    if not ur_connected:
        print("Exiting due to UR robot connection failure.")
        return
    
    while plc_connected and ur_connected:
        # Read trigger and area tags from PLC
        trigger = read_tag("UR.int[0]")
        area = read_tag("UR.int[1]")

        # Write to UR robot value from PLC tag
        write_digital_input(0, trigger)
        print(f"Set UR digital input 0 to {trigger}")
        time.sleep(0.5)
        write_digital_input(1, area)
        print(f"Set UR digital input 1 to {area}")

        # Read status from UR robot
        status = read_digital_output(0)
        print(f"UR digital output 0 status: {status}")
        if status:
            write_tag("UR_RETURN", 1) # Reset trigger in PLC
            print("Reset PLC trigger to 0")
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        ur_disconnect()
        disconnect()
        print("Disconnected from UR robot and PLC.")