import os
import requests
from typing import List, Optional, Dict, Tuple, Union
from errors import CocoError


class EmailMessage:
    def __init__(
        self,
        subject: str,
        to: List[str],
        content: Optional[str] = None,
        html: Optional[Union[str, os.PathLike]] = None,
        context: Optional[Dict[str, str]] = None,
    ):
        self.subject = subject
        self.to = to
        self.content = content
        self.html = html
        self.context = context or {}

        self._validate()

    def _validate(self):
        if not self.subject:
            raise CocoError("Subject is required.")
        if not self.to or not all(isinstance(addr, str) for addr in self.to):
            raise CocoError("Valid recipient email addresses are required.")
        if not self.content and not self.html:
            raise CocoError(
                "Either plain content or HTML (string or file) must be provided."
            )

    def get_payload(self) -> Dict:
        html_content = None

        if self.html:
            if isinstance(self.html, (str, os.PathLike)) and os.path.exists(self.html):
                with open(self.html, "r", encoding="utf-8") as f:
                    html_content = f.read()
            else:
                html_content = str(self.html)

        return {
            "subject": self.subject,
            "to": self.to,
            "content": self.content,
            "html": html_content,
            "context": self.context,
        }


class Client:
    def __init__(self, client_secret: Optional[str] = None, url: Optional[str] = None):
        self.url = url or "http://127.0.0.1:8000"
        self.client_secret = client_secret or os.getenv("COCO_SECRET")

        if not self.client_secret:
            raise CocoError(
                "Client Secret was not set. "
                "Set it via the COCO_SECRET environment variable or pass it into the Client class."
            )

    def send_mail(self, message: EmailMessage) -> Tuple[bool, str]:
        try:
            headers = {
                "Authorization": f"Bearer {self.client_secret}",
                "Content-Type": "application/json",
            }

            payload = message.get_payload()

            response = requests.post(
                f"{self.url}/api/send/", headers=headers, json=payload, timeout=10
            )

            if response.status_code == 200:
                return True, "Mail sent successfully"
            return False, f"Failed to send mail: {response.text}"

        except requests.RequestException as e:
            return False, f"Error occurred: {str(e)}"
