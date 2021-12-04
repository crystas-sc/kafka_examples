from confluent_kafka import Producer
import time
p = Producer({'bootstrap.servers': 'kafka:9092'})
TOPIC = 'my-topic'
interval = 10

def run_producer():
    """Runs the Producer"""
    count = 1
    while True:
        print(f"Producer: Sending message to topic {TOPIC}")
        p.produce(TOPIC, f"Hello World!!, This is my {count} message".encode("utf-8"))
        count += 1
        # p.flush()
        time.sleep(interval)
    


if __name__ == '__main__':
    run_producer()




