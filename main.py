from Server import Server
from Proposer import Proposer
from Acceptor import Acceptor
from Learner import Learner
import time #para fazer o sleep

print("######   ALGORITMO INICIADO  ######")
# count = 0
server = Server()

prop = Proposer(1,10)
prop2 = Proposer(2,20)
prop3 = Proposer(3, 30)

server.addProposer(prop2)
server.addProposer(prop3)
server.addProposer(prop)

server.showAllProposers()

acceptor = Acceptor(1)
acceptor2 = Acceptor(2)
acceptor3 = Acceptor(3)

server.addAcceptor(acceptor)
server.addAcceptor(acceptor2)
server.addAcceptor(acceptor3)

server.showAllAcceptors()

learner = Learner(1)
server.addLearner(learner)

server.start()
# proposal = Proposal()
# proposal.addProposer(prop)
# proposal.addProposer(prop2)

# print(server.proposers)
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
