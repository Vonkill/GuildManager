class Job:
    """Base class for all Jobs a unit can have"""

    def __init__(self, level=1):
        self.job_title = ""
        self.level = level
        self.hp_multiplier = 0
        self.mp_multiplier = 0
        self.speed_multiplier = 0
        self.base_atk = 0
        self.base_mg_atk = 0

    def __str__(self):
        return f"{self.job_title} Lvl {self.level}"

    def calculate_stats(self):
        return (
            self.level * self.hp_multiplier,
            self.level * self.mp_multiplier,
            self.level * self.speed_multiplier
        )


class Warrior(Job):
    """The Warrior class."""

    def __init__(self, level=1):
        super().__init__(level)
        self.job_title = "Warrior"
        self.hp_multiplier = 12
        self.mp_multiplier = 0
        self.speed_multiplier = 5
        self.base_atk = 8

    def __str__(self):
        return super().__str__()

    def calculate_stats(self):
        return super.calculate_stats()


class Wizard(Job):
    """The Wizard class."""

    def __init__(self, level=1):
        super().__init__(level)
        self.job_title = "Wizard"
        self.hp_multiplier = 6
        self.mp_multiplier = 12
        self.speed_multiplier = 3
        self.base_atk = 1
        self.base_mg_atk = 6

    def __str__(self):
        return super().__str__()

    def calculate_stats(self):
        return super.calculate_stats()


class Priest(Job):
    """The Priest Class."""

    def __init__(self, level=1):
        super().__init__(level)
        self.job_title = "Priest"
        self.hp_multiplier = 8
        self.mp_multiplier = 10
        self.speed_multiplier = 4
        self.base_atk = 4
        self.base_mg_atk = 4

    def __str__(self):
        return super().__str__()

    def calculate_stats(self):
        return super.calculate_stats()
