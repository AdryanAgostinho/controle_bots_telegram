import bd 


try:
    con = bd.conexao.conectarbot()
    cursor = con.cursor()
    sql = "SELECT id_tele,nome,cod_rca,cod_magento,bloqueado FROM users"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    print(resultado)

except Exception as E:
    print("erro : " + str(E))