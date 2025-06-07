import argparse
import ssl
import textwrap
import base64
from email.message import EmailMessage
import google.auth
from googleapiclient.discovery import build

# My app.
pythonApp = argparse.ArgumentParser(
    prog="pythoncommandlineapp",
    formatter_class=argparse.RawTextHelpFormatter,
    description=textwrap.dedent(f"""\
    Python {__file__}
       +=======================================+
       =      IbrahimCPS Command Line App.     =
       +=======================================+
       FOLLOW THE INSTRUCTION...
    """),
    epilog=textwrap.dedent("""\
     Example:
       pythoncommanlineapp.py -t toUser@gmai.com -s subjectFor -m messageFor
       pythoncommanlineapp.py -f fromEmail@gmail.com -p password -t toUser@gmai.com -s subjectFor -m messageFor
    """),
    exit_on_error=True
)

# Optional args.
pythonApp.add_argument("-t", "--toUser", required=True, help="Send to email.", type=str, action="store")
pythonApp.add_argument("-s", "--subjectFor", required=True, help="Subject for the email.", type=str, action="store")
pythonApp.add_argument("-m", "--messageFor", required=True, help="Message", type=str, action="store")

# Optional args
pythonApp.add_argument("-v", "--verbosity", help="View in details", action="store_true")

# Attaching args to python app instance.
args = pythonApp.parse_args()

# My Data Initiallization
toUser = args.toUser
subjectFor = args.subjectFor
messageFor = args.messageFor

# Create a secured SSL context
context = ssl.create_default_context()


# Send Mail
def sendMail(t, s, m):
    # Getting permisstion.
    creds, _ = google.auth.default()

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message.set_content(m)

        message['From'] = "itsmecps4all@gmail.com"
        message['To'] = t
        message['Subject'] = s

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        service.users().messages().send(userId="me", body=create_message).execute()
        return True
    except:
        return False


# Sender.
fromUser = "itsmecps4all@gmail.com"

if args.verbosity:
    print(__file__)

    # Sending mail
    if sendMail(toUser, subjectFor, messageFor):
        print()
        print()
        print(f"Sender: {fromUser}")
        print(f"Reciver: {toUser}")
        print(f"Subject:: {subjectFor}")
        print(f"Message: {messageFor}")
        print()
        print()
        print("Send Successfull...")
    else:
        print()
        print()
        print(f"Sender: {fromUser}")
        print(f"Reciver: {toUser}")
        print(f"Subject:: {subjectFor}")
        print(f"Message: {messageFor}")
        print()
        print()
        print("Message not send...")
        print("""Network Error!  error network connection""")

else:
    print(__file__)

    # Sending mail
    if sendMail(toUser, subjectFor, messageFor):
        print("Send Successfull...")
    else:
        print("Message not send...")
        print("""Network Error!  error network connection""")
