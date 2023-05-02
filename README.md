# Envia Email
Aplicativo simples para enviar emails em python.

# Suporte a Gmail
Esse aplicativo tem suporte ao gmail, para você integrar basta habilitar a autenticação de 2 fatores na sua conta Google e buscar pela opção de criar uma senha para aplicativo.

# Como usar em seus projetos
### 1. Acesse a pasta modulos e faça uma cópia do arquivo envia_email para o diretório do seu projeto
### 2. Faça a importação dentro do seu projeto com o seguinte bloco de código
```python
import envia_email
```
### 3. Faça a configuração básica do Envia Email
```python
gmail = envia_email.ServidorSMTP.gmail() # Criando um objeto do servidor préconfigurado gmail
envia_obj = envia_email.EnviarEmail(gmail) # Instanciando o objeto do Envia Email com o servidor préconfigurado do gmail
envia_obj.definir_credenciais("email@email.com", "senha1234") # Define as credenciais de login para o servidor SMTP
envia_obj.definir_destinatario("destinatario@email.com") # Define o email do destinatário
envia_obj.definir_mensagem("Assunto do email", "Mensagem") # Define o corpo da mensagem
```
### 4. Caso queira enviar 1 anexo, adicione o seguinte trecho de código e adapte-o
```python
anexo = envia_email.Anexo("txt", "C:\arquivo.txt") # Primeiro argumento é o tipo do arquivo e o segundo é o caminho para o arquivo
envia_obj.inserir_anexo(anexo) # Insere o anexo no corpo do email.
```
### 5. Agora vamos tentar enviar o email e caso ele retorne True, deu tudo certo.
```python
if envia_obj.enviar():
    print("Email enviado com sucesso!!!")
else:
    print("Falha ao tentar enviar o email.")
```
