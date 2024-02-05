import canopen
import sys
import os
import traceback

import time

import subprocess
import threading


class MaxonDriver:

    def __init__(self, ID, network):

        try:
            self.network = network

            # Add some nodes with corresponding Object Dictionaries
            self.node = canopen.BaseNode402(ID, 'maxon.eds')
            self.network.add_node(self.node)
            # network.add_node(34, 'eds/example34.eds')
            # node = network[34]

            # Reset network
            self.node.nmt.state = 'RESET COMMUNICATION'
            # node.nmt.state = 'RESET'
            self.node.nmt.wait_for_bootup(15)

            print('node {0} nmt state 1) = {1}'.format(ID, self.node.nmt.state))

            # Iterate over arrays or records
            error_log = self.node.sdo[0x1003]
            for error in error_log.values():
                print("Error {0} was found in the log".format(error.raw))

            for node_id in self.network:
                print(self.network[node_id])

            print('node {0} nmt state 2) = {1}'.format(ID, self.node.nmt.state))

            # Read a variable using SDO

            # node.sdo[0x1006].raw = 1
            # node.sdo[0x100c].raw = 100
            # node.sdo[0x100d].raw = 3
            # node.sdo[0x1014].raw = 163
            # node.sdo[0x1003][0].raw = 0

            # Transmit SYNC every 100 ms
            self.network.sync.start(0.1)

            #self.node.load_configuration()

            self.node.nmt.state = 'OPERATIONAL'

            print('node {0} nmt state 3) = {1}'.format(ID, self.node.nmt.state))

            self.node.setup_402_state_machine()

            device_name = self.node.sdo[0x1008].raw
            vendor_id = self.node.sdo[0x1018][1].raw

            print(device_name)
            print(vendor_id)

            print('node {0} state 1 = {1}'.format(ID, self.node.state))

            # node.state = 'SWITCH ON DISABLED'

            # Read PDO configuration from node
            self.node.tpdo.read()
            # Re-map TxPDO1
            self.node.tpdo[1].clear()
            self.node.tpdo[1].add_variable('Statusword')
            self.node.tpdo[1].add_variable('Velocity actual value')
            self.node.tpdo[1].trans_type = 1
            # self.node.tpdo[1].event_timer = 0
            self.node.tpdo[1].enabled = True
            # Save new PDO configuration to self.node
            self.node.tpdo.save()

            self.node.rpdo[1].clear()
            self.node.rpdo[1].add_variable('Modes of operation')
            self.node.rpdo[1].trans_type = 1
            self.node.rpdo[1].enabled = True

            self.node.rpdo[2].clear()
            self.node.rpdo[2].add_variable('Target velocity')
            self.node.rpdo[2].trans_type = 1
            self.node.rpdo[2].enabled = True

            self.node.rpdo[3].clear()
            self.node.rpdo[3].add_variable('Controlword')
            self.node.rpdo[3].trans_type = 1
            self.node.rpdo[3].enabled = True

            # self.node.rpdo[4].clear()
            # self.node.rpdo[4].add_variable('Modes of operation display')
            # self.node.rpdo[4].trans_type = 1
            # self.node.rpdo[4].enabled = True

            self.node.rpdo.save()

            self.node.rpdo[1].start(0.01)
            self.node.rpdo[2].start(0.01)
            self.node.rpdo[3].start(0.01)
            # self.node.rpdo[3].start(0.01)
            # self.node.rpdo[4].start(0.01)

            self.node.state = 'READY TO SWITCH ON'

            self.node.state = 'SWITCHED ON'

            print('node {0} state 2 = {1}'.format(ID, self.node.state))

            # -----------------------------------------------------------------------------------------

            print(f'Node {ID} booted up')

            timeout = time.time() + 15
            self.node.state = 'READY TO SWITCH ON'
            while self.node.state != 'READY TO SWITCH ON':
                if time.time() > timeout:
                    raise Exception('Timeout when trying to change state')
                time.sleep(0.001)

            timeout = time.time() + 15
            self.node.state = 'SWITCHED ON'
            while self.node.state != 'SWITCHED ON':
                if time.time() > timeout:
                    raise Exception('Timeout when trying to change state')
                time.sleep(0.001)

            timeout = time.time() + 15
            self.node.state = 'OPERATION ENABLED'
            while self.node.state != 'OPERATION ENABLED':
                if time.time() > timeout:
                    raise Exception('Timeout when trying to change state')
                time.sleep(0.001)

            print('Node {0} Status {1}'.format(ID, self.node.state))

            self.node.nmt.start_node_guarding(0.01)

            self.node.rpdo.read()
            self.node.rpdo[1]['Modes of operation'].raw = 3
            self.node.rpdo[1].transmit()
            # -----------------------------------------------------------------------------------------

        except KeyboardInterrupt:
            # Disconnect from CAN bus
            print('going to exit... stopping...')
            if self.network:

                for node_id in self.network:
                    self.node = self.network[node_id]
                    self.node.nmt.state = 'PRE-OPERATIONAL'
                    self.node.nmt.stop_node_guarding()
                self.network.sync.stop()
                self.network.disconnect()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            traceback.print_exc()

    def set_vel(self, vel, ID):

        try:

            self.node.rpdo.read()
            self.node.rpdo[2]['Target velocity'].raw = vel
            self.node.rpdo[2].transmit()

            self.node.rpdo.read()
            self.node.rpdo[3]['Controlword'].raw = 0x000F
            self.node.rpdo[3].transmit()

            print("Speed = " + str(self.node.rpdo[2]['Target velocity'].raw))

            try:
                self.network.check()
            except Exception:
                pass
            # Read a value from TxPDO1
            self.node.tpdo[1].wait_for_reception()
            speed = self.node.tpdo[1]['Velocity actual value'].phys

            # Read the state of the Statusword
            statusword = self.node.sdo[0x6041].raw

            print('ID: {0}'.format(ID))
            print('statusword: {0}'.format(statusword))
            print('VEL: {0}'.format(speed))

            time.sleep(0.001)

        except KeyboardInterrupt:
            # Disconnect from CAN bus
            print('going to exit... stopping...')
            if self.network:

                for node_id in self.network:
                    self.node = self.network[node_id]
                    self.node.nmt.state = 'PRE-OPERATIONAL'
                    self.node.nmt.stop_node_guarding()
                self.network.sync.stop()
                self.network.disconnect()
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            traceback.print_exc()
        finally:
            pass


# TODO: ovo staviti samo na jedno mesto (najbolje kada se inicijalizuje nukleo)
subprocess.run(["sudo", "/sbin/ip", "link", "set",
                "can0", "up", "type", "can", "bitrate", "500000"])
subprocess.run(["sudo", "ip", "link", "set", "can0",
                "type", "can", "restart-ms", "500"])

# Start with creating a network representing one CAN bus
network = canopen.Network()

# Connect to the CAN bus
network.connect(bustype='socketcan', channel='can0')

network.check()

# maxon1 = MaxonDriver(1, network)
# maxon2 = MaxonDriver(2, network)
# maxon1.set_vel(1000, 1)
# # time.sleep(0.01)
# maxon2.set_vel(1000, 2)
# # time.sleep(5)
# # maxon2.set_vel(2000, 2)
# # maxon1.set_vel(2000, 1)