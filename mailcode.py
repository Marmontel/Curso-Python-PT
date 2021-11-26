# objetivo

from email import message
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# corpo da mensagem do e-mail
msg = MIMEMultipart()
message = "E-mail teste recebido :)"

# credenciais e assuntos do e-mail

password = "desgostoalenda"
msg['From'] = "desgostoselfie@gmail.com"
msg['To'] = "alyssonmarmontelpereira@gmail.com"
msg['Subject'] = "Assunto 1 teste"

# Monta a conexão e envia o e-mail

msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
