from random import randint

class Proposal(object):
    def __init__(self):
        self.id = 0
        self.proposers = []

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def addProposer(self, proposer):
        proposer.setQuantTotalProposers(len(self.proposers) +1)
        self.proposers.append(proposer)

    def getQuantProposers(self):
        return len(self.proposers)

    def proposal_number(self):
        ids_usados = []

        number_proposers = len(self.proposers);
        for p in self.proposers:
            tem_id = False
            while not tem_id:
                random_int = randint(1,1000)
                if random_int not in ids_usados:
                    p.setId(random_int)
                    ids_usados.append(random_int)
                    tem_id = True
