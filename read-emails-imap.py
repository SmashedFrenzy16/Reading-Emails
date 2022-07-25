import imaplib
import pprint

host = input("Enter IMAP host: ")
username = input("Enter username: ")
password = input("Enter password: ")

imap = imaplib.IMAP4_SSL(host)

imap.login(username, password)
imap.select('Inbox')

tmp, data = imap.search(None, 'ALL')
for num in data[0].split():
	tmp, data = imap.fetch(num, '(RFC822)')
	print('Message: {0}\n'.format(num))
	pprint.pprint(data[0][1])
	break
imap.close()
