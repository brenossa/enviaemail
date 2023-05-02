from modulos import envia_email

credenciais = {"email_app":input("Digite seu email: "),
               "senha_app":input("Digite sua senha: ")}
destinatario = input("Digite o email de destino: ")
corpo_msg = {"assunto":input("Assunto: "),
             "mensagem":input("Mensagem: ")}

tentativa = envia_email.EnviarEmail(envia_email.ServidorSMTP.gmail())
tentativa.definir_credenciais(credenciais["email_app"], credenciais["senha_app"])
tentativa.definir_destinatario(destinatario)
tentativa.definir_mensagem(corpo_msg["assunto"], corpo_msg["mensagem"])
tem_anexo = True if input("Tem anexo? ").lower() in ["s","sim","tem"] else False

if tem_anexo:
    anexo = envia_email.Anexo(input("Tipo do arquivo: "), input("Caminho do arquivo: "))
    tentativa.inserir_anexo(anexo)

if tentativa.enviar():
    print("Email enviado com sucesso!!!")
else:
    print("Falha ao tentar enviar o email.")
