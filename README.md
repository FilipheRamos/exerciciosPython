# APS
def atendimentoPreferencial():
    while True:
      cpf = input('\tCPF: ').strip()
      if len(cpf) != 11 or not cpf.isdigit():
        print('\tCPF inválido.')
      else:
        break

    while True:
      nome = input('\tNome: ').capitalize().strip()
      if nome.replace(' ','').isalpha():
        break
      else:
          print('\tErro!! Por favor insira apenas texto. ')

    senhap = random.randint(1,1000)
    senhaconsultap.append((senhap, nome))
    print(f'\tSua senha preferencial é: {senhap}')
    return senhap

def atendimentoGeral(tamanho):
    while True:
      cpf = input('\tCPF: ')
      if len(cpf) != 11 or not cpf.isdigit():
        print('\tCPF inválido.')
      else:
        break

    while True:
      nome = input('\tNome: ').capitalize()
      if nome.replace(' ','').isalpha():
        break
      else:
          print('\tErro!! Por favor insira apenas texto. ')

    caracteres = string.ascii_letters + string.digits
    senhag = ''.join(random.choice(caracteres) for _ in range(tamanho)).upper()
    senhaconsultag.append((senhag, nome))
    print(f'\tSua senha geral é: {senhag}')
    return senhag

def consultaSenha():
  while True:
      z = input('\nDeseja consultar a Fila Preferencial, Geral ou Ambas?\n\t1.Preferencial\n\t2.Geral\n\t3.Ambas\nDigite a opção desejada\n').strip()
      if z == "1":
          consultaPreferenciais()
      elif z == "2":
          consultaGerais()
      elif z == "3":
          consultaPreferenciais()
          consultaGerais()
      else:
          print('Digite uma opção valida!')



      print('\nDeseja consultar novamente?\n\t1.Sim\n\t2.Não')
      resposta = input('Digite uma opção: \n ').strip()

      if resposta == "1":
        continue
      elif resposta =="2":
        break
      else:
        print('Desculpa, não entendi!')
        continue


def consultaPreferenciais():
    if senhaconsultap:
        print(f'\nSenhas da Fila Preferencial: {senhaconsultap}')
    else:
        print('\nNão há senhas na Fila Preferencial.')

def consultaGerais():
    if senhaconsultag:
        print(f'\nSenhas da Fila Geral: {senhaconsultag}\n')
    else:
        print('\nNão há senhas na Fila Geral.')

def chamarSenhas():
    while True:
        print(f'\nSenhas Fila Preferencia: {len(senhaconsultap)} ')
        print(f'Senhas Fila Geral: {len(senhaconsultag)}\n')
        y = input('Deseja chamar qual fila?\n\t1.Fila preferencial\n\t2.Fila geral\nDigite a opção desejada\n ').strip()
        if y == "1":
            if senhaconsultap:
                print(f'\nPróxima senha: {senhaconsultap.pop(0)}\n')
            else:
                print('A fila Preferencial está vazia!\n')
        elif y == "2":
            if senhaconsultag:
                print(f'\nPróxima senha: {senhaconsultag.pop(0)}\n')
            else:
                print('A fila Geral está vazia!\n')
        else:
            print('Digite uma opção valida!\n')

        a = input('Deseja chamar outra senha?\n\t1.Sim \n\t2.Não\nDigite uma opção: ').strip()
        if a == "1":
          continue
        elif a == "2":
          break
        else:
          print('Desculpa, não entendi!')
          continue

def menu():
  print("\nMENU DE GESTÃO DE ATENDIMENTO\n")
  print("Selecione uma das opções abaixo:")
  print('\t1.Cadastro Atendimento Preferêncial.')
  print('\t2.Cadastro Atendimento Geral.')
  print('\t3.Consulta de senhas.')
  print('\t4.Chamar senha')
  print('\t5.Finalizar')



def opcoes(opcao):

    if opcao == 1:
        atendimentoPreferencial()

    elif opcao == 2:
        atendimentoGeral(3)

    elif opcao == 3:
        consultaSenha()

    elif opcao ==4:
        chamarSenhas()

    elif opcao ==5:
        print("\nAtendimento finalizado.\nObrigado!")





def main():
    while True:
      menu()

      try:
        x = int(input('Escolha uma das opções acima: '))
        if 1 <= x <= 5:
            opcoes(x)
            continue
        else:
            print("opção inválida. Por favor, escolha um número entre 1 e 5.")
            continue
      except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")







#principal
import string
import random
senhaconsultap=[]
senhaconsultag = []


main()
