class Duck(object):

    def __str__(self):
        return "Duck"

    @classmethod
    def quack(cls) -> str:
        return "quack"

    @classmethod
    def fly(cls) -> str:
        return "fly"


class Turkey(object):

    def __str__(self):
        return "Turkey"

    @classmethod
    def gobble(cls) -> str:
        return "gobble, gobble"

    @classmethod
    def fly(cls) -> str:
        return "a short flight"


class TurkeyAdapter(Duck):
    # Duck inheritance here is just so the correct type is returned
    # see instantiation below

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self) -> str:
        return self.turkey.gobble()

    def fly(self) -> str:
        flights = [self.turkey.fly()] * 5
        return '\n'.join(flights)


class DuckAdapter(Turkey):

    def __init__(self, duck: Duck):
        self.duck = duck

    def gobble(self) -> str:
        return self.duck.quack()

    def fly(self) -> str:
        return self.duck.fly() + ' shorter'


class ThanksgivingPardon:
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def pardon(self) -> str:
        return f"I, the President of the United States of America, declare this {str(self.turkey)} pardoned."


class TurkeyAdapterMultiple(Duck, Turkey):

    def quack(self) -> str:
        return self.gobble()

    def fly(self) -> str:
        flight = super(Duck, self).fly()  # wrong super call but yields the correct result
        return flight


if __name__ == '__main__':
    ta = TurkeyAdapter(turkey=Turkey())
    print(ta.quack())
    print(ta.fly())
    print(ta.__class__.__bases__[0])

    da = DuckAdapter(duck=Duck())
    print(da.gobble())
    print(da.fly())

    # this should work by default
    tp = ThanksgivingPardon(turkey=Turkey())
    print(tp.pardon())

    # through the interface, this also works!
    fake_tp = ThanksgivingPardon(turkey=DuckAdapter(duck=Duck()))
    print(fake_tp.pardon())

    tam = TurkeyAdapterMultiple()
    print(tam.quack())
    print(tam.fly())
