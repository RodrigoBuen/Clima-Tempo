☁️ Previsão do Tempo com API ClimaTempo + Envio por E-mail
Este projeto Python permite consultar a previsão do tempo para os próximos 15 dias usando a API do ClimaTempo, com opção de envio automático por e-mail.

📦 Funcionalidades
Consulta de cidade e obtenção do ID via API

Previsão completa para os próximos 15 dias:

Temperatura máxima e mínima

Probabilidade de chuva e precipitação

Índice UV e nível de risco

Descrição do clima

Envio automático do relatório por e-mail

🔧 Pré-requisitos
Python 3.x

Conta no ClimaTempo API

Conta de e-mail (de preferência Gmail)

📥 Instalação
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/previsao-tempo-email.git
cd previsao-tempo-email
Instale as dependências:

bash
Copiar
Editar
pip install requests
🔑 Configuração
Edite os seguintes campos no seu código:

python
Copiar
Editar
token = "Seu Token do clima tempo"
id_cidade = "Id da cidade"

# Configurações de e-mail
self.server.login("Email Login", "Senha do seu email")
"Seu email",
"Email do destinario"
Para descobrir o ID da cidade, defina pesquisa_cidade = True e execute o script.

▶️ Como Usar
1. Buscar o ID da cidade (opcional)
Defina pesquisa_cidade = True e execute o script:

bash
Copiar
Editar
python app.py
Digite o nome da cidade e copie o ID desejado.

2. Executar previsão do tempo
Altere pesquisa_cidade = False e defina o ID da cidade. Execute novamente:

bash
Copiar
Editar
python app.py
A previsão será exibida no terminal e enviada por e-mail.

🛡️ Observações de Segurança
Evite colocar senhas diretamente no código. Use variáveis de ambiente ou arquivos .env (veja bibliotecas como python-dotenv).

Ative a autenticação de dois fatores no Gmail e crie senhas de app se necessário.
