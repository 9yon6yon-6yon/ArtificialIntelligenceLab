import math


def calculate_cost(state):
    count = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if(state[i] > state[j]):
                count += 1
    return count


def State_gen(currentState):
    while (True):
        current_state_cost = calculate_cost(currentState)
        print(currentState, current_state_cost)
        min_next_cost = math.inf
        min_next_state = None

        for i in range(len(currentState)):
            for j in range(i+1, len(currentState)):
                newState = currentState.copy()
                newState[i], newState[j] = newState[j], newState[i]
                next_state = newState
                next_state_cost = calculate_cost(next_state)
                if (next_state_cost < min_next_cost):
                    min_next_cost = next_state_cost
                    min_next_state = next_state

        if (min_next_cost < current_state_cost):
            currentState = min_next_state
        else:
            print("Final State : ", currentState, current_state_cost)
            break


state = [7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
State_gen(state)
