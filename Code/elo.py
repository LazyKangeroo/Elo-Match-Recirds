from const import *

class Elo:
    def __init__(self):
        pass

    def getNewElo(self,result,playerA,playerB):
        # gets player experience
        K = self.experience(playerA)
        E = self.expectedResult(playerA,playerB)

        return playerA["elo"] + K * (result - E)

    def expectedResult(self,playerA,playerB):
        Q_A = 10 ** (playerA["elo"] / 400)
        Q_B = 10 ** (playerB["elo"] / 400)
        return Q_A / (Q_A + Q_B)

    def experience(self,player):
        if player["games"]["amnt"] <= MIN_GAMES:
            return K1
        elif player["elo"] >= K2_ELO and player["elo"] <= K3_ELO:
            return K2
        elif player["elo"] <= K3_ELO:
            return K3
