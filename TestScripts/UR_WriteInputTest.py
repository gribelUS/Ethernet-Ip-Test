from UR.UR import UR
from UR.URconfig import ur_ip

def test_write_digital_input():
    ur = UR()
    ur.connect(ur_ip)
    test_pin = 1
    test_value = 1
    ur.write_digital_input(test_pin, test_value)


if __name__ == "__main__":
    test_write_digital_input()
    