import canopen
import time
import subprocess

# Constants
PDO_TIME = 0.001  # SYNC interval in seconds


# Controlword sequence to exit "Switch on Disabled" and enable operation
def enable_operation(motor):
    try:
        # Reset fault and ensure drive is ready
        motor.sdo[0x6040].raw = 0x80  # Fault reset
        time.sleep(0.1)

        motor.sdo[0x6060].raw = 0x03

        # Transition to "Ready to Switch On"
        motor.sdo[0x6040].raw = 0x06
        time.sleep(0.1)

        # Transition to "Switched On"
        motor.sdo[0x6040].raw = 0x07
        time.sleep(0.1)

        # Transition to "Operation Enabled"
        motor.sdo[0x6040].raw = 0x0F
        time.sleep(0.1)
        
        # Verify final state
        status = motor.sdo[0x6041].raw
        print(f"Node {motor.id} Statusword: {hex(status)}")


    except Exception as e:
        print(f"Error enabling Node {motor.id}: {e}")
        raise

# trebalo bi da ima bootupovan can
# Set up the CAN interface
# subprocess.run(["sudo", "/sbin/ip", "link", "set", "can0", "up", "type", "can", "bitrate", "500000"])
# subprocess.run(["sudo", "ip", "link", "set", "can0", "type", "can", "restart-ms", "500"])

# Connect to the CAN network
network = canopen.Network()
network.connect(channel='can0', bustype='socketcan')

# Add the CiA 402 nodes
motor_1 = network.add_node(1, 'maxon.eds')  # Replace with correct EDS file path
motor_2 = network.add_node(5, 'maxon.eds')

# Start SYNC
network.sync.start(PDO_TIME)

# Configure PDOs for each motor
for motor, node_id, cob_id in zip([motor_1, motor_2], [1, 5], [0x201, 0x205]):
    # Set node to PRE-OPERATIONAL state
    motor.nmt.state = 'PRE-OPERATIONAL'
    time.sleep(2)

    # Configure RPDO1 for velocity control
    motor.rpdo.read()
    motor.rpdo[1].clear()
    motor.rpdo[1].add_variable('Controlword')  # 0x6040
    motor.rpdo[1].add_variable('Target velocity')  # 0x60FF
    motor.rpdo[1].cob_id = cob_id  # Assign unique COB-ID
    motor.rpdo[1].trans_type = 1  # Synchronous updates
    motor.rpdo[1].enabled = True
    motor.rpdo.save()

    # Verify RPDO1 mapping
    print(f"Node {node_id} RPDO1 COB-ID: {hex(motor.rpdo[1].cob_id)}")
    print(f"Node {node_id} RPDO1 map: {motor.rpdo[1].map}")

# Enable motors for operation
for motor in [motor_1, motor_2]:
    enable_operation(motor)

# Check for warnings or errors
for motor in [motor_1, motor_2]:
    error_register = motor.sdo[0x1001].raw
    print(f"Node {motor.id} Error Register: {bin(error_register)}")
    error_history = motor.sdo[0x1003]
    print(f"Node {motor.id} Error History: {list(error_history.values())}")

    if error_register != 0:
        print(f"Node {motor.id} has active warnings/errors. Resolve before proceeding.")
        raise Exception(f"Error detected in Node {motor.id}: {bin(error_register)}")
    
# Switch nodes to OPERATIONAL state
for motor in [motor_1, motor_2]:
    motor.nmt.state = 'OPERATIONAL'
    time.sleep(1)

# Transmit target velocities via RPDOs
def transmit_velocities():
    
    VEL1 = 1000  # Target velocity for motor 1 (counts/sec)
    VEL2 = 500  # Target velocity for motor 2 (counts/sec)

    motor_1.rpdo[1]['Controlword'].raw = 0x0F  # Enable operation
    motor_1.rpdo[1]['Target velocity'].raw = VEL1
    motor_1.rpdo[1].transmit()

    motor_2.rpdo[1]['Controlword'].raw = 0x0F
    motor_2.rpdo[1]['Target velocity'].raw = VEL2
    motor_2.rpdo[1].transmit()

    print(f"Speed set for motor 1: {VEL1} counts/sec")
    print(f"Speed set for motor 2: {VEL2} counts/sec")
    
    time.sleep(2)
    VEL1 = 500
    VEL2 = 1000
    
    motor_1.rpdo[1]['Controlword'].raw = 0x0F  # Enable operation
    motor_1.rpdo[1]['Target velocity'].raw = VEL1
    motor_1.rpdo[1].transmit()

    motor_2.rpdo[1]['Controlword'].raw = 0x0F
    motor_2.rpdo[1]['Target velocity'].raw = VEL2
    motor_2.rpdo[1].transmit()

    print(f"Speed set for motor 1: {VEL1} counts/sec")
    print(f"Speed set for motor 2: {VEL2} counts/sec")
    
    time.sleep(5)
    
    

# Loop to maintain velocity commands and re-transmit
try:
    while True:
        transmit_velocities()
        time.sleep(PDO_TIME)  # Match SYNC interval
except KeyboardInterrupt:
    print("Stopping motors and exiting.")

# Stop motors before disconnecting
for motor in [motor_1, motor_2]:
    motor.sdo[0x6040].raw = 0x06  # Shut down
    motor.nmt.state = 'PRE-OPERATIONAL'
    time.sleep(1)

# Disconnect from the CAN network
network.disconnect()
print("Disconnected from CAN network.")