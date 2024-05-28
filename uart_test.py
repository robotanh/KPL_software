
import serial
import time

def calculate_checksum(data):
    # Implement checksum calculation (assuming a simple sum for this example)
    checksum = sum(ord(c) for c in data[:-1]) % 256
    return checksum

def parse_gas_pump_data(raw_data):
    if len(raw_data) != 76:
        raise ValueError("Invalid data length")

    status_gas_pump = raw_data[0]
    id_pump_action = raw_data[1:7]
    liter_already_pumped = raw_data[7:16]
    gas_cost = raw_data[16:22]
    total_liter = raw_data[22:31]
    money = raw_data[31:40]
    checksum_received = ord(raw_data[40])  # Convert checksum character to its ASCII value

    # Calculate checksum and validate
    calculated_checksum = calculate_checksum(raw_data)
    if checksum_received != calculated_checksum:
        raise ValueError("Checksum mismatch")

    parsed_data = {
        "status_gas_pump": status_gas_pump,
        "id_pump_action": id_pump_action,
        "liter_already_pumped": float(liter_already_pumped),
        "gas_cost": float(gas_cost),
        "total_liter": float(total_liter),
        "money": float(money)
    }
    return parsed_data

def send_command(ser, command):
    ser.write(bytes([command]))
    time.sleep(1)  # Wait for the pump to process the command

def main():
    port = '/dev/ttyS0' # Replace with your serial port
    baud_rate = 9600

    ser = serial.Serial(port, baud_rate, timeout=1)
    time.sleep(2)  # Wait for the serial connection to initialize

    try:
        while True:
            # Send commands 11, 12, and 13 in decimal
            send_command(ser, 11)
            send_command(ser, 40)
            send_command(ser, 12)
            
            time.sleep(1)  # Adjust timing as needed

            raw_data = ser.read(76)  # Read 76 bytes of data

            print(raw_data)
            
            time.sleep(10)  # Adjust the delay as needed for your application
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
