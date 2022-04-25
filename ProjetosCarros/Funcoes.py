import csv
import random
import pymysql
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


con = pymysql.connect(host='localhost', user='root', password='root', database='Venda_veiculos', port=3306)
cur = con.cursor()

def capturar_municipio():
    print('******* CAPTURANDO MUNICIPIOS *******')
    municipios = []
    #A intenção é pegar apenas os 150 primeiro municipios
    contador = 0
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil_acima_de_cem_mil_habitantes')
    filtrar_tabela = driver.find_elements(By.TAG_NAME, 'tbody')
    for filtro in filtrar_tabela:
        contador += 1
        listas_municipios = filtro.find_elements(By.TAG_NAME, 'tr')
        if contador > 1:
            contador = 0
            for lista in listas_municipios:
                municipios_html = lista.find_elements(By.TAG_NAME, 'a')
                contador += 1
                municipio_temp = dict()
                for n, municipio_estado in enumerate(municipios_html):
                    if len(municipios_html) == 3:
                        if n == 0:
                            municipio = municipio_estado.text
                            municipio_temp['Municipio'] = municipio
                        if n == 2:
                            estado = municipio_estado.text
                            municipio_temp['Estado'] = estado
                    elif len(municipios_html) == 2:
                        if n == 0:
                            municipio = municipio_estado.text
                            municipio_temp['Municipio'] = municipio
                        if n == 1:
                            estado = municipio_estado.text
                            municipio_temp['Estado'] = estado
                    else:
                        pass
                if 'Municipio' in municipio_temp:
                    if municipio_temp.get('Municipio') == '':
                        pass
                    else:
                        municipios.append(municipio_temp)
                if contador > 150:
                    break
    driver.close()
    return list(municipios)

def geraCPF():
    cpf = list()
    for s in range (0,3):  #Faz o sorterio dos 3 grupos que compõem a base
        for c in range(0, 3): #Faz o sorterio dos 3 números que compõem o grupo.
            c = random.randint(0, 9)
            cpf.append(c)
        if s != 2:
            cpf.append('.')
    cpfFormatado = ''
    for i in cpf:  #Monta o CPF de forma formatada.
        cpfFormatado += str(i)
    acumulador = 0  #Utilizado apenas nos cálculos
    multiplicador = 10
    base = cpfFormatado[0:11].replace('.', '')
    for i in base:  #Calcula o primeiro digito verificador
        multi = multiplicador * int(i)
        acumulador += multi
        multiplicador -= 1
    resultBase = 11 - (acumulador % 11)
    digito1 = 9 - resultBase
    if digito1 < 0:
        cpfFormatado += '-0' #Salva o primeiro digito como 0
    else:
        digito1 = str(digito1)
        cpfFormatado += f'-{digito1}'  #Ou salva o resultado de resultBase como primeiro digito verificador.
    base = cpfFormatado[0:13].replace('.', '')
    base = base.replace('-', '')
    multiplicador = 10
    acumulador = 0
    for i in base:  #Calcula o segundo numeral do verificador
        multi = (multiplicador + 1) * int(i)
        acumulador += multi
        multiplicador -= 1
    verificador2 = 11 - (acumulador % 11)
    digito2 = 9 - verificador2
    if digito2 < 0:
        cpfFormatado += '0'
    else:
        cpfFormatado += f'{verificador2}'
    return cpfFormatado

def obter_cpf():
    cur.execute(f'select CPF from pessoa;')
    consulta = cur.fetchall()
    con.commit()
    return consulta

def gerar_Municipio():
    municipio_capturado = capturar_municipio()
    return municipio_capturado

def definindo_cpf(cpfs_cadastrados):
    sair = False
    while sair == False:
        cpf_pessoal = geraCPF()
        cpf_pessoal = cpf_pessoal.replace('.', '').replace('-', '')
        if cpf_pessoal in cpfs_cadastrados:
            pass
        else:
            cpfs_cadastrados.append(cpf_pessoal)
            sair = True
            return cpf_pessoal

def ler_Veiculos():
    veiculos_totais = []
    with open('Vendas.CSV', 'r', encoding='utf-8') as vd:
        vendas = csv.reader(vd, delimiter=';')
        vendas.__next__()
        for i in vendas:
            marcador = 0
            veiculos_parc = {'Veiculo': i[2], 'Montadora': i[3], 'Categoria': i[1]}
            if veiculos_totais != '':
                for l in veiculos_totais:
                    if veiculos_parc['Veiculo'] == l['Veiculo']:
                        marcador = 1
                    else:
                        pass
            if marcador == 0:
                veiculos_totais.append(veiculos_parc)
    return veiculos_totais

def gerar_chassis(cur,con):
    while True:
        chassis_novo = random.randint(111111111111, 999999999999)
        cur.execute(f'select * from venda where chassis = {chassis_novo};')
        consulta = cur.fetchall()
        if not consulta or consulta == ():
            break
    return chassis_novo

def buscar_modelos():
    veiculos_totais = []
    with open('Vendas.CSV', 'r', encoding='utf-8') as vd:
        vendas = csv.reader(vd, delimiter=';')
        vendas.__next__()
        for i in vendas:
            veiculos_parc = {'Veiculo': i[2], 'Unidades_vendidas':  int(i[4].replace('.', '')) // 10, 'Ano': i[0]}
            veiculos_totais.append(veiculos_parc)
    return veiculos_totais

class Pessoa:
    def __init__(self, residencia, cpfs_cadastrados, Municipio= '', Estado= '', Sexo = ''):
        self.Idade = random.randint(18,65)
        self.Municipio = residencia['Municipio']
        self.Estado = residencia['Estado']
        self.Sexo = Sexo
        self.Cpf = definindo_cpf(cpfs_cadastrados)

class Venda:
    def __init__(self, Cor='', Cambio='', Modelo = '', CPF='', Data_da_compra=''):
        self.Chassis = gerar_chassis(cur, con)
        self.Cor = Cor
        self.Cambio = Cambio
        self.Modelo = Modelo
        self.CPF = CPF
        self.Data_da_compra = Data_da_compra


