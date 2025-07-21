from pymodbus.client import ModbusTcpClient
import time

# UR5e IP address
robot_ip = "192.168.1.10"

# I/O address
trigger_bit_address = 1
area_bit_address = 31

# I/O value
trigger_bit = 0
area_bit = 0

client = ModbusTcpClient(robot_ip, port=502)
client.connect()

# Write value 1 to Holding Register 0
client.write_register(trigger_bit_address, trigger_bit)
time.sleep(1)
client.write_register(area_bit_address, area_bit)

print("Wrote values to UR5e I/O registers.")
client.close()

