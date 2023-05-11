import random
import time
import threading

from sapo import Sapo
from exibicao_corrida import ExibicaoCorrida


class ComendoMoscas:
    def __init__(self, id):
        self.id = id

    def comer(self):
        print(f"Sapo {self.id} está comendo moscas...")
        time.sleep(random.uniform(1, 5))


def corrida_sapos():
    num_sapos = 5

    # Criando lista de objetos Sapo
    lista_sapos = [Sapo(i) for i in range(1, num_sapos + 1)]

    # Iniciando threads para cada sapo
    threads_sapos = []
    for sapo in lista_sapos:
        t = threading.Thread(target=sapo.pular)
        t.start()
        threads_sapos.append(t)

    # Iniciando thread para exibição da corrida
    exibicao = ExibicaoCorrida(lista_sapos)
    t_exibicao = threading.Thread(target=exibicao.exibir)
    t_exibicao.start()

    # Iniciando threads para os sapos comerem moscas
    threads_moscas = []
    for sapo in lista_sapos:
        comendo = ComendoMoscas(sapo.id)
        t = threading.Thread(target=comendo.comer)
        t.start()
        threads_moscas.append(t)

    # Aguardando todas as threads terminarem
    for t in threads_sapos:
        t.join()

    for t in threads_moscas:
        t.join()

corrida_sapos()