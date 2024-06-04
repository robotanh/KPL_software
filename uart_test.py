import serial
import time

def calculate_checksum(data):
    # XOR all bytes from byte 2 to byte 73
    xor_sum = 0
    for byte in data[2:74]:
        xor_sum ^= ord(byte)
    # XOR with 0x5A
    checksum = xor_sum ^ 0x5A
    return checksum

def parse_gas_pump_data(raw_data):
    if len(raw_data) != 76:
        raise ValueError("Invalid data length")

    trang_thai_voi = raw_data[2]
    id_voi = raw_data[3]
    ma_lan_bom_rt = raw_data[4:10]
    so_lit_da_bom_rt = raw_data[10:19]
    gia_ban_rt = raw_data[19:25]
    tong_da_bom_rt = raw_data[25:34]
    tien_dang_ban_rt = raw_data[34:43]
    
    ma_lan_bom_pass = raw_data[43:49]
    gia_ban_pass = raw_data[49:55]
    tong_da_bom_pass = raw_data[55:64]
    tien_dang_ban_pass = raw_data[64:73]
    
    checksum_received = raw_data[75]

    calculated_checksum = calculate_checksum(raw_data)
    if checksum_received != calculated_checksum:
        raise ValueError("Checksum mismatch")

    parsed_data = {
        "trang_thai_voi": trang_thai_voi,
        "id_voi": id_voi,
        "ma_lan_bom_rt": ma_lan_bom_rt,
        "so_lit_da_bom_rt": float(so_lit_da_bom_rt),
        "gia_ban_rt": float(gia_ban_rt),
        "tong_da_bom_rt": float(tong_da_bom_rt),
        "tien_dang_ban_rt": float(tien_dang_ban_rt),
        "ma_lan_bom_pass": ma_lan_bom_pass,
        "gia_ban_pass": float(gia_ban_pass),
        "tong_da_bom_pass": float(tong_da_bom_pass),
        "tien_dang_ban_pass": float(tien_dang_ban_pass)
    }
    return parsed_data

def send_command(ser, command):
    ser.write(bytes([command]))
    time.sleep(1)  # Wait for the pump to process the command

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
