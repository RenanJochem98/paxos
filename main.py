from Proposer import Proposer
import time #para fazer o sleep

print("######   ALGORITMO INICIADO  ######")

count = 0
proc = Proposer(2)
proc.addAcceptor(3)
print(proc.acceptors)
# print(proc.getId())
# proc.setId(1)
# while count < 30 :
#     print(proc.getId())
#     count += 1
#     time.sleep(0.5)
# print("######   ALGORITMO FINALIZADO  ######")
