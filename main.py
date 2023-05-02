from modulos import envia_email

credenciais = {"email_app":input("Digite seu email: "),
               "senha_app":input("Digite sua senha: ")}
destinatario = input("Digite o email de destino: ")
corpo_msg = {"assunto":input("Assunto: "),
             "mensagem":input("Mensagem: "),
             "anexo":{"tipo":input("Tipo do arquivo: "),
                      "caminho":input("Caminho do arquivo: ")} if input("Tem anexo? ").lower() in ["s","sim","tem"] else {}}

tentativa = envia_email.EnviarEmail(envia_email.ServidorSMTP.gmail())
tentativa.definir_credenciais(credenciais["email_app"], credenciais["senha_app"])
tentativa.definir_destinatario(destinatario)
tentativa.definir_mensagem(corpo_msg["assunto"], corpo_msg["mensagem"], corpo_msg["anexo"])

if tentativa.enviar():
    print("Email enviado com sucesso!!!")
else:
    print("Falha ao tentar enviar o email.")
