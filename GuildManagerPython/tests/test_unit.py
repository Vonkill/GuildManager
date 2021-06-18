import unittest
from unit import Unit
from job import Warrior, Wizard


class TestUnit(unittest.TestCase):
    """Unit tests for basic Unit functionality."""

    unit = None

    @classmethod
    def setUpClass(cls):
        cls.unit = Unit(name="Bob Dole", level=1, character_job=Wizard)

    @classmethod
    def tearDownClass(cls):
        cls.unit = None

    def test_unit_attributes(self):
        self.assertTrue(hasattr(self.unit, "name"))
        self.assertTrue(hasattr(self.unit, "level"))
        self.assertTrue(hasattr(self.unit, "job"))

    def test_unit_attribute_values(self):
        self.assertEqual(self.unit.name, "Bob Dole")
        self.assertEqual(self.unit.level, 1)
        self.assertEqual(self.unit.job.job_title, "Wizard")

    def test_unit_representation(self):
        string_rep = "Bob Dole - Wizard Lvl 1"
        self.assertEqual(string_rep, str(self.unit))

    def test_unit_representation_bad(self):
        string_rep = "Bob Dole - Wizard Lvl 2"
        self.assertNotEqual(string_rep, str(self.unit))
