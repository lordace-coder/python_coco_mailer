from coco_mailer import Client, EmailMessage

client = Client()

email = EmailMessage(
    subject="Welcome to Our App",
    to=["user@example.com"],
    html_file="emails/welcome.html",
    context=[
        {"key": "username", "value": "John"},
        {"key": "app_name", "value": "FutureMail"},
    ],
)

success, message = client.send_mail(email)
print(success, message)
