# this file work with serializing mongodata to dictionary

def individual_serial(mail) -> dict:
    return {
        "id": str(mail["_id"]),
        "mail": mail["mail"],
        "subject": mail["subject"],
        "body": mail["body"]

    }

def list_serial(mails) -> list:
    return [individual_serial(mail) for mail in mails]