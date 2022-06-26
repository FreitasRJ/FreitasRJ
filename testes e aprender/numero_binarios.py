
for a in range(32):
    temp = "{0:b}".format(a)

    print(f'{temp}  ==> {a}')

nota_100 = nota_50 = nota_10 = nota_5 = nota_1 = cont = 0   
nota_100_str = nota_50_str = nota_10_str = nota_5_str = nota_1_str = saida = controle = ""
retorno = [nota_100, nota_100_str, '', nota_50, nota_50_str, '', nota_10, nota_10_str, '', nota_5, nota_5_str, '', nota_1, nota_1_str]

controle = ['1', '0', '0', '1', '1']



if controle[4] != '0': # nota 1
    retorno[11] = ' e '

if controle[3] != '0' and controle[4] == '0': 
    retorno[8] = ' e '
    retorno[11] = ''

if controle[3] == '0':
    retorno[8] = ''
#__________________________________________-
if controle[2] != '0' and controle[3] == 0:
    retorno[5] = ' e '
    retorno[8] = ''

if controle[2] == '0':
    retorno[5] = ''
#__________________________________________

if controle[1] != '0' and controle[4] == '0': 
    retorno[2] = ' e '
    retorno[5] = ''

if controle[1] == '0':
    retorno[2] = ''
    
#__________________________________________
    
if controle[0] != '0' and controle[4] == '0': 
    #retorno[0] = ' e '
    retorno[2] = ''



            

print(retorno)

controle = '11111'

        