import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
def initialize_firebase():
    cred = credentials.Certificate("firebaseConfig.json")
    firebase_admin.initialize_app(cred)

def store_data(raw_data):
    ref = db.reference('gas_pump_data')
    ref.push({
        'raw_data': raw_data.decode('utf-8')
    })

