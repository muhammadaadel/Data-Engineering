from confluent_kafka import Consumer, KafkaError, KafkaException
import sys
import requests
import os

me = 'DolZz-1'
groupId = me + '-group2'

conf = {
    'bootstrap.servers': '34.138.205.183:9094,34.138.104.233:9094,34.138.118.154:9094',
    'group.id': groupId,
    'enable.auto.commit': True,
    'auto.offset.reset': 'smallest'
}


consumer = Consumer(conf)
topics = [me]
consumer.subscribe(topics)

import cv2
IMAGES_DIR = "images"

def process_image(image_id):
    image_path = os.path.join(IMAGES_DIR, f"{image_id}.jpg")  # Assuming image extension is jpg; adjust if needed
    if os.path.exists(image_path):
        # Read the image using OpenCV
        img = cv2.imread(image_path)
        if img is not None:
            # Convert the image to black and white
            bw_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Save the black and white image
            cv2.imwrite(image_path, bw_image)
            print(f"Processed image {image_id} and saved as black and white.")
        else:
            print(f"Failed to read image {image_id}.")
    else:
        print(f"Image with ID {image_id} not found.")

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
            message_value = msg.value().decode('utf-8')
            process_image(message_value)
            requests.put('http://127.0.0.1:5000/object/' + message_value)
            print(f"Consumer group {'group2'}: Received message: {msg.value().decode('utf-8')}")


finally:
    consumer.close()
