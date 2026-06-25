class guest:
    def __init__(self, name):
        self.name = name
    def invite(self):
        if self.name == "Bob":
            print(f"Dear {self.name}, you are not invited to the party.")
        else:
            print(f"Dear {self.name}, you are invited to the party.")
guest1 = guest("Alice")
guest2 = guest("Bob")
guest3 = guest("Charlie")
for guest in [guest1, guest2, guest3]:
    guest.invite()