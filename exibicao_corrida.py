import time

class ExibicaoCorrida:
    def __init__(self, lista_sapos):
        self.lista_sapos = lista_sapos

    def exibir(self):
        while True:
            # for sapo in self.lista_sapos:
            #     print(f"{sapo.id} (distância percorrida: {sapo.posicao:.2f}m)")
              # Esperando 3 segundos

            # Verificando se todos os sapos terminaram a corrida
            if all(sapo.posicao >= 100 for sapo in self.lista_sapos):
                break
            time.sleep(60) 