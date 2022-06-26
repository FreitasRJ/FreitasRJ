'''
18 - Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo
usando este link (em minutos).
Arredonde o tempo em minutos

'''
import math

tam_MB = int(input('Informe o tamanho do arquivo MB: '))
velo_Mbps = int(input('Informe a velocidade em Mbps: '))

tempo_down_minutos = math.ceil((tam_MB /(velo_Mbps/8))/60)

print(tempo_down_minutos)
