from pydantic import BaseModel

class mail(BaseModel):
    mail: str
    subject: str
    body: str
