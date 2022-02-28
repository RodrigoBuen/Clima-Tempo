import requests
import json
import smtplib
from time import sleep

token = "Seu Token do clima tempo" # tem que cadastrar no site do clima tempo
id_cidade = "Id da cidade" # é so colocar pesquisa_cidade True digitar a cidade desejada e ver o id

pesquisa_cidade = False

class App:
    def __init__(self):
        self.choice()

    def choice(self):
        if pesquisa_cidade == True:
            nome_cidade = input('Informe o nome da cidade: ')
            url = f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={nome_cidade}&token={token}"
            response = requests.request("GET", url)
            resp_req = json.loads(response.text)

            for key in resp_req:
                id = key['id']
                nome = key['name']
                estado = key['state']
                pais = key['country']
                print(f"id: {str(id)} - stlocalesidate: {str(estado)}  - country: {str(pais)} - name: {str(nome)} \n")

            nova_cidade = input('Informe o ID da nova cidade ou 0(zero) para sair: ')

            if nova_cidade != "0":
                url = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/{token}/locales"
                payload = "localeId[]=" + nova_cidade
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
                response = requests.request("PUT", url, headers=headers, data=payload)
                print(response.text)

            else:
                exit()

        elif pesquisa_cidade != True:
            url = f'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{id_cidade}/days/15?token={token}'
            response = requests.request("GET", url)
            resp_req = json.loads(response.text)
            msg_tempo = ''

            for iten in resp_req['data']:
                date_consulte = iten.get('date_br')
                temp_max = iten['temperature']['max']
                temp_min = iten['temperature']['min']
                probability_rain = iten['rain']['probability']
                precipitation_rain = iten['rain']['precipitation']
                index_uv = iten['uv']['max']
                text_uv = ''
                text_prevision = iten['text_icon']['text']['pt']

                if float(index_uv) <= 2.9:
                    text_uv = 'Baixo Risco'

                elif float(index_uv) > 2.9 and float(index_uv) <= 5.9:
                    text_uv = 'Risco Moderado'

                elif float(index_uv) > 5.9 and float(index_uv) <= 7.9:
                    text_uv = 'Risco Alto'

                elif float(index_uv) > 7.9 and float(index_uv) <= 10.9:
                    text_uv = 'Risco Muito Alto'

                elif float(index_uv) > 11.0:
                    text_uv = 'Risco Extremo'

                msg_tempo += f'''
                    data: {date_consulte}
                    chuva: {probability_rain}% - {precipitation_rain}mm
                    temperatura: {temp_max}° max - {temp_min}° min
                    indice uv: {index_uv} ({text_uv})
                    {text_prevision} \n
                '''

    def send_email(self, msg_tempo=''):
        try:
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.login("Email Login", "Senha do seu email")
            self.server.sendmail(
                "Seu email",
                "Email do destinario",
                msg_tempo.encode())
            self.server.quit()

            print('Status: 200 -- OK')

            sleep(120)

        except:
            print('Não foi possivel enviar o email!!!')