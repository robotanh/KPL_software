import serial
import time

def calculate_checksum(data):
    # XOR all bytes from byte 2 to byte 73
    xor_sum = 0
    for byte in data[2:73]:
        xor_sum ^= byte
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
    
    ma_lan_bom_past = raw_data[43:49]
    gia_ban_past = raw_data[49:55]
    tong_da_bom_past = raw_data[55:64]
    tien_dang_ban_past = raw_data[64:73]
    
    checksum_received = raw_data[74]

    calculated_checksum = calculate_checksum(raw_data)
    print("calculated_checksum = ", calculated_checksum)
    print("checksum_received = ", checksum_received)
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
        "ma_lan_bom_past": ma_lan_bom_past,
        "gia_ban_past": float(gia_ban_past),
        "tong_da_bom_past": float(tong_da_bom_past),
        "tien_dang_ban_past": float(tien_dang_ban_past)
    }
    return parsed_data

def send_command(ser, command):
    ser.write(bytes([command]))
    time.sleep(1)  # Wait for the pump to process the command

