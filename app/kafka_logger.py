from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def log_action(user_id: int, action: str, timestamp: str):
    producer.send('logs', {'user_id': user_id, 'action': action, 'timestamp': timestamp})