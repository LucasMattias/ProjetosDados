import random
import Funcoes
import pymysql

cores= ['Branco', 'Preto', 'Cinza', 'Prata', 'Azul', 'Vermelho', 'Verde']
cambio = ['Automático', 'Manual']
con = pymysql.connect(host='localhost', user='root', password='root', database='Venda_veiculos', port=3306)
cur = con.cursor()
list_model = Funcoes.buscar_modelos()
list_CPF = Funcoes.obter_cpf()
acumulador_cores = 0
acumulador_cambio = 0
acumula_cpf = 0
for l in list_model:
    for v in range(1, l['Unidades_vendidas']+1):
        #Escolhe a cor aleatoriamente.
        aleatorio_cores = random.randint(1,5)
        acumulador_cores += aleatorio_cores
        if acumulador_cores >= 6:
            acumulador_cores -= random.randint(0,5)
            if acumulador_cores >= 6:
                acumulador_cores -= 5
        #Escolhe o cambio aleatoriamente.
        aleatorio_cambio = random.randint(0, 1)
        acumulador_cambio += aleatorio_cambio
        if acumulador_cambio >= 2:
            acumulador_cambio -= 2
            if acumulador_cambio >= 6:
                acumulador_cambio -= 5
        venda1= Funcoes.Venda(Cor= cores[acumulador_cores], Cambio= cambio[acumulador_cambio], Modelo=l['Veiculo'], CPF=list_CPF[acumula_cpf][0], Data_da_compra=l['Ano'])
        cur.execute(f'INSERT INTO Venda(Chassis, Cor, Cambio, Modelo, Cpf_comprador, data_compra) VALUES ({venda1.Chassis},"{venda1.Cor}", "{venda1.Cambio}", "{venda1.Modelo}", {venda1.CPF}, "{venda1.Data_da_compra}");')
        con.commit()
        acumula_cpf += 1
        print(f'Salvando a venda {v} do cpf {acumula_cpf}.')
        del venda1
    if acumula_cpf == 760000:
        break
con.close()