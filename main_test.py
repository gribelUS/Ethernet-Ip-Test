from UR.UR import UR
from UR.URconfig import ur_ip
from time import sleep

ur = UR()

def main():
    ur_connected = ur.connect(ur_ip)
    if not ur_connected:
        print(f"Failed to connect to UR robot at {ur_ip}. Exiting.")
        return
    if ur_connected:
        print(f"Successfully connected to UR robot at {ur_ip}.")
        ur.write_digital_input(1, 12)
        sleep(1)
        check = ur.read_digital_input(1)
        print(f"Digital input 1 set to: {check}")
        second_check = ur.read_digital_output(0)
        print(f"Digital output 0 status: {second_check}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        ur.disconnect()
        print("Disconnected from UR robot.")

