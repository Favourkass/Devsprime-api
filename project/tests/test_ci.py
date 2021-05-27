from unittest import TestCase


class TestCI(TestCase):
  def test_ci(self):
    self.assertTrue(True)

  def test_ci_2(self):
    self.assertEqual(2 + 3, 5)


