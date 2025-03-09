import serial
import serial.tools.list_ports
import subprocess
import time
import sys

class STMResetTool:
    def __init__(self, port='/dev/tty_stm32'):
        self.port = port
        self.baudrate = 115200
        self.timeout = 1

    def list_available_ports(self):
        """List all available COM ports"""
        ports = serial.tools.list_ports.comports()
        print("\nAvailable ports:")
        for port in ports:
            print(f"- {port.device}: {port.description}")

    def check_serial_connection(self):
        """Test if we can open the serial port"""
        try:
            with serial.Serial(self.port, self.baudrate, timeout=self.timeout) as ser:
                print(f"Successfully opened {self.port}")
                return True
        except serial.SerialException as e:
            print(f"Error opening {self.port}: {e}")
            return False

    def reset_via_dtr(self):
        """Reset using DTR line"""
        try:
            print("\nAttempting DTR reset...")
            with serial.Serial(self.port, self.baudrate, timeout=self.timeout) as ser:
                ser.setDTR(False)
                time.sleep(0.1)
                ser.setDTR(True)
                time.sleep(2)
                data = ser.read(100)
                if data:
                    print("DTR reset successful - Received data:")
                    print(data.hex())
                else:
                    print("DTR reset completed, no data received")
            return True
        except serial.SerialException as e:
            print(f"DTR reset failed: {e}")
            return False

    def reset_via_stlink(self):
        """Reset using ST-Link tools"""
        try:
            print("\nAttempting ST-Link reset...")
            # Try st-flash first
            subprocess.run(['st-flash', 'reset'], check=True)
            time.sleep(1)
            #subprocess.run(['st-flash', 'reset run'], check=True)
            print("ST-Link reset successful")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error with st-flash: {e}")
            try:
                # Try st-link_cli as backup
                subprocess.run(['st-link_cli', '-c', 'SWD', '-Rst'], check=True)
                time.sleep(1)
                subprocess.run(['st-link_cli', '-c', 'SWD', '-Run'], check=True)
                print("ST-Link CLI reset successful")
                return True
            except subprocess.CalledProcessError as e:
                print(f"Error with st-link_cli: {e}")
                return False
            except FileNotFoundError:
                print("ST-Link tools not found")
                return False

    def verify_board_state(self):
        """Verify board is responding after reset"""
        try:
            with serial.Serial(self.port, self.baudrate, timeout=self.timeout) as ser:
                time.sleep(1)
                if ser.is_open:
                    ser.write(b'\r\n')  # Send empty line
                    time.sleep(0.1)
                    response = ser.read(100)
                    if response:
                        print("\nBoard is responding after reset")
                        return True
                    else:
                        print("\nNo response from board")
                        return False
        except serial.SerialException as e:
            print(f"\nError verifying board state: {e}")
            return False

    def full_reset_procedure(self):
        """Execute full reset procedure with all methods"""
        print("\n=== Starting STM32 Reset Procedure ===")
        
        # List available ports
        self.list_available_ports()
        
        # Check initial connection
        if not self.check_serial_connection():
            print("\nWARNING: Initial serial connection failed")
        
        # Try DTR reset first
        # dtr_success = self.reset_via_dtr()
        
        # If DTR reset fails or verification fails, try ST-Link reset
        #if not dtr_success or not self.verify_board_state():
        #    print("\nDTR reset insufficient, trying ST-Link reset...")
        #    stlink_success = self.reset_via_stlink()
        #    
        #    if not stlink_success:
        #        print("\nWARNING: Both reset methods failed")
        #        return False
        self.reset_via_stlink()
        
        # Final verification
        if self.verify_board_state():
            print("\n=== Reset procedure completed successfully ===")
            return True
        else:
            print("\n=== Reset procedure completed with warnings ===")
            return False

def main():
    # Create reset tool instance
    stm_reset = STMResetTool('/dev/ttyUSB1')
    
    try:
        # Execute full reset procedure
        success = stm_reset.full_reset_procedure()
        
        # Exit with appropriate status
        sys.exit(0 if success else 1)
        
    except KeyboardInterrupt:
        print("\nReset procedure interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()