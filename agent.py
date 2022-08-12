from actions import Action
from random import random


class Agent:
    def __init__(self, player_id, game):
        self.player_id = player_id
        self.game = game
        pass

    def get_action(self, last_action_p1, last_action_p2) -> Action:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__

    def __repr__(self):
        return str(self)


class AllCooperateAgent(Agent):
    """ Agent that always cooperates """
    def get_action(self, last_action_p1, last_action_p2) -> Action:
        return Action.Cooperate

class AllDefectAgent(Agent):
    """ Agent that always defects """
    def get_action(self, last_action_p1, last_action_p2) -> Action:
        return Action.Defect

class RandomAgent(Agent):
    """ Agent that randomly chooses to play Cooperate or Defect """
    def get_action(self, last_action_p1, last_action_p2) -> Action:
        return Action.Cooperate if random() > 0.5 else Action.Defect

class GrudgerAgent(Agent):
    """ Agent that starts to always play cooperate until its opponent defects once after which it only defects """
    def __init__(self, player_id, game):
        super(GrudgerAgent, self).__init__(player_id, game)
        self.was_defected = False

    def get_action(self, last_action_p1, last_action_p2) -> Action:
        if self.was_defected:
            return Action.Defect
        else:
            if (self.player_id == 1 and last_action_p2 is Action.Defect) or \
                    (self.player_id == 2 and last_action_p1 is Action.Defect):
                self.was_defected = True
                return Action.Defect
            else:
                return Action.Cooperate

class CopycatAgent(Agent):
    """ Agent that always starts with Cooperate and then repeats the action of its opponent. """
    def get_action(self, last_action_p1, last_action_p2) -> Action:
        if self.player_id == 1:
            return last_action_p2 if last_action_p2 is not None else Action.Cooperate
        else:
            return last_action_p1 if last_action_p1 is not None else Action.Cooperate

class DetectiveAgent(Agent):
    """ Agent that starts with Cooperate, Defect, Cooperate, Cooperate. After the first rounds if you ever Defect
    it plays like a CopycatAgent otherwise it plays like AllDefectAgent. """
    def __init__(self, player_id, game):
        super(DetectiveAgent, self).__init__(player_id, game)
        self.round = 0
        self.pattern = [Action.Cooperate, Action.Defect, Action.Cooperate, Action.Defect]
        self.was_defected = False

    def get_action(self, last_action_p1, last_action_p2) -> Action:
        # check if the agent ever got defected
        if (self.player_id == 1 and last_action_p2 is Action.Defect) or \
                (self.player_id == 2 and last_action_p1 is Action.Defect):
            self.was_defected = True

        # use the defined pattern during the first rounds
        self.round += 1
        if self.round < len(self.pattern):
            return self.pattern[self.round-1]

        if self.was_defected: # if defected play like copycat
            if self.player_id == 1:
                return last_action_p2 if last_action_p2 is not None else Action.Cooperate
            else:
                return last_action_p1 if last_action_p1 is not None else Action.Cooperate
        else: # if not defected then always defect
            return Action.Defect

if __name__ == "__main__":
    from game import get_default_game
    test_game = get_default_game()

    test_agent = RandomAgent(1, test_game)
    action_p1 = None
    previous_action_p2 = [None, Action.Cooperate, Action.Defect, Action.Cooperate, Action.Defect]

    print("{:15}  {:8}  {:18}".format("agent response", "round", "previous action p2"))

    for round, action_p2 in enumerate(previous_action_p2):
        action_p1 = test_agent.get_action(action_p1, action_p2)
        print("{:15}  {:3}       {:18}".format(action_p1.value, round, "None" if action_p2 is None else action_p2.value))
