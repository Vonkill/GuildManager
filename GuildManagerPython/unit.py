from job import Job, Warrior


class Unit:
    def __init__(self, name="", level=1, character_job=Job):
        self.name = name
        self.level = level
        self.job = character_job(level)

    def __str__(self):
        return f"{self.name} - {self.job}"
