from coco_mailer import Client, EmailMessage

client = Client(client_secret="4910672670394566", config="3179170")

email = EmailMessage(
    subject="Welcome to FutureMail",
    to=["chiderapatrickk@gmail.com","lordyacey@gmail.com"],
    content="Thanks for joining us!",
    context={"username": "John", "app": "FutureMail"},
)

success, msg = client.send_mail(email)
print(success, msg)
