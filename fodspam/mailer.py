import smtplib

SERVER = "gold1wmbx002.ex.goldcorp.net"
FROM = "gary.graham@goldcorp.com"
TO = ["gary.graham@goldcorp.com"]

SUBJECT = "test"
TEXT = "test12"


if __name__ == '__main__':
	message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\ %s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	server = smtplib.SMTP(SERVER)
	server.loggin("gary.graham", "Muss0ssum!")
	server.sendmail(FROM, TO, message)
	server.quit()

