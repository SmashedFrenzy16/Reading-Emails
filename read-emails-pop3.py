import poplib

username = input("Enter username: ")
password = input("Enter password: ")
server = input("Enter POP3 server: ")
port = input("Enter port: ")

Mailbox = poplib.POP3_SSL(server, port)

Mailbox.user(username)

Mailbox.pass_(password)

messages = len(Mailbox.list()[1])
