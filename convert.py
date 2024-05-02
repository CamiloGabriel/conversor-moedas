from currency_converter import ECB_URL, SINGLE_DAY_ECB_URL
from currency_converter import CurrencyConverter
from forex_python.converter import CurrencyCodes, CurrencyRates
from os import system
from colorama import init, Fore
import emoji
import time

init(autoreset=True)

c = CurrencyRates()
cd = CurrencyCodes()
cc = CurrencyConverter(ECB_URL)
ccsd = CurrencyConverter(SINGLE_DAY_ECB_URL)

system('cls')

first_date, last_date = cc.bounds ['USD']
Data_Conversao = last_date.strftime('%d/%m/%y')

moedas = cc.currencies

def instrucoes ():
        
    boas_vindas(emoji.emojize(f'Bem-vindo(a) ao Conversor Universal de Moedas! Fico muito feliz em ter você aqui 😁\nIrei converter o valor de uma moeda para outra com base no padrão internacional de moedas.\n{Fore.RED}⚠ OBS: Em finais de semanas e feriados, uso a data de conversão do último dia útil!😉 '))
    
    while True:

        
        press = input(f'{Fore.GREEN}Digite "Vamos!" para continuar ou "Sair" para encerrar o programa: ').lower()
        
        if press == 'sair':
            print(emoji.emojize(f"{Fore.BLUE}Poxa, tudo bem então, é uma pena que você já vai embora...😞"))
            exit()
        elif press == 'vamos' or press == 'vamos!':
            boas_vindas(emoji.emojize('🪙🪙🪙  CONVERSOR UNIVERSAL DE MOEDAS 🪙🪙🪙'))
            boas_vindas('- INSIRA O VALOR DESEJADO PARA CAMBIAR\n- INSIRA A MOEDA INICIAL\n- INSIRA A MOEDA DE CÂMBIO')
            boas_vindas('VALOR INICIAL')
            break 
            
        else:
            print(emoji.emojize(f"Entrada inválida, por favor digite apenas 'Vamos!' ou 'Sair'"))

def boas_vindas(txt):
    print('-'*len(txt))
    print(f'{Fore.GREEN}'+txt+'')
    print('-'*len(txt))

def boas_vindas2(txt):
    print('-'*len(txt))
    print(f'{Fore.WHITE}'+txt+'')
    print('-'*len(txt))


def moeda():
    print(f'{Fore.CYAN}\n1 - BRL\n2 - USD\n3 - OUTRO')
def moeda2():
    print(f'{Fore.WHITE}\n1 - BRL\n2 - USD\n3 - OUTRO')
def encerrar():
    print(f'{Fore.RED}0 - Encerrar programa\n')

    

def loop(txt):
    print('-'*len(txt))
    print(f'{Fore.GREEN}'+txt+'')
    print('-'*len(txt))



def question():
    print('\nVocê escolheu a opção 0\n')
    print(emoji.emojize(f'{Fore.LIGHTBLUE_EX}Tem certeza que deseja encerrar o programa?'))
    print(emoji.emojize(f'{Fore.LIGHTRED_EX}1 - Sim, certeza \n2 - Não, quero continuar! \n'))
    while True:
        try:
            saida = int(input('Escolha 1 ou 2: '))
            if saida == 1:
                encerramento()
                cont_regress(5)
                exit()

            elif saida == 2:
                print(emoji.emojize(f'{Fore.BLUE}Opa!\nEntão irei reiniciar para não ocorrer nenhum erro, ok?\nVamos lá!! 😎 '))
                reinicio(start)
                

            else:
                print(emoji.emojize(f'{Fore.RED}Digite apenas 1 ou 2 👻'))
            
        except ValueError: 
            print(emoji.emojize(f'{Fore.RED}Ei, você digitou algum caractere errado 👀'))

def certeza():

    boas_vindas(emoji.emojize('Tem certeza que deseja sair do programa?'))
    resp_question = None
    while resp_question not in (1, 2):
        question()
        try:
            resp_question = int(input("Selecione uma das 2 opções: "))
            if resp_question == 1:
                break
            elif resp_question == 2:
                continue
            else:
                print(f'{Fore.RED}Opção inválida, tente novamente!\n')

        except ValueError:
            print(f'{Fore.RED}Caractere inválido, tente novamente!\n')
         

def encerramento():
    print(emoji.emojize(f"{Fore.BLUE}Poxa, tudo bem então, é uma pena que você já vai embora...😞\n"))
    print(emoji.emojize(f"{Fore.BLUE}Mas espero que eu tenha sido útil a você. Fico feliz em ter te ajudado!\n"))
    print(emoji.emojize(f"{Fore.BLUE}E se caso você tenha gostado, por favor não esqueça de parabenizar meu criador Camilo Gabriel!\nO Linkedin dele é: 'https://www.linkedin.com/in/camilo-gabrielrm/' 😜"))
