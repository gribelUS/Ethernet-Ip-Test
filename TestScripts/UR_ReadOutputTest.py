from UR.UR import UR
from UR.URconfig import ur_ip

def test_read_digital_output():
    ur = UR()
    ur.connect(ur_ip)
    test_pin = 1
    test_read = ur.read_digital_output(test_pin)
    print(f"Digital output pin {test_pin} read value: {test_read}")

if __name__ == "__main__":
    test_read_digital_output()