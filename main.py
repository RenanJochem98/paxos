from Proposer import Proposer
from Proposal import Proposal
import time #para fazer o sleep

print("######   ALGORITMO INICIADO  ######")
count = 0
prop = Proposer()
prop2 = Proposer()

proposal = Proposal()
proposal.addProposer(prop)
proposal.addProposer(prop2)
# proposal.proposal_number()
# print(prop.getId())
# proc.setId(id)
# proc2.setId(id2)

# proc.addAcceptor(3)
# print(proc.acceptors)
# print(proc.getId())
# proc.setId(1)
# while count < 32 :
#     print(proc.getId())
#     count += 1
#     time.sleep(0.5)
print("######   ALGORITMO FINALIZADO  ######")
