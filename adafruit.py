
import time
import random
import json
from Adafruit_IO import MQTTClient



class Adafruit_MQTT:

    AIO_FEED_IDs = ["cambien1", "cambien2"]
    AIO_USERNAME = "robotanh"
    AIO_KEY = ""
    recvCallBack = None

    def connected(self, client):
        print("Connected ...")
        for feed in self.AIO_FEED_IDs:
            client.subscribe(feed)

    def subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribed...")

    def disconnected(self, client):
        print("Disconnected... Trying to reconnect.")
        self.client.reconnect()


    def message(self, client, feed_id, payload):
        print("Received: " + payload + ", feed id: "+feed_id)



    def setRecvCallBack(self, func):
        self.recvCallBack = func

    def __init__(self):
        self.client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.message
        self.client.on_subscribe = self.subscribe
        self.client.connect()
        self.client.loop_background()






# Create an instance of Adafruit_MQTT

mqtt_instance = Adafruit_MQTT()


while True:
    print("Data is publishing.........")

    num1 = random.randint(10, 20)
    num2 = random.randint(10, 20)
    num3 = random.randint(10, 20)
    mqtt_instance.client.publish("cambien1", num1)
    mqtt_instance.client.publish("cambien2", num2)
    mqtt_instance.client.publish("cambien3", num3)
    print("cambien1 = ",num1)
    print("cambien2 = ",num2)
    print("cambien3 = ",num3)
    time.sleep(5)
