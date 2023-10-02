"""
constantes = "Variáveis" que não vão mudar
muitas condições no mesmo if é ruim
    = contagem de complexidade é ruim

"""

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGER = 1 # a distancia onde o radar pega 

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGER) and \
    local_carro <= (LOCAL_1 + RADAR_RANGER)


if vel_carro_pass_radar_1:
    print("Velocidade do carro passou do radar 1")

if carro_passou_radar_1:
    print("Carro passou radar 1")
if carro_passou_radar_1 and vel_carro_pass_radar_1:
    print("Carro multado em radar 1")
