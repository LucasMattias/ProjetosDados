import Funcoes
import random
import pymysql


contador = 0
con = pymysql.connect(host='localhost', database='Venda_veiculos', user='root', password= 'root', port=3306)
cur = con.cursor()
cpfs_cadastrados = []
residencia = Funcoes.capturar_municipio()
print(len(residencia))
cur.execute(f'CREATE TABLE IF NOT exists Pessoa(CPF BIGINT PRIMARY KEY,'
            f' Idade INT,'
            f' Municipio varchar(35),'
            f' Estado varchar(30),'
            f' Sexo varchar(12));')
sexo = random.randint(0,1)
acumulador = 0
acumulador_sexo = 0
while contador < 760000:
    if contador < 322032:
        numero_aleatorio = random.randint(1, 100)
        acumulador += numero_aleatorio
        if acumulador >= 147:
            acumulador -= random.randint(1,145)
            if acumulador >= 147:
                acumulador -= 146
        print(acumulador)
        pessoa = Funcoes.Pessoa(residencia[acumulador], cpfs_cadastrados, Sexo= sexo)
        print(f'Salvando a pessoa {contador+1}')
        cur.execute(f'INSERT INTO Pessoa(CPF, Idade, Municipio, Estado, Sexo) VALUES ({int(pessoa.Cpf)}, {pessoa.Idade}, "{pessoa.Municipio}", "{pessoa.Estado}", "Feminino");')
        con.commit()
        contador += 1
        del pessoa
    else:
        numero_aleatorio = random.randint(1, 100)
        acumulador += numero_aleatorio
        if acumulador >= 147:
            acumulador -= random.randint(1,145)
            if acumulador >= 147:
                acumulador -= 146
        print(acumulador)
        pessoa = Funcoes.Pessoa(residencia[acumulador], cpfs_cadastrados, Sexo= sexo)
        print(f'Salvando a pessoa {contador+1}')
        cur.execute(f'INSERT INTO Pessoa(CPF, Idade, Municipio, Estado, Sexo) VALUES ({int(pessoa.Cpf)}, {pessoa.Idade}, "{pessoa.Municipio}", "{pessoa.Estado}", "Masculino");')
        con.commit()
        contador += 1
        del pessoa
cur.close()
