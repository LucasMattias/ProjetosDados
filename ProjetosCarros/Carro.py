import Funcoes
import pymysql


con = pymysql.connect(host='localhost', database='Venda_veiculos', user='root', password= 'root', port=3306)
cur = con.cursor()
veiculos = Funcoes.ler_Veiculos()
cur.execute(f'CREATE TABLE IF NOT exists Veiculos(Veiculo varchar(35) PRIMARY KEY,'
            f' Montadora varchar(30),'
            f' Categoria varchar(30));')
veiculos_inseridos = []
for l in veiculos:
    if l['Veiculo'].upper() not in veiculos_inseridos:
        cur.execute(f'INSERT INTO  Veiculos(Veiculo, Montadora, Categoria) VALUES ("{l["Veiculo"]}", "{l["Montadora"]}", "{l["Categoria"]}");')
        con.commit()
        veiculos_inseridos.append(l['Veiculo'].upper())
con.close()