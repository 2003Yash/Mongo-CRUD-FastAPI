# this file work with serializing mongodata to dictionary

## Serialize a single mail document to a dictionary
def individual_serial(mail) -> dict:
    return {
        "id": str(mail["_id"]),
        "mail": mail["mail"],
        "subject": mail["subject"],
        "body": mail["body"]

    }

# # Serialize a list of mail documents to a list of dictionaries
def list_serial(mails) -> list:
    return [individual_serial(mail) for mail in mails]