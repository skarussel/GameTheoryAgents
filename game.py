import numpy as np
import pandas as pd

from actions import Action


class Game:
    def __init__(self, payoff_matrix_p1, payoff_matrix_p2=None):
        self.payoff_matrix_p1 = payoff_matrix_p1
        if payoff_matrix_p2 is not None:
            self.payoff_matrix_p2 = payoff_matrix_p2
        else:
            self.payoff_matrix_p2 = payoff_matrix_p1

    def get_payoff_matrix(self, player_id: int):
        if player_id == 1:
            return self.payoff_matrix_p1
        else:
            return self.payoff_matrix_p2

    def get_agent_payoffs(self, action1: Action, action2: Action):
        payoff1 = self.payoff_matrix_p1[action2.value][action1.value]
        payoff2 = self.payoff_matrix_p2[action2.value][action1.value]
        return payoff1, payoff2

    def __repr__(self):
        return "Game Payoff matrixes:\n" + \
               "player 1 payoff: \n" + str(self.payoff_matrix_p1) + "\n\nplayer 2 payoff: \n" + str(self.payoff_matrix_p2)


def get_default_game() -> Game:
    payoff_matrix_p1 = pd.DataFrame(np.array([[2, -1], [3, 0]]), columns=["Cooperate", "Defect"],
                                    index=["Cooperate", "Defect"])
    payoff_matrix_p2 = pd.DataFrame(np.array([[2, 3], [-1, 0]]), columns=["Cooperate", "Defect"],
                                    index=["Cooperate", "Defect"])
    return Game(payoff_matrix_p1, payoff_matrix_p2)

def get_snowdrift_game() -> Game:
    payoff_matrix_p1 = pd.DataFrame(np.array([[2, 0], [3, -1]]), columns=["Cooperate", "Defect"],
                                    index=["Cooperate", "Defect"])
    payoff_matrix_p2 = pd.DataFrame(np.array([[2, 3], [0, -1]]), columns=["Cooperate", "Defect"],
                                    index=["Cooperate", "Defect"])
    return Game(payoff_matrix_p1, payoff_matrix_p2)
    

if __name__ == "__main__":
    print("game in which both players should choose the same option")
    payoff_matrix = pd.DataFrame(np.array([[1, 0], [0, 1]]), columns=["Cooperate", "Defect"], index=["Cooperate", "Defect"])
    g = Game(payoff_matrix)
    print(g, "\n")

    print("game in which both players should choose different actions")
    payoff_matrix = pd.DataFrame(np.array([[0, 1], [1, 0]]), columns=["Cooperate", "Defect"],
                                 index=["Cooperate", "Defect"])
    g = Game(payoff_matrix)
    print(g, "\n")

    print("default game")
    g2 = get_default_game()
    print(g2, "\n")

    print("access payoff matrix")
    print("Cooperate, Cooperate", g2.get_agent_payoffs(Action.Cooperate, Action.Cooperate))
    print("Cooperate, Defect", g2.get_agent_payoffs(Action.Cooperate, Action.Defect))
    print("Defect, Cooperate", g2.get_agent_payoffs(Action.Defect, Action.Cooperate))
    print("Defect, Defect", g2.get_agent_payoffs(Action.Defect, Action.Defect))
