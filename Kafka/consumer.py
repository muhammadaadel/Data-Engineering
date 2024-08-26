from confluent_kafka import Consumer, KafkaError, KafkaException
import sys

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

def msg_process (msg) :
    print("got a new message (group1): ", msg.value())

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
            msg_process(msg)
finally:
    consumer.close()
