class GumballMachine:
    SOLD_OUT: int = 0
    NO_QUARTER: int = 1
    HAS_QUARTER: int = 2
    SOLD: int = 3

    def __init__(self):
        self.state = self.SOLD_OUT
        self.count = 0

    def insert_quarter(self) -> None:
        if self.state == self.HAS_QUARTER:
            raise ValueError("Cannot insert another quarter.")

        elif self.state == self.SOLD_OUT:
            print('Cannot insert a quarter because the machine is sold out')

        elif self.state == self.SOLD:
            print('Return a gumball')

        elif self.state == self.NO_QUARTER:
            self.state = self.HAS_QUARTER
            print('A quarter has been inserted')

    def eject_quarter(self) -> None:
        if self.state == self.HAS_QUARTER:
            self.state = self.NO_QUARTER
            print('The customer recovered the quarter')

        elif self.state == self.NO_QUARTER:
            raise ValueError("No quarter has been inserted.")

        elif self.state == self.SOLD:
            raise ValueError("Not possible, the crank has been turned.")

        elif self.state == self.SOLD_OUT:
            raise ValueError("No quarter has been inserted.")

    def turns_crank(self) -> None:
        if self.state == self.SOLD:
            raise ValueError("Stop trying to trick the machine!")

        elif self.state == self.NO_QUARTER:
            raise ValueError("No quarter has been inserted.")

        elif self.state == self.HAS_QUARTER:
            print("You get a gumball!")
            self.state = self.SOLD
            self.dispense()

    def dispense(self) -> None:
        initial_state = self.state

        if initial_state == self.SOLD:
            print("Gumball comes rolling out!")
            self.count -= 1

            if not self.count:
                print("OUT OF GUMBALLS!")
                self.state = self.SOLD_OUT
            else:
                self.state = self.NO_QUARTER

        elif initial_state == self.NO_QUARTER:
            raise ValueError("No quarter has been inserted.")

        elif initial_state == self.SOLD_OUT:
            raise ValueError("SOLD OUT!")

        elif initial_state == self.HAS_QUARTER:
            raise ValueError("No gumball has been dispensed.")

    def stock_gumballs(self, num_gumballs: int) -> None:
        self.state = self.NO_QUARTER
        self.count = num_gumballs


if __name__ == '__main__':
    gbm = GumballMachine()
    gbm.stock_gumballs(num_gumballs=50)
    print(gbm.state)
    print(gbm.count)
    print(gbm.insert_quarter())
    print(gbm.turns_crank())

    print("Empty GBM")
    empty_gbm = GumballMachine()
    print(empty_gbm.state)
    print(empty_gbm.count)
    print(empty_gbm.dispense())
