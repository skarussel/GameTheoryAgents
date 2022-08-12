import numpy as np
from game_simulation import simulate_match_up
from agent import *
from game import get_default_game, Game


class MyAgent(Agent):
    """ Define your own Agent """
    def __init__(self, player_id, game):
        super(MyAgent, self).__init__(player_id, game)

    def get_action(self, last_action_p1, last_action_p2) -> Action:
        raise NotImplementedError("Agent behaviour not yet implemented!")

    def __repr__(self):
        return "MyAgent"


if __name__ == "__main__":
    GAMES_PER_MATCHUP = 100
    game = get_default_game()  # or define your own using Game()  (see game.py for details)
    print(game, "\n")

    # evaluate a specific match-up, e.g. AllDefectAgent vs. CopycatAgent  (index 1 vs index 2)
    agents=[AllDefectAgent, CopycatAgent]
    print(f"{agents[0](1,game)} vs. {agents[1](1,game)} -> {simulate_match_up(agents[0], agents[1], game,    GAMES_PER_MATCHUP)}\n") 
    # play out all combinations of agents
    agents = [AllCooperateAgent, AllDefectAgent, CopycatAgent, RandomAgent, GrudgerAgent, DetectiveAgent]
    results = np.zeros((2, len(agents), len(agents)))
    for id1, player1 in enumerate(agents):
        for id2, player2 in enumerate(agents):
            results[:, id1, id2] = simulate_match_up(player1, player2, game, GAMES_PER_MATCHUP)
    print(results, "\n")
    # results[:, agent1, agent2] contains the results of simulate_match_up(agent1, agent2, game)

    for id, agent in enumerate(agents):
        print(f"total points of agent: {agent(1,game)} = {sum(results[0,id,:]) + sum(results[1,:,id])}")
