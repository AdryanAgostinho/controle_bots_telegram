import sqlite3
import paramiko
from sshtunnel import SSHTunnelForwarder

# Substitua 'server_ip' pelo endereço IP do seu servidor Linux
# Substitua 'port' pela porta SSH do seu servidor
# Substitua 'your_database.db' pelo caminho e nome do seu banco de dados SQLite no servidor
# Substitua 'local_port' pelo número da porta local que será encaminhada para o servidor SQLite
# Substitua 'path/to/your/key.pem' pelo caminho para o seu arquivo .pem

server_ip = '18.230.186.171'
ssh_port = 22
database_path_on_server = 'path/to/your/remote/database.db'
local_port = 8888
pem_key_path = 'bd/Bot-Telegram.pem'

# Configurando a conexão SSH com o servidor
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server_ip, port=ssh_port, username='ubuntu', key_filename=pem_key_path)

# Configurando o encaminhamento de porta SSH para o servidor SQLite
with SSHTunnelForwarder(
    (server_ip, ssh_port),
    ssh_username='your_username',
    ssh_pkey=pem_key_path,
    remote_bind_address=('18.230.186.171', 22),
    local_bind_address=('0.0.0.0', local_port),
):
    # Conectando-se ao banco de dados SQLite usando a porta encaminhada
    conn = sqlite3.connect(f'18.230.186.171:{local_port}/{database_path_on_server}')

    cursor = conn.cursor()

    # Exemplo de consulta
    cursor.execute('SELECT * FROM sua_tabela')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

# Fechando a conexão SSH
ssh.close()
