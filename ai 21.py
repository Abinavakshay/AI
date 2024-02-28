class MonkeyBananaProblem:
    def __init__(self):
        self.state = {'monkey': 'A', 'box': 'A', 'banana': 'C'}  # Corrected initial box position

    def actions(self, state):
        if state['monkey'] == 'A' and state['box'] == 'A':
            return ['push box from A to B']
        elif state['monkey'] == 'B' and state['box'] == 'B':
            return ['climb box', 'grab banana']
        else:
            return []

    def result(self, state, action):
        if action == 'push box from A to B':
            new_state = {'monkey': 'B', 'box': 'B', 'banana': 'C'}
        elif action == 'climb box':
            new_state = {'monkey': 'B', 'box': 'B', 'banana': 'C'}
        elif action == 'grab banana':
            new_state = {'monkey': 'B', 'box': 'B', 'banana': 'Picked'}
        else:
            raise ValueError("Invalid action")

        return new_state

    def goal_test(self, state):
        return state['banana'] == 'Picked'


def main():
    problem = MonkeyBananaProblem()
    state = problem.state
    print("Initial State:", state)

    while not problem.goal_test(state):
        possible_actions = problem.actions(state)
        print("Possible Actions:", possible_actions)

        action = input("Enter your action: ")
        if action in possible_actions:
            state = problem.result(state, action)
            print("New State:", state)
        else:
            print("Invalid action, please try again.")

    print("Congratulations! You have picked the banana!")


if __name__ == "__main__":
    main()
