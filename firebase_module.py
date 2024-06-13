import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
def initialize_firebase():
    cred = credentials.Certificate("./firebaseConfig.json")
    firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://kpl-gaspump-realtime-default-rtdb.asia-southeast1.firebasedatabase.app/gas_pump_data'
        })

def store_data(raw_data , id_voi):
    try:
        ref = db.reference(f'gas_pump_data/Voi_{id_voi}')
        ref.update({
            'raw_data': raw_data.decode('utf-8')
        })
        print("Raw data stored successfully.")
    except Exception as e:
        print(f"Failed to store raw data: {e}")

