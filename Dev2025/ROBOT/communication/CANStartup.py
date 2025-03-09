# ZA RPI 4/5

import os
import can
import subprocess
import sys



def is_interface_up(interface):
    try:
        output = subprocess.check_output(["ip", "link", "show", interface])
        return "state UP" in output.decode()
    except subprocess.CalledProcessError:
        return False

def setup_can_interfaces():
    try:
        # Proverite da li je can0 podignut
        if not is_interface_up("can0"):
            os.system("sudo ip link set can0 type can bitrate 500000")
            os.system("sudo ifconfig can0 up")
        
        # Proverite da li je can1 podignut
        if not is_interface_up("can1"):
            os.system("sudo ip link set can1 type can bitrate 500000")
            os.system("sudo ifconfig can1 up")
        
        # Ako su oba interfejsa uspela da se podignu, izađite sa statusom 0 (success)
        if is_interface_up("can0") and is_interface_up("can1"):
            print("CAN interfaces are up and running")
            sys.exit(0)  # Uspeh
        
        else:
            print("Failed to bring up CAN interfaces")
            sys.exit(1)  # Neuspeh
    
    except Exception as e:
        # Ako dođe do bilo kakve greške, obradite i izađite sa statusom 1
        print(f"Error: {e}")
        sys.exit(1)  # Neuspeh

# Poziv funkcije
setup_can_interfaces()

# can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')
# can1 = can.interface.Bus(channel = 'can1', bustype = 'socketcan')