#  Thresholds
BULKY_VOLUME_THRESHOLD = 1_000_000 # cm³
BULKY_DIMENSION_THRESHOLD = 150 # cm
HEAVY_MASS_THRESHOLD = 20 # kg


def is_bulky(width: int, height: int, length: int) -> bool:
    volume = width * height * length
    largest_dimension = max(width, height, length)
    return volume >= BULKY_VOLUME_THRESHOLD or largest_dimension >= BULKY_DIMENSION_THRESHOLD

def is_heavy(mass: int) -> bool:
    return mass >= HEAVY_MASS_THRESHOLD

def sort(width: int, height: int, length: int, mass: int) -> str:
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"


import unittest

class TestSortFunction(unittest.TestCase):

    def test_standard_package(self):
        self.assertEqual(sort(50, 50, 50, 10), "STANDARD")

    def test_bulky_due_to_volume(self):
        self.assertEqual(sort(200, 200, 30, 10), "SPECIAL")

    def test_bulky_due_to_dimension(self):
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")

    def test_heavy_package(self):
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_both_bulky_and_heavy(self):
        self.assertEqual(sort(200, 200, 30, 25), "REJECTED")

    def test_edge_case_volume_exact(self):
        self.assertEqual(sort(100, 100, 100, 19), "SPECIAL")

    def test_edge_case_mass_exact(self):
        self.assertEqual(sort(50, 50, 50, 20), "SPECIAL")

    def test_edge_case_dimension_exact(self):
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")

if __name__ == "__main__":
    unittest.main()
