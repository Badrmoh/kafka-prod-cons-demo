import requests
import json
import os
import time
from kafka import KafkaConsumer

PRODUCER_HOST = str(os.environ.get('PRODUCER_HOST'))
PRODUCER_PORT = str(os.environ.get('PRODUCER_PORT'))
PRODUCER_MSG_ENDPOINT = str(os.environ.get('PRODUCER_MSG_ENDPOINT'))
PRODUCER_ENDPOINT = "http://" + PRODUCER_HOST + ":" + PRODUCER_PORT + "/" + PRODUCER_MSG_ENDPOINT
KAFKA_SERVER = str(os.environ.get('KAFKA_SERVER'))
KAFKA_PORT = str(os.environ.get('KAFKA_PORT'))
KAFKA_TOPIC = str(os.environ.get('KAFKA_TOPIC','test'))
KAFKA_HOST_STRING = KAFKA_SERVER + ":" + KAFKA_PORT

def wait_for_host(host, port='9092', timeout=3000):
    i = 0
    while True:
        time.sleep(5)
        if (i > timeout):
            print("---> Timeout!")
            sys.exit()
        try:
            return requests.head("http://"+str(host)+":"+str(port))
        except Exception:
            print("... Waiting for Producer ...")
            i += 1

def get_kafka_conn_object(timeout=3000):
    i = 0
    while True:
        time.sleep(5)
        if (i > timeout):
            print("---> Timeout! <---")
            sys.exit()
        try:
            return KafkaConsumer(KAFKA_TOPIC,
                        group_id='my-group',
                        auto_offset_reset='earliest',
                        enable_auto_commit=False,
                        value_deserializer=lambda m:
                        json.loads(m.decode('utf-8')),
                        bootstrap_servers=KAFKA_HOST_STRING)
        except Exception:
            print("... Waiting for Kafka ...")
            i += 1

consumer = get_kafka_conn_object()
wait_for_host(PRODUCER_HOST, port=PRODUCER_PORT)

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    r = requests.post(PRODUCER_ENDPOINT,
     data=json.dumps({'topic': message.topic,
        'message':message.value}))
    print(r.status_code, r.reason)