def cont_regress(segundos):
    print(f'{Fore.YELLOW}\nEncerrando o programa em...')
    for i in range(segundos, 0, -1):
        print(i, end=' ')  
        time.sleep(1)      

    print(f'{Fore.RED}Programa encerrado!\n')

def cont_regress_reinicio(segundos):
    print(f'{Fore.YELLOW}\nReiniciando o programa em...')
    for i in range(segundos, 0, -1):
        print(i, end=' ')  
        time.sleep(1)      

     

def new_convertion():
    print(f'{Fore.GREEN}\n1 - Sim\n0 - Não, quero encerrar o programa\n')

            

def reinicio(start):
    cont_regress_reinicio(3)
    start()




    
def conversao(cod_moeda_inicial, cod_moeda_cambio, valor_inicial):
    
    boas_vindas(emoji.emojize('CONVERTENDO...💸'))
    result = c.convert(cod_moeda_inicial, cod_moeda_cambio, valor_inicial)
    simbolo_moeda = cd.get_symbol(cod_moeda_inicial)
    simbolo_moeda_cambio = cd.get_symbol(cod_moeda_cambio)
    result = round(result, 2)
    print(Fore.LIGHTYELLOW_EX + f'Data da Cotação: {Data_Conversao}')
    print(emoji.emojize(f'{Fore.YELLOW}Pronto! {simbolo_moeda}{valor_inicial} {cod_moeda_inicial} equivalem a {simbolo_moeda_cambio}{ result} {cod_moeda_cambio}!🤑💰'))
    return result



def start():

    while True:    
        instrucoes()

        try:
            valor_inicial = float(
                input(f"{Fore.GREEN}Insira o valor desejado para a operação: \n").replace(',','.'))
            break
        except ValueError:
            print(
                emoji.emojize(f'{Fore.RED}Ah não!😓\nPor favor, insira um valor válido'))
            continue
                

    # 2 Bloco : Inserir moeda inicial
    boas_vindas('SELECIONE A MOEDA INICIAL')
    cod_moeda_inicial = None
    while cod_moeda_inicial not in (1,2,3,0):
        moeda()
        encerrar()
        try:
            cod_moeda_inicial = int(input("Selecione uma das 4 opções: "))
            
            if cod_moeda_inicial == 1:
                cod_moeda_inicial = 'BRL'
                print("Código escolhido:", cod_moeda_inicial)
                break
            elif cod_moeda_inicial == 2:
                cod_moeda_inicial = 'USD'
                print("Código escolhido", cod_moeda_inicial)
                break
            elif cod_moeda_inicial == 3:
                cod_moeda_inicial = input(
                    '\nDigite o código da moeda de sua escolha (3 dígitos):').upper()
                print('Código de escolha do país de operação:', cod_moeda_inicial)
                break

            elif cod_moeda_inicial == 0:
                question()

            else:
                print(emoji.emojize(f'{Fore.RED}Digite apenas uma das 4 opções acima!\n'))       
        except ValueError:
            print(emoji.emojize(f'{Fore.RED}Ei, você digitou algum caractere errado 👀'))
        
        

                
    boas_vindas2('SELECIONE A MOEDA DE CÂMBIO')
    cod_moeda_cambio = None
    while cod_moeda_cambio not in (1,2,3,0):
        moeda2()
        encerrar()
        try:
            cod_moeda_cambio = int(input("Selecione uma das 3 opções: "))
            if cod_moeda_cambio == 1:
                cod_moeda_cambio = 'BRL'
                print("Código escolhido", cod_moeda_cambio)
                
                break
            elif cod_moeda_cambio == 2:
                cod_moeda_cambio = 'USD'
                print("Código escolhido", cod_moeda_cambio)
                
                break
            elif cod_moeda_cambio == 3:
                cod_moeda_cambio = input(
                    '\nDigite o código da moeda de sua escolha (3 dígitos):').upper()
                print('Código escolhido', cod_moeda_cambio)
                
                break
            elif cod_moeda_cambio == 0:
                question()
                
            else:
                print(emoji.emojize(f'{Fore.RED}Digite apenas uma das opções de 0 a 3 👻'))
            
        except ValueError:
            print(emoji.emojize(f'{Fore.RED}Ei, você digitou algum caractere errado 👀'))

    
    
    conversao(cod_moeda_inicial, cod_moeda_cambio, valor_inicial)
            
            

    loop('DESEJA FAZER OUTRA CONVERSÃO?🤓')
    resposta = None
    while resposta not in (1,0):
        new_convertion()
        try:
            resposta = int(input('Digite uma das duas opções: '))
            if resposta == 1:
                reinicio(start)
                
                        
            elif resposta == 0:
                print('Código escolhido', resposta)
                encerramento()
                cont_regress(5)
                exit()

            else:
                print(emoji.emojize(f'{Fore.RED}Digite apenas uma das opções de numéricas disponíveis 👻'))

        except ValueError:
            print(emoji.emojize(f'{Fore.RED}Ei, você digitou algum caractere errado 👀'))

start()






        