from PLC.PLC import PLC
from PLC.PLCconfig import PRT_PLC_IP_ADDRESS

def test_plc_connection():
    plc = PLC()
    if plc.connect(PRT_PLC_IP_ADDRESS):
        print("PLC connection test successful.")
        plc.disconnect()
    else:
        print("PLC connection test failed.")

if __name__ == "__main__":
    test_plc_connection()