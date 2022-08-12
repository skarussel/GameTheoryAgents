def simulate_match_up(agent1, agent2, game, number_of_games):
    agent1 = agent1(1, game)
    agent2 = agent2(2, game)
    action1 = None
    action2 = None
    result_player_1 = 0
    result_player_2 = 0

    for i in range(number_of_games):
        new_action1 = agent1.get_action(action1, action2)
        new_action2 = agent2.get_action(action1, action2)
        payoff_p1, payoff_p2 = game.get_agent_payoffs(new_action1, new_action2)
        result_player_1 += payoff_p1
        result_player_2 += payoff_p2
        action1 = new_action1
        action2 = new_action2
    return result_player_1, result_player_2
