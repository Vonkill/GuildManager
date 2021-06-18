import unittest
from job import Priest, Warrior, Wizard


class TestJob(unittest.TestCase):
    """Unit tests for basic Job functionality."""

    priest = None
    warrior = None
    wizard = None

    @classmethod
    def setUpClass(cls):
        cls.priest = Priest(level=1)
        cls.warrior = Warrior(level=1)
        cls.wizard = Wizard(level=1)

    @classmethod
    def tearDownClass(cls):
        cls.priest = None
        cls.warrior = None
        cls.wizard = None

    def test_priest_attributes(self):
        self.assertTrue(hasattr(self.priest, "job_title"))
        self.assertTrue(hasattr(self.priest, "hp_multiplier"))
        self.assertTrue(hasattr(self.priest, "mp_multiplier"))
        self.assertTrue(hasattr(self.priest, "speed_multiplier"))
        self.assertTrue(hasattr(self.priest, "base_atk"))
        self.assertTrue(hasattr(self.priest, "base_mg_atk"))

    def test_priest_attribute_values(self):
        self.assertEqual(self.priest.job_title, "Priest")
        self.assertEqual(self.priest.hp_multiplier, 8)
        self.assertEqual(self.priest.mp_multiplier, 10)
        self.assertEqual(self.priest.speed_multiplier, 4)
        self.assertEqual(self.priest.base_atk, 4)
        self.assertEqual(self.priest.base_mg_atk, 4)

    def test_warrior_attributes(self):
        self.assertTrue(hasattr(self.warrior, "job_title"))
        self.assertTrue(hasattr(self.warrior, "hp_multiplier"))
        self.assertTrue(hasattr(self.warrior, "mp_multiplier"))
        self.assertTrue(hasattr(self.warrior, "speed_multiplier"))
        self.assertTrue(hasattr(self.warrior, "base_atk"))
        self.assertTrue(hasattr(self.warrior, "base_mg_atk"))

    def test_warrior_attribute_values(self):
        self.assertEqual(self.warrior.job_title, "Warrior")
        self.assertEqual(self.warrior.hp_multiplier, 12)
        self.assertEqual(self.warrior.mp_multiplier, 0)
        self.assertEqual(self.warrior.speed_multiplier, 5)
        self.assertEqual(self.warrior.base_atk, 8)
        self.assertEqual(self.warrior.base_mg_atk, 0)

    def test_wizard_attributes(self):
        self.assertTrue(hasattr(self.warrior, "job_title"))
        self.assertTrue(hasattr(self.warrior, "hp_multiplier"))
        self.assertTrue(hasattr(self.warrior, "mp_multiplier"))
        self.assertTrue(hasattr(self.warrior, "speed_multiplier"))
        self.assertTrue(hasattr(self.warrior, "base_atk"))
        self.assertTrue(hasattr(self.warrior, "base_mg_atk"))

    def test_wizard_attribute_values(self):
        self.assertEqual(self.wizard.job_title, "Wizard")
        self.assertEqual(self.wizard.hp_multiplier, 6)
        self.assertEqual(self.wizard.mp_multiplier, 12)
        self.assertEqual(self.wizard.speed_multiplier, 3)
        self.assertEqual(self.wizard.base_atk, 1)
        self.assertEqual(self.wizard.base_mg_atk, 6)

    # TODO: Add in tests for calculating stats
    # TODO: Add in check for representation of Job string
    # TODO: Add in docstrings for all unittests
