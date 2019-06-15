class Proposer(object):
    def __init__(self):
        self.id = 0
        self.acceptors = []

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def addAcceptor(self, acceptor_id):
        self.acceptors.append(acceptor_id)

    def removeAcceptor(self, acceptor_id):
        pass

    def proposal_number():
        pass

    def prepare_request():
        pass

    def accept_request():
        pass
