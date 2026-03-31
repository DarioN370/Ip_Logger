# 🛡️ Link Logger - Capturador de Metadados (Estudo de Segurança)

Este projeto é um **IP Logger** invisível desenvolvido para fins educacionais. Ele demonstra como funciona o rastreamento de requisições HTTP, coleta de IPs e redirecionamento de tráfego, utilizando **Python (Flask)** e **MySQL**.

---

## 🚀 Como subir o sistema do zero

Siga este guia se você acabou de clonar este repositório em uma máquina limpa.

### 1. Instalação das Ferramentas Necessárias
Você precisará instalar os seguintes softwares:

* **Python 3.10+**: [Download oficial](https://www.python.org/downloads/) (Marque a caixa **"Add Python to PATH"**).
* **MySQL Community Server & Workbench**: [Download oficial](https://dev.mysql.com/downloads/installer/).
    * Escolha a instalação tipo **Full**.
    * Defina uma senha para o usuário `root` e guarde-a bem.
* **Ngrok** (Opcional): [Site Oficial](https://ngrok.com/) (Para gerar links públicos).

---

### 2. Configurando o Ambiente Local

1.  **Instale as dependências do Python**:
    Abra o terminal na pasta do projeto e execute:
    ```bash
    pip install flask mysql-connector-python python-dotenv
    ```

2.  **Configure as credenciais (.env)**:
    Crie um arquivo chamado `.env` na raiz do projeto e preencha com seus dados do MySQL:
    ```env
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=SUA_SENHA_AQUI
    DB_NAME=log_db
    ```

---

### 3. Execução do Programa

Para colocar o link no ar, execute o arquivo principal:
```bash
python app.py