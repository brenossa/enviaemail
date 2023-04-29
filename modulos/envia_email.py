import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class EnviarEmail:
    def __init__(self):
        pass

    def definir_credenciais(self, email, senha):
        self.email = email
        self.senha = senha

    def definir_destinatario(self, destinatario):
        self.destinatario = destinatario

    def definir_mensagem(self, assunto, mensagem, anexo):
        self.assunto = assunto
        self.mensagem = mensagem
        self.anexo = anexo

    def enviar(self):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.destinatario
        msg['Subject'] = self.assunto

        msg.attach(MIMEText(self.mensagem, 'plain'))

        if self.anexo.get("caminho"):
            with open(self.anexo["caminho"], "rb") as anexo:
                att = MIMEApplication(anexo.read(),_subtype=self.anexo["tipo"])
                att.add_header("Content-Disposition","attachment",filename=str(anexo.buffer.name))
                msg.attach(att)

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(self.email, self.senha)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        return True
