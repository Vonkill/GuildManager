class Party:
    """The Basic Party class - the groups of units being sent on raids."""

    def __init__(self, party_name, party_size):
        """Initialize our party; only require the name and party size."""
        self.party_name = party_name
        self.party_size = party_size
        self.party_members = []

    def __str__(self):
        return f"{self.party_name}: ({';'.join(self.party_members)})"

    def add_party_member(self, party_member):
        """Add a party member to the party."""

        if len(self.party_members) < self.party_size:
            self.party_members.append(party_member)
        else:
            raise Exception("Party is Full")

    def remove_party_member(self, party_member):
        """Remove a party member from the party."""

        self.party_members.remove(party_member)

    def rename_party(self, new_party_name):
        self.party_name = new_party_name
