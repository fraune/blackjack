from app.simulator.policy import State, Action

q_table = {}

for state in State:
    q_table[state] = {}
    for action in Action:
        q_table[state][action] = 0.0
