from random import randint
class Proposer(object):
    def __init__(self):
        self.id = 0
        self.acceptors = []
        self.value = randint(1,1000)
        self.quantTotalProposers = 0

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getQuantTotalProposers(self):
        return self.quantTotalProposers

    def setQuantTotalProposers(self, newQuantProposers):
        self.quantTotalProposers = newQuantProposers

    def addAcceptor(self, acceptor_id):
        self.acceptors.append(acceptor_id)

    def removeAcceptor(self, acceptor_id):
        pass

    def prepare_request(self):
        for a in self.acceptors
            a.prepare_reponse(self.getId, self.value, self.quantTotalProposers)
    def accept_request():
        pass
