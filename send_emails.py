import csv
import smtplib
import argparse
from email.message import EmailMessage
from urllib.request import urlopen

parser = argparse.ArgumentParser()
parser.add_argument("-u", required=True)
parser.add_argument("-p", required=True)
parser.add_argument("-f", required=True)
args = parser.parse_args()

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
server.starttls()
server.login(args.u, args.p)

with open(args.f, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)

    for row in reader:
        msg = EmailMessage()
        msg["From"] = args.u
        msg["To"] = row["toaddress"]
        msg["Subject"] = row["subject"]

        msg.set_content(
            f"Hello {row['firstname']} {row['lastname']},\n\n"
            f"This is an automated email.\n"
        )

        link = row["attachment link"].strip()
        if link:
            data = urlopen(link).read()
            filename = link.split("/")[-1] or "attachment"
            msg.add_attachment(
                data,
                maintype="application",
                subtype="octet-stream",
                filename=filename
            )

        server.send_message(msg)
        print("sent to", row["toaddress"])

server.quit()