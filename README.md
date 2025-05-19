# ☁️ Clima Tempo - Previsão do Tempo + Envio por E-mail

Projeto em Python que utiliza a **API do ClimaTempo** para consultar a previsão do tempo dos próximos 15 dias e enviar o relatório por **e-mail automaticamente**.

---

## 📌 Funcionalidades

- 🔍 Pesquisa de cidade e ID via API
- 📆 Previsão para os próximos 15 dias:
  - 🌡️ Temperatura máxima e mínima
  - 🌧️ Probabilidade de chuva e precipitação
  - 🌞 Índice UV com classificação de risco
  - 📝 Descrição do clima em português
- 📧 Envio automático da previsão por e-mail

---

## 🛠️ Requisitos

- Python 3.x
- Biblioteca `requests` (instalável via `pip`)
- Conta no [ClimaTempo API](https://advisor.climatempo.com.br/)
- Conta de e-mail (recomendado: Gmail)

---

## 🚀 Como Usar

### 1. Clonar o Repositório

git clone https://github.com/RodrigoBuen/Clima-Tempo.git
cd Clima-Tempo

---

### 2. Instalar Dependência
pip install requests

---

### 3. Configurar Token e ID da Cidade
Abra o arquivo .py e configure:

- token = "SEU_TOKEN"
- id_cidade = "ID_DA_CIDADE"
- Você pode obter o ID da cidade executando o código com pesquisa_cidade = True.

---

### 4. Configurar Envio por E-mail
Substitua os campos do método send_email com seus dados de e-mail:

- self.server.login("seu_email@gmail.com", "sua_senha")
- "seu_email@gmail.com",
- "destinatario@gmail.com"
- ⚠️ Use uma senha de aplicativo no Gmail para maior segurança.

---

🖼️ Exemplo de Saída

- data: 20/05/2025
- chuva: 80% - 10mm
- temperatura: 28° max - 19° min
- indice uv: 9.3 (Risco Muito Alto)
- Parcialmente nublado com pancadas de chuva

---

🧪 Testar o Programa
Para buscar o ID de uma cidade:

- pesquisa_cidade = True
- Para obter a previsão e enviar por e-mail:

- pesquisa_cidade = False
- Execute com:
python nome_do_arquivo.py

---

🔐 Segurança
- Evite deixar senhas no código. Use variáveis de ambiente ou um arquivo .env.

- Use senhas de aplicativo do Gmail se tiver autenticação em 2 etapas.

📄 Licença
- Este projeto está sob a licença MIT.
