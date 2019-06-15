class Acceptor(object):
    def __init__(self, id):
        self.id = id
        self.minimumNumber = 0
        self.highestValue = 0
        self.propInfos = {}

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def prepare_response(self, propNumber, propValue, quantTotalProposers):
        if not self.propInfos:
            #manda mensagem numero minimo propNumber
            self.minimumNumber = propNumber
        else:
            if propNumber > self.minimumNumber:
                #manda mensagem pra deus e o mundo
                self.minimumNumber = propNumber
        if propValue > self.highestValue:
            self.highestValue = propValue

        self.propInfos[propNumber] = propValue

    def accepted():
        pass
