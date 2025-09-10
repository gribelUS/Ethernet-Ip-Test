from PLC.PLC import PLC
from PLC.PLCconfig import PRT_PLC_IP_ADDRESS
from UR.UR import UR
from UR.URconfig import ur_ip
import time

plc = PLC()
ur = UR()

def main():
    # Connect to PLC
    plc_connected = plc.connect(PRT_PLC_IP_ADDRESS)
    if not plc_connected:
        print("Exiting due to PLC connection failure.")
        return
    
    # Connect to UR Robot
    ur_connected = ur.connect(ur_ip)
    if not ur_connected:
        print("Exiting due to UR robot connection failure.")
        return
    
    while plc_connected and ur_connected:
        # Read trigger and area tags from PLC
        trigger = plc.read_tag("UR.int[0]")
        area = plc.read_tag("UR.int[1]")

        # Write to UR robot value from PLC tag
        ur.write_digital_input(0, trigger)
        print(f"Set UR digital input 0 to {trigger}")
        time.sleep(0.5)
        ur.write_digital_input(1, area)
        print(f"Set UR digital input 1 to {area}")

        # Read status from UR robot
        status = ur.read_digital_output(0)
        print(f"UR digital output 0 status: {status}")
        if status:
            plc.write_tag("UR_RETURN", 1) # Reset trigger in PLC
            print("Reset PLC trigger to 0")
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        ur.disconnect()
        plc.disconnect()
        print("Disconnected from UR robot and PLC.")