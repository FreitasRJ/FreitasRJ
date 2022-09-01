# Estudo baseado em: https://www.youtube.com/watch?v=CtSX3dWqWBQ&list=PLAgbpJQADBGLo24x_xBwGtTDO-bjwrFb_&index=2

class ControleRemoto:

    def __init__(self, televisao, comodo) -> None:
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print('Canal avançado.')

    def volta_canal(self):
        print('Voltar canal.')

    def escolher_canal(self, canal):
        print(f'Alterado para o canal {canal} ')


controle_sala = ControleRemoto('Samsung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()
controle_sala.escolher_canal(12)

controle_quarto = ControleRemoto("LG", "quarto")
print(controle_quarto.televisao)
print(controle_quarto.comodo)