from app.simulator.evaluator import evaluate_policy_table
from app.simulator.q_learning import optimize_policy, construct_policy
from app.utility.logging import i
from app.utility.policy_rw import save_policy, load_policy

EVALUATE = True
LEARN = False

"""
Policy table evaluation
"""
if EVALUATE:
    i('Evaluating a policy')
    policy = load_policy('policy_1648428252.json')
    evaluate_policy_table(policy)

"""
Initiate q-learning and save the policy
"""
if LEARN:
    i('Learning a policy')
    q_table = optimize_policy()
    policy = construct_policy(q_table)
    save_policy(policy)
