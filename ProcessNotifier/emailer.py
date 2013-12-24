import smtplib


class Email():
    """Object containing the necessary commands to send an email through the local relay."""

    def __init__(self, to, proc, time_elapsed, time_threshold,
                 percent_threshold, cpu_or_ram):
        self.TO = to
        self.SUBJECT = proc + ' Idling Notification'
        self.TEXT = '''Your process appears to have finished running, as it has been idling for <b>%s</b> seconds under a threshold of <b>%s</b> percent <b>%s</b> usage.
		<br>
		<br>
		<table border="1">
		<tr>
			<td>Process:</td><td> %s</td>
		</tr>
		<tr>
			<td>Elapsed Time:</td> <td>%s</td>
		</tr>
		</table>
        <br><br> ''' % ( time_threshold, percent_threshold, cpu_or_ram, proc, time_elapsed)
        self.server = smtplib.SMTP('10.19.110.18', 25)

    def send_email(self):
        self.server.ehlo()
        BODY = '\r\n'.join(['To: %s' % self.TO,
                            'From: Process Notification Bot',
                            'Subject: %s' % self.SUBJECT,
                            'MIME-Version: 1.0',
                            'Content-type: text/html',
                            '', self.TEXT])
        try:
            print("Attempting to send mail...")
            self.server.sendmail("Gary@whatever.com", self.TO, BODY)
            print ('email sent')
        except:
            print ('error sending mail')
        self.server.quit()
