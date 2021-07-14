from BindingObject import BindingObject


class State:
    def __init__(self, state_name, state_condition):
        self.state_condition = state_condition
        self.state_name = state_name

    def print(self):
        if self.state_condition.get():
            print("The condition is passed")

if __name__ == "__main__":
    reference_condition_1 = BindingObject(False)
    reference_condition_2 = BindingObject(False)

    state_1 = State("STATE_1", reference_condition_1)
    state_2 = State("STATE_2", reference_condition_2)

    state_1.print()

    # When somewhere else or sometimes the reference condition activate
    reference_condition_1.set(True)

    # The state_condition that binding to that reference condition will automatically activate
    # And we don't have to fetch the global data for this state or perform any assignment
    state_1.print()



