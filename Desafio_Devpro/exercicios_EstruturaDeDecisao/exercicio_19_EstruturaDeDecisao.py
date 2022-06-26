'''
19 - Faça um Programa que leia um número inteiro menor que 1000 e
    imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula
    entre outros. Exemplo:
    
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,
    305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

'''

while True:
    try:
        
        numero = int(input('Digite um número positivo menor que 1000: '))
        
        if numero >= 1000:
            print('O número precisa ser menor que 1000')
        elif numero < 0:
            print('O número precisa ser positivo')
        else:
            
            cent_int = dez_int = und_int = 0
            cent_str = dez_str = und_str = ''
            resto = 0
           
            
            cent_int, resto = divmod(numero,100)
            if cent_int != 0:
                cent_str = " centena"
                if cent_int > 1:
                    cent_str += "s"
            
            dez_int, resto = divmod(numero - (cent_int * 100),10)
            if dez_int != 0:
                dez_str = " dezena"
                if dez_int > 1:
                    dez_str += "s"
            
            und_int = resto 
            if und_int != 0:
                und_str = " unidade"
                if und_int > 1:
                    und_str += "s"
            
            # 101 ou 100
            if cent_int != 0 and dez_int == 0:
                mensagem = str(cent_int) + cent_str
                if und_int != 0:
                    mensagem += " e " + str(und_int) + und_str
           
            # 110 
            if cent_int != 0 and dez_int != 0 and und_int == 0:
                mensagem = str(cent_int) + cent_str + " e " + str(dez_int) +dez_str
            # 111   
            elif cent_int != 0 and dez_int != 0 and und_int != 0:
                mensagem = str(cent_int) + cent_str + ", " + str(dez_int) + dez_str + ' e ' + str(und_int) + und_str
            
            # 011
            elif cent_int == 0 and dez_int != 0 and und_int != 0:
                mensagem = str(dez_int) + dez_str + ' e ' + str(und_int) + und_str
            # 010
            elif cent_int == 0 and dez_int != 0 and und_int == 0:
                 mensagem = str(dez_int) + dez_str
            
        
            print(f'{numero} = {mensagem}')
            break
    except ValueError:
        print('Entrada inválida')
        
