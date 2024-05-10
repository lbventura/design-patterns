# The State pattern allows an object to alter its behavior when its internal class changes.
# The object will appear to have changed its class.
# The class diagram of the State pattern is the same as that of Strategy, but the two patterns differ on their intent.
# With state, the client knows very little (if anything) about the state objects.
# With strategy, the client usually specifies the strategy object that the context is composed with.

# Strategy is a flexible alternative to subclassing. One can change the behavior of an object through composition.
# State is an alternative for long conditionals. One encapsulates the behaviors within state objects
# and then changes state objects to obtain different behaviors.

from random import random


class State:
    def insert_quarter(self):
        raise ValueError("Please check if a quarter has been inserted or if a gumball has been released")

    def eject_quarter(self):
        raise ValueError("Please check if a quarter has been inserted or if a gumball has been released")

    def turn_crank(self):
        raise ValueError("No quarter has been inserted")

    def dispense(self):
        raise ValueError("No quarter has been inserted")

    def refill(self, number_gumballs: int):
        raise ValueError("No gumballs has been inserted")


class GumballMachine:
    # The implementation of each of the state's behaviors is left to the
    # concrete implementation of State (for example, NoQuarterState).
    # Thereby encapsulating what varies.
    def __init__(self, number_gumballs: int):
        self.no_quarter_state: State = NoQuarterState(gumball_machine=self)
        self.sold_out_state: State = SoldOutState(gumball_machine=self)
        self.has_quarter_state: State = HasQuarterState(gumball_machine=self)
        self.sold_state: State = SoldState(gumball_machine=self)
        self.winner_state: State = WinnerState(gumball_machine=self)
        self.count = number_gumballs
        self.state: State = State()

        if self.count > 0:
            self.state = self.no_quarter_state

    def set_state(self, state: State) -> None:
        self.state = state

    def set_number_gumballs(self, number_gumballs: int) -> None:
        self.count = number_gumballs

    def insert_quarter(self) -> None:
        self.state.insert_quarter()

    def eject_quarter(self) -> None:
        self.state.eject_quarter()

    def turn_crank(self) -> None:
        print(self.state)
        self.state.turn_crank()
        print(self.state)
        self.state.dispense()

    def release_ball(self):
        print("A gumball comes rolling out!")
        if self.count > 0:
            self.count -= 1

    def refill(self, number_gumballs: int):
        self.state.refill(number_gumballs=number_gumballs)


class SoldState(State):

    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def dispense(self):
        self.gumball_machine.release_ball()

        if self.gumball_machine.count > 0:
            self.gumball_machine.set_state(state=self.gumball_machine.no_quarter_state)
        else:
            print("No more gumballs, needs to be restocked!")
            self.gumball_machine.set_state(state=self.gumball_machine.sold_out_state)


class SoldOutState(State):

    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def refill(self, number_gumballs: int):
        self.gumball_machine.set_number_gumballs(number_gumballs=number_gumballs)
        print("The gumball machine has been refilled!")
        self.gumball_machine.set_state(state=self.gumball_machine.no_quarter_state)


class NoQuarterState(State):

    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self) -> None:
        print("A quarter has been inserted")
        self.gumball_machine.set_state(state=self.gumball_machine.has_quarter_state)


class HasQuarterState(State):

    def __init__(self, gumball_machine: GumballMachine):
        self.gumball_machine = gumball_machine

    def eject_quarter(self) -> None:
        print("A quarter has been ejected")
        self.gumball_machine.set_state(state=self.gumball_machine.no_quarter_state)

    def turn_crank(self):
        print("The crank has been turned")

        is_winner = random() < 0.1
        if is_winner and self.gumball_machine.count > 1:
            self.gumball_machine.set_state(state=self.gumball_machine.winner_state)
        else:
            self.gumball_machine.set_state(state=self.gumball_machine.sold_state)


class WinnerState(SoldState):
    def dispense(self):
        print('You are a goddamn winner!')
        self.gumball_machine.release_ball()

        if self.gumball_machine.count == 0:
            self.gumball_machine.set_state(state=self.gumball_machine.sold_out_state)
        else:
            self.gumball_machine.release_ball()
            if self.gumball_machine.count > 0:
                self.gumball_machine.set_state(state=self.gumball_machine.no_quarter_state)
            else:
                print("No more gumballs, needs to be restocked!")
                self.gumball_machine.set_state(state=self.gumball_machine.sold_out_state)


if __name__ == '__main__':
    num_gumballs = 10
    gbm = GumballMachine(number_gumballs=num_gumballs)
    print(gbm.state)

    for i in range(num_gumballs*2):
        print(f'Gumball No {i + 1}')

        try:
            gbm.insert_quarter()
            gbm.turn_crank()
        except ValueError:
            gbm.refill(number_gumballs=10)
