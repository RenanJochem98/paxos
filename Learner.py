class Learner(object):
    def __init__(self, id):
        self.id = id
        self.highestValue = 0
        self.server = None

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getPaxos(self, value, acceptorId, propNumber):
        print("****************************************************")
        print("Valor aceito em Paxos: "+str(value)+", enviado pelo Acceptor: "+str(acceptorId)
        +" e gerado pelo Proposer: "+str(propNumber)+ ", no Learner "+str(self.id))
        print("")

    def learnToString(self):
        return "Learner Id: " + str(self.id) + ", Learner Server Name: "+ str(self.server.getName())
