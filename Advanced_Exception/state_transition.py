from transition_error import TransitionError

class StateMachine:
    allowed_transitions = {
        "new" : ["loading"],
        "loading": ["completed", "incomplete"],
        "incomplete": [],
        "completed": ["cancelled"]
        }
    
    def __init__(self, state="new"):
        self.state = state
        
    def transition(self, new_state):
        if new_state.lower() in self.allowed_transitions:
            self.state = new_state.lower()
        else:
            raise TransitionError(self.state, new_state, f"unable to transition from {self.state} to {new_state}. Can only transition to {self.allowed_transitions[self.state]}")
        
if __name__ == "__main__":
    sm = StateMachine()
    try:
        sm.transition("loading")
        sm.transition("canceled")
    except TransitionError as err:
        print(f"Previous State {err.previous}")
        print(f"Desired State {err.next_state}")
        print(err.message)