import serial

def main():
    # Open the serial port
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)

    # Check if the serial port is open
    if ser.is_open:
        print("Serial port is open.")
    else:
        print("Failed to open serial port.")

    try:
        # Write data to the serial device
        ser.write(b'Hello, UART!\n')

        # Read data from the serial device
        line = ser.readline()  # Read a line of text (ending with \n or \r)
        print(f"Received: {line.decode('utf-8')}")

    finally:
        # Close the serial connection
        ser.close()
        print("Serial port is closed.")

if __name__ == "__main__":
    main()

