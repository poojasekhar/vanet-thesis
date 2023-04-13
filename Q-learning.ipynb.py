import numpy as np
import random
import math


def signum(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def calculateCBR(density, txpower):
    if txpower == 2:
        if density <= 37:
            cbr = (0.0115 * density) + 0.505
        else:
            cbr = 0.1934 * math.log(density) + 0.2378
    elif txpower == 4:
        if density <= 40:
            cbr = (0.0093 * density) + 0.5973
        else:
            cbr = 0.1681 * math.log(density) + 0.3509
    elif txpower == 6:
        if density <= 42:
            cbr = (0.0081 * density) + 0.6468
        else:
            cbr = 0.1537 * math.log(density) + 0.4126
    elif txpower == 8:
        if density <= 42:
            cbr = (0.0079 * density) + 0.6528
        else:
            cbr = 0.1519 * math.log(density) + 0.4202
    elif txpower == 10:
        if density <= 42:
            cbr = (0.0079 * density) + 0.6533
        else:
            cbr = 0.1518 * math.log(density) + 0.4207
    elif txpower == 12:
        if density <= 42:
            cbr = (0.0079 * density) + 0.6532
        else:
            cbr = 0.1519 * math.log(density) + 0.4203
    elif txpower == 14:
        if density <= 42:
            cbr = (0.0079 * density) + 0.6544
        else:
            cbr = 0.1516 * math.log(density) + 0.4217
    elif txpower == 16:
        if density <= 42:
            cbr = (0.0079 * density) + 0.6532
        else:
            cbr = 0.1518 * math.log(density) + 0.4206
    elif txpower == 18:
        if density <= 42:
            cbr = (0.0079 * density) + 0.6532
        else:
            cbr = 0.1518 * math.log(density) + 0.4205
    elif txpower == 20:
        if density <= 42:
            cbr = (0.0079 * density) + 0.654
        else:
            cbr = 0.1516 * math.log(density) + 0.4215
    else:
        cbr = -1

    if cbr > 0.92:
        cbr = 0.92
    return cbr


# Parameters
gamma = 0.99
alpha = 0.01
num_episode = 50000

epsilon = 0.9  # the percentage of time when we should take the best action (instead of a random action)
discount_factor = 0.9  # discount factor for future rewards
learning_rate = 0.9  # the rate at which the AI agent should learn

def QLearning(rewards, gamma=0.99, alpha=0.01, num_episode=50000):
    """
    Run Q-learning loop for num_episode iterations or till difference between Q is below min_difference.
    """
    Q = [[0 for i in range(0, len(rewards[0]))] for j in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]]
    # all_states = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    all_states = np.arange(len(rewards))
    # print(all_states)
    j = -1
    for i in range(num_episode):
        # initialize state
        initial_state = np.random.choice(all_states)
        if random.random() < epsilon:
            action = Q[initial_state].index(max(Q[initial_state]))
        else:
            action = random.randint(0, 9)
        Q[initial_state][action] = Q[initial_state][action] + alpha * (rewards[initial_state][action] + gamma * np.max(Q[nextStates[initial_state][action]]) - Q[initial_state][action])
        cur_state = nextStates[initial_state][action]
        # loop for each step of episode, until reaching goal state
        # while cur_state != goal_state:
        for k in range(0, 10):  # for each state, we take 10 actions because we have no goal state
            action = k-1 #random.randint(0, 9)  # this line was used for the new table
            Q[cur_state][action] = Q[cur_state][action] + alpha * (rewards[cur_state][action] + gamma * np.max(Q[nextStates[cur_state][action]]) - Q[cur_state][action])
            cur_state = nextStates[cur_state][action]

    return np.around(Q / np.max(Q) * 100)


threshold = 0.60
file = open("qtabletxpower.txt", "w")
for density in range(0, 52):
    cbrVals = []
    rewards = []
    rateRewards = []
    txpower = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    for i in txpower:
        cbrVals.append([calculateCBR(density, i) for k in range(1,11)])
        for j in txpower:
                #rateRewards.append((j)*cbrVals[i][j]*signum(0.6-cbrVals[i][j]))
                rateRewards.append((cbrVals[txpower.index(i)][txpower.index(j)]*j) * signum(0.60 - cbrVals[txpower.index(i)][txpower.index(j)]))
        rewards.append(rateRewards)
        rateRewards = []

    nextStates = [[i for i in range(0, 10)] for j in range(0, 10)]
    print(rewards)

    Q = QLearning(rewards, gamma=gamma, alpha=alpha, num_episode=num_episode)


    for j in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]:
        file.write(str(density) + '\t' + str(round(calculateCBR(density, j), 4)) + '\t')
        for i in range(0, len(Q[[2, 4, 6, 8, 10, 12, 14, 16, 18, 20].index(j)])):
            if i < 9:
                file.write(str(Q[[2, 4, 6, 8, 10, 12, 14, 16, 18, 20].index(j)][i]) + '\t')
            else:
                file.write(str(Q[[2, 4, 6, 8, 10, 12, 14, 16, 18, 20].index(j)][i]) + '\n')
        file.flush()

    print(density)
file.close()