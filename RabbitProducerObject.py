import pika


class RabbitProducerObject:
    def __init__(self, q_name):
        self.q_name = q_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.q_name)

    def publish(self, data):
        self.channel.queue_declare(queue=self.q_name)
        self.channel.basic_publish(exchange='', routing_key=self.q_name, body=data)
