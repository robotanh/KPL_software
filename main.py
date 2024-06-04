import serial
from uart import *


def main():
    port = '/dev/ttyS0'  # Replace with your serial port
    baud_rate = 9600

    ser = serial.Serial(port, baud_rate, timeout=2)
    time.sleep(2)  # Wait for the serial connection to initialize

    try:
        while True:
            # Send commands 11, 40, and 12 in decimal
            send_command(ser, 11)
            send_command(ser, 40)
            send_command(ser, 12)
            
            time.sleep(1)  # Adjust timing as needed

            raw_data = ser.read(76)  # Read exactly 76 bytes of data
            print(raw_data)
            if len(raw_data) == 76:
                parsed_data = parse_gas_pump_data(raw_data)
                print("Parsed Data:", parsed_data)
                # Here you can store the parsed data in a database or process it further
            else:
                print("Incomplete data received. Length:", len(raw_data))
            
            time.sleep(5)  # Adjust the delay as needed for your application
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()

if __name__ == "__main__":
    main()