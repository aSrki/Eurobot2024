import canopen
import sys
import os
import traceback

import time

import subprocess



class MaxonDriver:

    subprocess.run(["sudo", "/sbin/ip", "link", "set", "can0", "up", "type", "can", "bitrate", "500000"])
    subprocess.run(["sudo", "ip", "link", "set", "can0", "type", "can", "restart-ms", "500"])

    # Start with creating a network representing one CAN bus
    network = canopen.Network()

    # Connect to the CAN bus
    network.connect(bustype='socketcan', channel='can0')
    network.check()
    
    def __init__(self, id):        
        # Add some nodes with corresponding Object Dictionaries
        self.node = canopen.BaseNode402(id, 'maxon.eds')
        self.network.add_node(self.node)

        print('node nmt state 0) = {0}'.format(self.node.nmt.state))

        # Reset network
        self.node.nmt.state = 'RESET COMMUNICATION'
        
        #node.nmt.state = 'RESET'
        self.node.nmt.wait_for_bootup(15)

        print('node nmt state 1) = {0}'.format(self.node.nmt.state))

        # Transmit SYNC every 100 ms
        self.network.sync.start(0.1)

        self.node.load_configuration()

        self.node.nmt.state = 'OPERATIONAL'

        print('node nmt state 2) = {0}'.format(self.node.nmt.state))
    
        self.node.setup_402_state_machine()

        print('node state 1 = {0}'.format(self.node.state))

        # Read PDO configuration from node
        #self.node.tpdo.read()

        # Re-map TxPDO1
        self.node.tpdo[1].clear()
        self.node.tpdo[1].add_variable('Statusword')
        self.node.tpdo[1].add_variable('Velocity actual value')
        self.node.tpdo[1].trans_type = 1
        self.node.tpdo[1].enabled = True

        self.node.tpdo.save()


        self.node.rpdo[1].clear()
        self.node.rpdo[1].add_variable('Modes of operation')
        self.node.rpdo[1].trans_type = 1
        self.node.rpdo[1].enabled = True

        self.node.rpdo[2].clear()
        self.node.rpdo[2].add_variable('Target velocity')
        self.node.rpdo[2].add_variable('Controlword')
        self.node.rpdo[2].trans_type = 1
        self.node.rpdo[2].enabled = True

        self.node.rpdo.save()

        self.node.rpdo[1].start(0.01)
        self.node.rpdo[2].start(0.01)

        self.node.sdo['Profile acceleration'].raw = 10000

        self.node.state = 'READY TO SWITCH ON'
        self.node.state = 'SWITCHED ON'

        print('node state 2 = {0}'.format(self.node.state))

        timeout = time.time() + 15
        self.node.state = 'READY TO SWITCH ON'
        while self.node.state != 'READY TO SWITCH ON':
            print("Usao u while ready")
            if time.time() > timeout:
                raise Exception('Timeout when trying to change state')
            time.sleep(0.001)

        timeout = time.time() + 15
        self.node.state = 'SWITCHED ON'
        while self.node.state != 'SWITCHED ON':
            print("Usao u while switched on")
            if time.time() > timeout:
                raise Exception('Timeout when trying to change state')
            time.sleep(0.001)

        timeout = time.time() + 15
        self.node.state = 'OPERATION ENABLED'
        while self.node.state != 'OPERATION ENABLED':
            print("Usao u while op enable")
            if time.time() > timeout:
                raise Exception('Timeout when trying to change state')
            time.sleep(0.001)
        
        print('Node Status {0}'.format(self.node.state))

        if self.node.state == 'OPERATION ENABLED':
            print('Node booted up')

        # -----------------------------------------------------------------------------------------
        self.node.nmt.start_node_guarding(0.01)

    def set_vel(self, vel):
        self.node.rpdo.read()
        self.node.rpdo[2]['Target velocity'].raw = vel
        self.node.rpdo[2]['Controlword'].raw = 0xF
        self.node.rpdo[2].transmit()
        print("Speed = " + str(self.node.rpdo[2]['Target velocity'].raw))


maxon1 = MaxonDriver(id = 1)
# maxon2 = MaxonDriver(id = 2)

maxon1.set_vel(3000)
# maxon2.set_vel(500)

time.sleep(5)

maxon1.set_vel(-3000)
# maxon2.set_vel(-500)

time.sleep(5)

maxon1.set_vel(0)
# maxon2.set_vel(0)

# network.disconnect()
