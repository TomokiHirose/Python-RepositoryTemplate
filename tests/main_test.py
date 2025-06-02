import unittest
import sys
import os

# srcディレクトリをパスに追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import add


class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        """正の数の足し算テスト"""
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        """負の数の足し算テスト"""
        self.assertEqual(add(-3, -5), -8)
        self.assertEqual(add(-10, 5), -5)

    def test_add_zero(self):
        """ゼロとの足し算テスト"""
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(10, 0), 10)
        self.assertEqual(add(0, 0), 0)

    def test_add_floats(self):
        """小数の足し算テスト"""
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)


if __name__ == "__main__":
    unittest.main()
