1.Put the script and the CSV in the same folder.

2.CSV columns must be:
firstname,lastname,toaddress,subject,attachment link

3.Run it like this:
python send_emails.py -u youraddress@gmail.com -p your_app_password -f emails.csv

4.Use a Gmail app password, not your normal password.

5.If the attachment link is empty, the email is sent without attachment.
