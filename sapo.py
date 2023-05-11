import random
import time

class Sapo:
    def __init__(self, id):
        self.id = id
        self.posicao = 0
        self.velocidade = 0
        self.vivo = True

    def pular(self):
        tempo_decorrido = 0
        while True:
            if self.vivo:
                # Gerando valores aleatórios de velocidade e distância
                self.velocidade = random.uniform(1, 5)
                self.posicao += self.velocidade
                tempo_decorrido += 0.5

                # Verificando se o sapo atingiu a distância máxima de 1000 metros
                if self.posicao >= 1000:
                    print(f"Sapo {self.id} terminou a corrida em {tempo_decorrido:.2f} segundos!")
                    break

                print(f"Sapo {self.id} correu {self.velocidade:.2f} unidades e está na posição {self.posicao:.2f} (tempo: {tempo_decorrido:.2f}s)")
                time.sleep(random.uniform(3, 5))  # Esperando tempo aleatório para pular

                if random.randint(0, 3) == 0:
                    pulo_distancia = random.uniform(10, 15)
                    print(f"Sapo {self.id} pulou! {pulo_distancia :.2f} Metros" )
                    time.sleep(random.uniform(2, 3))
                    self.posicao += pulo_distancia

                self.atacado_por_predador()

            else:
                break

    def atacado_por_predador(self):
        if random.random() < 0.1:
            print(f"Sapo {self.id} foi atacado por um predador! e desviou")

            if random.random() < 0.1:
                print(f"Infelizmente, sapo {self.id} foi morto pelo predador!")
                self.vivo = False
            else:
                print(f"Sapo {self.id} conseguiu escapar do predador!")
                self.vivo = True

    # def __str__(self):
    #     status = "vivo" if self.vivo else "morto"
    #     return f"Sapo {self.id} está na posição {self.posicao:.2f} ({status})" arquivo main.py    import threading