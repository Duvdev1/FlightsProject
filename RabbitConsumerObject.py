import pika


class RabbitConsumerObject:
    def __init__(self, q_name, callback):
        self.q_name = q_name
        self.callback = callback
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.q_name)

    def consume(self):
        self.channel.basic_consume(queue=self.q_name, on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
