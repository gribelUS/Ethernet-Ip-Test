from pycomm3 import LogixDriver

class PLC:
    """
    Class to handle communication with the PLC.
    """

    def __init__(self):
        self.driver = None

    def connect(self, ip_address):
        """
        Establish connection to the PLC.
        :return: True on success, False on failure
        """
        try:
            self.driver = LogixDriver(ip_address)
            self.driver.open()
            print(f"Connected to PLC at {ip_address}")
            return True
        except Exception as e:
            print(f"Failed to connect to PLC at {ip_address}: {e}")
            return False

    def read_tag(self, tag_name):
        """
        Read a tag from the PLC.
        :param tag_name: Name of the tag to read
        :return: Value of the tag or None on failure
        """
        if self.driver is None:
            print("Not connected to PLC.")
            return None

        try:
            response = self.driver.read(tag_name)
            if response is None:
                print(f"Tag {tag_name} not found.")
                return None
            return response.value
        except Exception as e:
            print(f"Failed to read tag {tag_name}: {e}")
            return None

    def write_tag(self, tag_name, value):
        """
        Write a value to a tag in the PLC.
        :param tag_name: Name of the tag to write
        :param value: Value to write to the tag
        :return: True on success, False on failure
        """
        if self.driver is None:
            print("Not connected to PLC.")
            return False

        try:
            response = self.driver.write(tag_name, value)
            if response:
                return True
            print(f"Failed to write value to tag {tag_name}.")
            return False
        except Exception as e:
            print(f"Failed to write tag {tag_name}: {e}")
            return False

    def disconnect(self):
        """
        Disconnect from the PLC.
        """
        if self.driver:
            self.driver.close()
            self.driver = None