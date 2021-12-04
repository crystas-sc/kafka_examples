from confluent_kafka import Consumer
import logging
# Create logger for consumer (logs will be emitted when poll() is called)
logger = logging.getLogger('consumer')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))
logger.addHandler(handler)

c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest',
    'session.timeout.ms': 60000,
    "log.connection.close": False,
    "log_level": 3,
    "log.queue": False
}, logger=logger)
TOPIC = 'my-topic'

def print_assignment(consumer, partitions):
    print('Assignment:', partitions)
    
def run_consumer():
    print(f'Starting consumer... for subscription to topic: {TOPIC}')
    c.subscribe([TOPIC], on_assign=print_assignment)

    while True:
        # print('Waiting for message...')
        msg = c.poll(1.0)
        # partitions = c.assignment()
        # print(f'Received message: {msg} partitions: {partitions} postition: {c.position(partitions)}')
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print(f"Received message:{msg.value().decode('utf-8')} from partition: {msg.partition()}")

    c.close()

if __name__ == '__main__':
    run_consumer()