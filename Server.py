from random import randint
from datetime import datetime
from datetime import timedelta
import time

class Server(object):

    def __init__(self):
        self.name = "Server"
        self.proposers = []
        self.acceptors = []
        self.learners = []
        self.quantProposers = 0;
        self.quantAcceptors = 0
        self.quantLearners = 0
        self.ids_usados = []
        self.temp_store = {} # guarda temporariamente proposers para nao executar tudo sequencial
        self.ignorados = []
        self.numberIgnorados = 0

    #apenas para testes
    def getName(self):
        return self.name
    def showAllProposers(self):
        print("     ----- Todos os PROPOSERS Adicionados -----")
        for p in self.proposers:
            print(p.propToString())
        print("")

    def showAllAcceptors(self):
        print("     ----- Todos os ACCEPTORS Adicionados -----")
        for a in self.acceptors:
            print(a.acceptToString())
        print("")

    # para organizacao
    def getQuantProposers(self):
        return self.quantProposers

    def getQuantAcceptors(self):
        return self.quantAcceptors

    def getQuantLearners(self):
        return self.quantLearners

    def addProposer(self, proposer):
        proposer.server = self
        proposer.setNumber(self.getUniqueId())
        self.proposers.append(proposer)
        self.quantProposers += 1

    def addAcceptor(self, acceptor):
        acceptor.server = self
        self.acceptors.append(acceptor)
        self.quantAcceptors += 1

    def addLearner(self, learner):
        learner.server = self
        self.learners.append(learner)
        self.quantLearners += 1

    def getUniqueProposer(self, propNumber):
        for p in self.proposers:
            if propNumber == p.getNumber():
                return p
        return None

    def start(self):
        for p in self.proposers:
            p.prepare_request()

    # para execucao
    def getUniqueId(self):
        id = -1
        tem_id = False
        while not tem_id:
            id = randint(1,1000)
            if id not in self.ids_usados:
                self.ids_usados.append(id)
                tem_id = True
        return id

    def send_prepare_request(self, propNumber, propValue):
        for a in self.acceptors:
            # print("Enviando valor de Proposer "+str(propNumber)+ ", com valor "]
            # +str(propValue)+" para Acceptor "+str(a.getId()))
            a.prepare_response(propNumber, propValue, self.quantProposers)

    def prop_accept_request(self, propNumber, propValue):
        if propValue is None and propNumber not in self.ignorados:
            self.ignorados.append(propNumber)
            self.numberIgnorados += 1
        elif propValue is not None:
            self.temp_store[propNumber] = propValue
        # print("Recebeu: N: "+str(propNumber)+" V: "+str(propValue))
        if len(self.temp_store)+self.numberIgnorados == self.quantAcceptors:
            # print("Passou")
            for propNumberKey in self.temp_store:
                prop = self.getUniqueProposer(propNumberKey)
                prop.accept_request(propNumberKey, self.temp_store[propNumberKey])
            self.temp_store.clear()
            self.numberIgnorados = 0

    def send_final_response(self, greaterPropNumber, greaterPropValue):
        for a in self.acceptors:
            a.accepted(greaterPropNumber, greaterPropValue)

    def send_value_to_learners(self, value, acceptorId, propNumber):
        for l in self.learners:
            l.getPaxos(value, acceptorId, propNumber)
