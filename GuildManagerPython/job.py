class Job:
    def __init__(self, level=1):
        self.job_title = ""
        self.level = level
        self.hp_multiplier = 0
        self.mp_multiplier = 0
        self.speed_multiplier = 0

    def __str__(self):
        return f"{self.job_title} Lvl {self.level}"

    def calculate_stats(self):
        return (
            self.level * self.hp_multiplier,
            self.level * self.mp_multiplier,
            self.level * self.speed_multiplier
        )


class Warrior(Job):
    def __init__(self, level=1):
        super().__init__(level)
        self.job_title = "Warrior"
        self.hp_multiplier = 12
        self.mp_multiplier = 0
        self.speed_multiplier = 5

    def __str__(self):
        return super().__str__()

    def calculate_stats(self):
        return super.calculate_stats()


class Wizard(Job):
    def __init__(self, level=1):
        super().__init__(level)
        self.job_title = "Wizard"
        self.hp_multiplier = 6
        self.mp_multiplier = 12
        self.speed_multiplier = 3

    def __str__(self):
        return super().__str__()

    def calculate_stats(self):
        return super.calculate_stats()


class Priest(Job):
    def __init__(self, level=1):
        super().__init__(level)
        self.job_title = "Priest"
        self.hp_multiplier = 8
        self.mp_multiplier = 10
        self.speed_multiplier = 4

    def __str__(self):
        return super().__str__()

    def calculate_stats(self):
        return super.calculate_stats()
