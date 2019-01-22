import json
import time

import pika
import requests

# delay to start rabbitmq
time.sleep(20)
print("Delay for rabbitmq")
# time.sleep(20)
print("Connecting to rabbit")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='wish', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def create_email_context(video_title, video_description):
    return """"
New Video Entry

A New video in your wishlist category was added to the catalogue.


Go Ahead and Log In to TrailerFlix :)

Title: {}

Description: {}

""".format(video_title, video_description)


def request_user_emails(categories):
    response = requests.request(method='GET', url='http://wishlist:8000/api/wish/users/?categories=' + str(categories))
    if response.status_code == 200:
        return [d['user_email'] for d in json.loads(response.text)['data'] if 'user_email' in d]


def send_email(email, context, subject):
    pass


def send_simple_message(email, context, subject):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox70a50c7be77a4a84b311ba55b9e0a218.mailgun.org/messages",
        auth=("api", "1270c7d9676cc65f73e88bfd893812aa-2d27312c-1ce90ada"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox70a50c7be77a4a84b311ba55b9e0a218.mailgun.org>",
              "to": email,
              "subject": subject,
              "text": context})


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    message = json.loads(body)
    emails = request_user_emails(message['categories'])
    email_title = "Your Wish Came True"
    email_context = create_email_context(message['title'], message['description'])
    emails = set(emails)
    for email in emails:
        if email:
            mail_response = send_simple_message(email, email_context, email_title)
            if mail_response:
                print("Email Sent")
            else:
                print("Could not send email to: {}".format(email))
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='wish')

channel.start_consuming()
