import canopen
import sys
import os
import traceback

import time

import subprocess

try:

    subprocess.run(["sudo", "/sbin/ip", "link", "set", "can0",
                   "up", "type", "can", "bitrate", "500000"])
    subprocess.run(["sudo", "ip", "link", "set", "can0",
                   "type", "can", "restart-ms", "500"])

    # Start with creating a network representing one CAN bus
    network = canopen.Network()

    # Connect to the CAN bus
    network.connect(bustype='socketcan', channel='can0')

    network.check()

    # Add some nodes with corresponding Object Dictionaries
    node = canopen.BaseNode402(1, 'maxon.eds')
    network.add_node(node)
    # network.add_node(34, 'eds/example34.eds')
    # node = network[34]

    # Reset network
    node.nmt.state = 'RESET COMMUNICATION'
    # node.nmt.state = 'RESET'
    node.nmt.wait_for_bootup(15)

    print('node nmt state 1) = {0}'.format(node.nmt.state))

    # Iterate over arrays or records
    error_log = node.sdo[0x1003]
    for error in error_log.values():
        print("Error {0} was found in the log".format(error.raw))

    for node_id in network:
        print(network[node_id])

    print('node nmt state 2) = {0}'.format(node.nmt.state))

    # Read a variable using SDO

    # node.sdo[0x1006].raw = 1
    # node.sdo[0x100c].raw = 100
    # node.sdo[0x100d].raw = 3
    # node.sdo[0x1014].raw = 163
    # node.sdo[0x1003][0].raw = 0

    # Transmit SYNC every 100 ms
    network.sync.start(0.1)

    node.load_configuration()

    node.nmt.state = 'OPERATIONAL'

    print('node nmt state 3) = {0}'.format(node.nmt.state))

    node.setup_402_state_machine()

    device_name = node.sdo[0x1008].raw
    vendor_id = node.sdo[0x1018][1].raw

    print(device_name)
    print(vendor_id)

    print('node state 1 = {0}'.format(node.state))

    # node.state = 'SWITCH ON DISABLED'

    # Read PDO configuration from node
    node.tpdo.read()
    # Re-map TxPDO1
    node.tpdo[1].clear()
    node.tpdo[1].add_variable('Statusword')
    node.tpdo[1].add_variable('Velocity actual value')
    node.tpdo[1].trans_type = 1
    # node.tpdo[1].event_timer = 0
    node.tpdo[1].enabled = True
    # Save new PDO configuration to node
    node.tpdo.save()

    node.rpdo[1].clear()
    node.rpdo[1].add_variable('Modes of operation')
    node.rpdo[1].trans_type = 1
    node.rpdo[1].enabled = True

    node.rpdo[2].clear()
    node.rpdo[2].add_variable('Controlword')
    node.rpdo[2].add_variable('Target velocity')
    node.rpdo[2].trans_type = 1
    node.rpdo[2].enabled = True

    # node.rpdo[3].clear()
    # node.rpdo[3].add_variable('Controlword')
    # node.rpdo[3].trans_type = 1
    # node.rpdo[3].enabled = True

    node.rpdo.save()

    node.rpdo[1].start(0.01)
    node.rpdo[2].start(0.01)
    # node.rpdo[3].start(0.01)

    node.state = 'READY TO SWITCH ON'
    node.state = 'SWITCHED ON'

    print('node state 2 = {0}'.format(node.state))

    # -----------------------------------------------------------------------------------------

    print('Node booted up')

    timeout = time.time() + 15
    node.state = 'READY TO SWITCH ON'
    while node.state != 'READY TO SWITCH ON':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    timeout = time.time() + 15
    node.state = 'SWITCHED ON'
    while node.state != 'SWITCHED ON':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    timeout = time.time() + 15
    node.state = 'OPERATION ENABLED'
    while node.state != 'OPERATION ENABLED':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print('Node Status {0}'.format(node.state))

    # -----------------------------------------------------------------------------------------
    node.nmt.start_node_guarding(0.01)

    node.rpdo.read()
    node.rpdo[1]['Modes of operation'].raw = 3
    node.rpdo[1].transmit()

    vel = input("speed?")
    node.rpdo.read()
    node.rpdo[2]['Target velocity'].raw = vel
    node.rpdo[2]['Controlword'].raw = 0x000F
    node.rpdo[2].transmit()

    print("Speed = " + str(node.rpdo[2]['Target velocity'].raw))

    while True:
        try:
            network.check()
        except Exception:
            break

        # Read a value from TxPDO1
        node.tpdo[1].wait_for_reception()
        speed = node.tpdo[1]['Velocity actual value'].phys

        # Read the state of the Statusword
        statusword = node.sdo[0x6041].raw

        print('statusword: {0}'.format(statusword))
        print('VEL: {0}'.format(speed))

        time.sleep(0.01)

except KeyboardInterrupt:
    pass
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    traceback.print_exc()
finally:
    # Disconnect from CAN bus
    print('going to exit... stopping...')
    if network:

        for node_id in network:
            node = network[node_id]
            node.nmt.state = 'PRE-OPERATIONAL'
            node.nmt.stop_node_guarding()
        network.sync.stop()
        network.disconnect()
