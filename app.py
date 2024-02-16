# #Instala os pacotes necessários do requirements
import subprocess
try:
	subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
	print("Pacotes instalados com sucesso!")
except subprocess.CalledProcessError as e:
	print("Erro ao instalar os pacotes:", e)
	

#Bibliotecas
import pandas as pd
import gspread
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import pytz


#Credenciais para envio
email_envio = 'xxxx'
senha_envio = 'xxxx'

#Infos para envio
nome_envio = 'xxxx'
assunto_mensagem = 'xxxx'
mensagem_envio = 'xxxx'


#Conexão com o sheets
code_sheets = 'xxxx'
gc = gspread.service_account(filename= 'key.json')
sh = gc.open_by_key(code_sheets)
ws_envio = sh.worksheet('Envio')
ws_historico = sh.worksheet('Historico')


#Verifica a quantidade de linhas para ver se tem algo a ser enviado
qt_linhas = len(ws_envio.get_all_records())

if qt_linhas > 0:

  #Pega os dados na planilha de envio e cria variavel de data de envio para controle
  df_envio = pd.DataFrame(ws_envio.get_all_records())
  data_envio = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d-%m-%Y %H:%M:%S')

  #Faz o login no servidor
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(email_envio,senha_envio)

    #Envia email de acordo com a quantidade de envios da aba envio
    for index, row in df_envio.iterrows():
      nome = row['nome'].split(' ')[0]
      email = row['email']

      msg = MIMEMultipart()
      msg['Subject'] = assunto_mensagem
      msg['From'] = nome_envio
      msg['To'] = email

      #Estrutura para envio
      corpo_email = f"""
      <html>
          <head>
              <style>
                  body {{
                      font-family: Georgia, Serif;
                      font-size: 14px;}}

                  .cabecalho {{
                    font-weight: bold;}}

                  .assinatura {{
                    color: #a9a9a9;
                    font-size: 12px;
                    font-weight: bold;}}
              </style>
          </head>
          <body>
              <p class="cabecalho">Olá, {nome}!</p>
              <p> {mensagem_envio} </p>

              <p class="assinatura"> Transformando o cenário do agro através da tecnologia. </p>
              <img src="cid:assinatura_imagem" alt="Assinatura" width="200" height="100">
          </body>
      </html>
      """

      msg.attach(MIMEText(corpo_email, 'html'))


      #Anexa a assinatura
      with open('assinatura.png', 'rb') as img_file:
          img_data = img_file.read()

      imagem = MIMEImage(img_data, name='Agrotech Connect')
      imagem.add_header('Content-ID', '<assinatura_imagem>')
      msg.attach(imagem)

      smtp.send_message(msg)

      #Inclui na aba de histórico
      df_historico = ws_historico.get_all_values()

      mensagem_envio = mensagem_envio.replace('<br>', '\n')
      inserir_historico = [email,mensagem_envio,data_envio]
      new_data = df_historico[1:] + [inserir_historico]
      ws_historico.update(f'A2:D{len(new_data) + 1}', new_data)
