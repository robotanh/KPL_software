import serial
import time
from uart import *
#from adafruit import *
from KPL_MySQL.KPL_MySQL_header import *
import firebase_module

# Initialize Firebase
firebase_module.initialize_firebase()
parsed_data = {}
def main():
    port = '/dev/ttyS0'  # Replace with your serial port
    baud_rate = 9600

    ser = serial.Serial(port, baud_rate, timeout=2)
    time.sleep(2)  # Wait for the serial connection to initialize

    try:
        id_gas_pump = 40
        while True:
            # Send commands 11, id_gas_pump, and 12 in decimal
            send_command(ser, 11)
            send_command(ser, id_gas_pump)
            send_command(ser, 12)
            
            time.sleep(0.2)  # Adjust timing as needed

            raw_data = ser.read(76)  # Read exactly 76 bytes of data
            print(raw_data)
            # mqtt_instance.client.publish("cambien1", raw_data)
            
            if len(raw_data) == 76:
                parsed_data = parse_gas_pump_data(raw_data)
                firebase_module.store_data(raw_data , parsed_data["id_voi"])
                print("Parsed Data:", parsed_data)
                data={
                    "id_voi":parsed_data["id_voi"],
                    "ma_lan_bom":parsed_data["ma_lan_bom_past"],
                    "gia_ban":parsed_data["gia_ban_past"],
                    "tong_da_bom":parsed_data["tong_da_bom_past"],
                    "tien_ban":parsed_data["tien_dang_ban_past"]
                }
                filtered_insert(data)
                # Here you can store the parsed data in a database or process it further
            else:
                print("Incomplete data received. Length:", len(raw_data))
            
            time.sleep(5)  # Adjust the delay as needed for your application

            # Increment id_gas_pump and loop back if it exceeds 47
            id_gas_pump += 1
            if id_gas_pump > 41:
                id_gas_pump = 40

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
