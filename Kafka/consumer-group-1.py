from confluent_kafka import Consumer, KafkaError, KafkaException
import sys
import requests

me = 'DolZz-1'
groupId = me + '-group1'

conf = {
    'bootstrap.servers': '34.138.205.183:9094,34.138.104.233:9094,34.138.118.154:9094',
    'group.id': groupId,
    'enable.auto.commit': True,
    'auto.offset.reset': 'smallest'
}


consumer = Consumer(conf)
topics = [me]
consumer.subscribe(topics)

import random

def detect_object(msg):
    choice = random.choice(['car', 'house', 'person'])
    id = msg.value().decode('utf-8')
    requests.put('http://127.0.0.1:5000/object/' + id, json={"object": choice})


try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None: continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                sys.stderr.write('%% %s [%d] reached end at offset %din' %
                                    (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                raise KafkaException(msg.error())

        else:
            detect_object(msg)



finally:
    consumer.close()
