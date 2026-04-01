import os
from flask import Flask, request, redirect
import mysql.connector
from dotenv import load_dotenv # Importa o leitor de .env

# Carrega as variáveis do arquivo .env para o sistema
load_dotenv()

app = Flask(__name__)

# Pega as configurações do .env (se não achar, usa padrões)
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "log_db")
}

def inicializar_banco():
    """Cria o banco e a tabela automaticamente se não existirem"""
    try:
        # Conecta sem especificar o banco primeiro (para poder criar o banco)
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        cursor = conn.cursor()
        
        # Cria o banco de dados
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        cursor.execute(f"USE {DB_CONFIG['database']}")
        
        # Cria a tabela de logs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS acessos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ip_publico VARCHAR(45),
                navegador_sistema TEXT,
                data_acesso DATETIME DEFAULT CURRENT_TIMESTAMP,
                url_destino TEXT
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Banco de dados pronto para uso!")
    except Exception as e:
        print(f"❌ Erro ao inicializar banco: {e}")

def salvar_no_banco(ip, user_agent):
    """Salva os dados coletados no MySQL"""
    try:
        conexao = mysql.connector.connect(**DB_CONFIG) # Usa o dicionário de config
        cursor = conexao.cursor()
        sql = "INSERT INTO acessos (ip_publico, navegador_sistema, url_destino) VALUES (%s, %s, %s)"
        cursor.execute(sql, (ip, user_agent, "https://www.youtube.com"))
        conexao.commit()
        cursor.close()
        conexao.close()
        print(f"✅ Log registrado: {ip}")
    except Exception as e:
        print(f"❌ Erro ao salvar log: {e}")

@app.route('/promocao')
def logger():
    ip_cliente = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    salvar_no_banco(ip_cliente, user_agent)
    return redirect("https://www.youtube.com")

if __name__ == '__main__':
    # Roda a criação do banco ANTES de ligar o servidor
    inicializar_banco()
    
    print(f"🚀 Servidor em http://127.0.0.1:5000/promocao")
    app.run(debug=True, host='0.0.0.0', port=5000)