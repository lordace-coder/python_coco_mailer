# Coco Mailer

**Coco Mailer** is a simple, yet powerful Python library for sending emails via an API. It supports both plain text and HTML email content, dynamic templating, and file-based HTML content. Built with flexibility and ease of use in mind, Coco Mailer allows you to send emails quickly and efficiently using just a few lines of code.

## Features

- Send emails with plain text or HTML content
- HTML email content from a file or string
- Context-based templating for dynamic content
- Easy-to-use API with a straightforward client
- Error handling and validation

## Installation

To install Coco Mailer, simply use `pip`:

```bash
pip install coco_mailer
```

## Usage

### 1. Initialize the Client

```python
from coco_mailer import Client

# Initialize with your client secret and config
client = Client(client_secret="your-client-secret", config="your-email-config")

# Or use environment variables COCO_SECRET and COCO_CONFIG
client = Client()
```

### 2. Create an Email Message

```python
from coco_mailer import EmailMessage

email = EmailMessage(
    subject="Your Subject",
    to=["recipient@example.com"],
    content="This is the plain text content.",
    html="<p>This is the HTML content.</p>",  # Or provide a path to an HTML file
    context={"name": "John Doe", "coupon_code": "12345"},
)
```

The `EmailMessage` object accepts the following parameters:

- `subject (str)`: The subject of the email
- `to (List[str])`: A list of recipient email addresses
- `content (Optional[str])`: Plain text content of the email
- `html (Optional[Union[str, os.PathLike]])`: HTML content, either as a string or path to an HTML file
- `context (Optional[Dict[str, str]])`: A dictionary of key-value pairs to replace in your template

### 3. Send the Email

```python
success, message = client.send_mail(email)

if success:
    print("Email sent successfully!")
else:
    print(f"Failed to send email: {message}")
```

## Error Handling

The `CocoError` is raised when validation or other errors occur. Example usage:

```python
from coco_mailer import EmailMessage, Client, CocoError

try:
    email = EmailMessage(
        subject="Welcome to Coco",
        to=["newuser@example.com"],
        content="Hello! This is a welcome message.",
        html="<p>Hello! This is a <strong>welcome</strong> message.</p>",
    )
    client = Client(client_secret="your-client-secret")
    success, message = client.send_mail(email)

    if success:
        print("Email sent!")
    else:
        print(f"Error: {message}")
except CocoError as e:
    print(f"CocoError: {str(e)}")
```

## Advanced Features

### Email Payload Structure

```json
{
  "subject": "Your Subject",
  "to": ["recipient@example.com"],
  "content": "This is the plain text content.",
  "html": "<p>This is the HTML content.</p>",
  "context": { "name": "John Doe", "coupon_code": "12345" }
}
```

### HTML Content Support

You can use either a string or a file for HTML content:

```python
# Using a string
html_content = "<h1>Welcome to Coco Mailer!</h1>"

# Using a file path
html_content = "path/to/your/email_template.html"
```

### Client Options

- `url`: The base URL of the email API (defaults to http://127.0.0.1:8000)
- `client_secret`: Your secret key for API authentication (required)
- `config`: Your email configuration identifier (required)

Both `client_secret` and `config` can be provided either directly or through environment variables (`COCO_SECRET` and `COCO_CONFIG`).

Example with custom URL:

```python
client = Client(
    url="https://api.coco.com",
    client_secret="your-client-secret",
    config="your-email-config"
)
```

## License

This package is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Please fork this repository, submit a pull request, and ensure all tests pass before submitting your changes.

For any issues or support, feel free to open an issue on the GitHub repository.
