from UR.URconfig import ur_ip
from UR.UR import UR

def test_ur_connection():
    try:
        ur = UR()
        ur.connect(ur_ip)
    except Exception as e:
        print(f"Error connecting to UR: {e}")

if __name__ == "__main__":
    test_ur_connection()