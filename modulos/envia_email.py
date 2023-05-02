import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class ServidorSMTP:
    def __init__(self, host: str, porta: int):
        self.host = host
        self.porta = porta
    
    @classmethod
    def gmail(cls):
        return cls("smtp.gmail.com",587)

class Anexo:
    def __init__(self, tipo: str, caminho: str):
        self.tipo = tipo
        self.caminho = caminho

class EnviarEmail:
    def __init__(self, servidor: ServidorSMTP):
        self.host = servidor.host
        self.porta = servidor.porta
        self.tem_anexo = False

    def definir_credenciais(self, email: str, senha: str):
        self.email = email
        self.senha = senha

    def definir_destinatario(self, destinatario: str):
        self.destinatario = destinatario

    def definir_mensagem(self, assunto: str, mensagem: str):
        self.assunto = assunto
        self.mensagem = mensagem

    def inserir_anexo(self, anexo: Anexo):
        self.anexo = anexo
        self.tem_anexo = True

    def enviar(self):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = self.destinatario
        msg['Subject'] = self.assunto

        msg.attach(MIMEText(self.mensagem, 'plain'))

        if self.tem_anexo:
            with open(self.anexo.caminho, "rb") as anexo:
                att = MIMEApplication(anexo.read(),_subtype=self.anexo.tipo)
                att.add_header("Content-Disposition","attachment",filename=str(os.path.basename(self.anexo.caminho)))
                msg.attach(att)

        s = smtplib.SMTP(self.host, self.porta)
        s.starttls()
        s.login(self.email, self.senha)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        return True
