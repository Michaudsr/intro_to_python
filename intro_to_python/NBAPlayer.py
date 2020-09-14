class NBAPlayer():
    def __init__(self, name, position, team):
        self.name = name
        self.position = position
        self.team = team
        self.salary = 0

    def add_salary(self, salary_amount):
        self.salary += salary_amount

    def fine(self, fine_amount):
        self.salary -= fine_amount

    def trade_player(self, new_team):
        self.team = new_team

lebron_james = NBAPlayer("Lebron James", "PG", "Lakers")
lebron_james.add_salary(35000000)
print("{} salary is ${}.".format(lebron_james.name, lebron_james.salary))

carmelo_anthony = NBAPlayer("Carmelo Anthony", "SF", "Rockets")
carmelo_anthony.add_salary(5000000)
print("{} salary is ${}.".format(carmelo_anthony.name, carmelo_anthony.salary))

carmelo_anthony.fine(20000)
print(f"{carmelo_anthony.name} is fine 20000")

carmelo_anthony.trade_player("Blazers")
print(f"{carmelo_anthony.name} is currently a member of the {carmelo_anthony.team}")