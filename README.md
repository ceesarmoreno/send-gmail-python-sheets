# send-gmail-python-sheets
**Script para envio automatizado via python utilizando gmail para os remetentes contidos no Google Sheets**

- Para realizar o envio, basta colocar o nome e email preenchidos na aba de Envio. A aba de Historico é apenas para guardar as mensagens que ja foram enviadas, sendo assim, ele é alimentada automaticamente conforme é enviado.
- O envio só acontece caso tenha pelo menos 1 registro preenchido na aba de Envio.


### Configurações

#### 1. Senhas de app
- Acesse https://myaccount.google.com/u/3/security
- Habilite a autenticação de dois fatores
- Desabilite a opção Navegação segura com maior proteção para sua conta caso esteja habilitada
- Acesse https://myaccount.google.com/u/3/apppasswords para criar a senha de app (Importante salvar a senha, porque aparece apenas uma vez)

![image](https://github.com/ceesarmoreno/send-gmail-python-sheets/assets/63748142/d2f19933-b651-4f2d-9d03-fb814fe172e7)


#### 2. API Google Sheets
- Acesse: https://console.cloud.google.com/welcome/new e caso não tenha um projeto criado, é necessário criar um.
- Ative a API Google Sheets em **APIs e serviços**
- Crie uma credencial utilizando a opção **Conta de serviço**
- Crie uma nova **chave JSON**
- Guarde o email da credencial e chave que foram criadas

![image](https://github.com/ceesarmoreno/send-gmail-python-sheets/assets/63748142/9a47845a-887a-4e5b-aba0-9f62c7266a21)

![image](https://github.com/ceesarmoreno/send-gmail-python-sheets/assets/63748142/0fe99fe3-b4ed-4e72-8a8b-d5a69358333c)

![image](https://github.com/ceesarmoreno/send-gmail-python-sheets/assets/63748142/24401372-5e2e-4508-b888-ea8c9b7074d4)



#### 3. Planilha Google Sheets
- Crie uma planilha e compartilhe com o email da credencial que foi criada anteriormente, com a opção de Editor
- Crie uma planilha chamada de Envio com duas colunas: nome e email
![image](https://github.com/ceesarmoreno/send-gmail-python-sheets/assets/63748142/bc5b78e4-cb94-47ad-85b0-0455a8e003a5)


- Crie uma planilha chamada de Historico com três colunas: email, mensagem e data_envio
![image](https://github.com/ceesarmoreno/send-gmail-python-sheets/assets/63748142/ba1506a5-5457-4ed4-80e9-aa8ae578adfe)

  
- Copie o código da planilha. Link de exemplo: docs.google.com/spreadsheets/d/codigo_planilha/xxxxxxxxxx
![image](https://github.com/ceesarmoreno/send-gmail-python-sheets/assets/63748142/dcefeb4b-c8f6-499e-b394-f09aff2412ce)


#### 3. Alterações de variáveis no código
- Altere a variavel email_envio com o email que enviará
- Altere a variavel senha_envio com a senha de app criada
- Altere a variavel nome_envio para definir o nome do remetente
- Altere a variavel assunto_mensagem para definir o assunto
- Altere a variavel mensagem_envio para definir a mensagem de envio (para quebra de linhas é necessário utilizar br entre o simbolo de maior e menor)
- Altere a variavel code_sheets com o código da planilha 
- Suba o arquivo da chave json da credencial gerada no mesmo diretório do projeto e renomeie como 'key' (tem que ficar como key.json)

  ![image](https://github.com/ceesarmoreno/send-gmail-python-sheets/assets/63748142/53c11963-ecf6-46bd-94b7-e545d4812e8f)

