from pydantic import BaseModel #pydantic is not a part of mongo
# pydantic is a data validation library in Python. It enforces type hints at runtime, and provides user friendly errors when data is invalid.
# BaseModel is a special class that comes from Pydantic. It's used to define the structure of the data that you want to work with.

# defining the structure of the data that you want to work with
class mail(BaseModel):
    mail: str
    subject: str
    body: str
