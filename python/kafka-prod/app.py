import logging
import json
import requests
import os
import time
from kafka import KafkaProducer
from flask import Flask, render_template, request


app = Flask(__name__)
messages: list = []
KAFKA_SERVER = str(os.environ.get('KAFKA_SERVER'))
KAFKA_PORT = str(os.environ.get('KAFKA_PORT'))
KAFKA_HOST_STRING = KAFKA_SERVER + ":" + KAFKA_PORT
FLASK_SERVER = str(os.environ.get('FLASK_HOST','0.0.0.0'))
FLASK_PORT = os.environ.get('FLASK_PORT','5000')

def on_send_success(r):
  logging.debug('success')


def on_send_error(excp):
    logging.error('I am an errback', exc_info=excp)


def get_kafka_conn_object(timeout=3000):
    i = 0
    while True:
        time.sleep(5)
        if (i > timeout):
            print("---> Timeout! <---")
            sys.exit()
        try:
            return KafkaProducer(bootstrap_servers=KAFKA_HOST_STRING,
            value_serializer=lambda m: json.dumps(m).encode('utf-8'),retries=5)
        except Exception:
            print("... Waiting for Kafka ...")
            i += 1

@app.route("/")
def index():
  if not messages:
      return render_template("producer.html")
  print (messages)
  return render_template("producer.html", messages=messages)

@app.route("/", methods=['POST'])
def publish():
  message = request.form['message']
  logging.info(str(message))
  # produce asynchronously with callbacks
  if message:
    producer.send('test', json.dumps(str(message))).add_callback(on_send_success).add_errback(on_send_error)
    producer.flush()
  return render_template("producer.html", messages=messages)


@app.route("/messages")
def get_messages():
  if not messages:
      return render_template("consumer.html")
  return render_template("consumer.html", messages=messages)

@app.route("/messages", methods=['POST'])
def update_messages():
    content = request.get_json(force=True)
    print ('received: ' + str(content))
    messages.append(content['message'])
    return render_template("producer.html", messages=messages)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    producer = get_kafka_conn_object()
    app.run(host=FLASK_SERVER,port=FLASK_PORT)
