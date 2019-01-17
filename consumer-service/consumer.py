import re
import pika
import time
import requests

# delay to start rabbitmq
time.sleep(20)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='wish', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def request_user_emails(categories):
    category_list = ','.join(categories)
    response = requests.request(method='GET', url='wishlist:8000/api/wish/users/?categories='+category_list)
    if response.status_code == 200:
        return response.json()


def send_email(email, context):
    pass


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    categories =  re.findall(r'\d+', body)
    emails = request_user_emails(categories)
    context = 'New Video Added'
    for email in emails:
        send_email(email, context)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='wish')

channel.start_consuming()
