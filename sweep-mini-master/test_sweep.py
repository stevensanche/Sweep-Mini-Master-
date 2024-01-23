import sweep   # You write sweep.py
import unittest
import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class TestSame(unittest.TestCase):
    def test_same(self):
        before = [1, 3, 5, 7]
        saved = before.copy()
        self.assertFalse(sweep.all_same(before))
        self.assertEqual(before, saved)
        self.assertTrue(sweep.all_same([]))
        self.assertTrue(sweep.all_same([3, 3, 3]))
        self.assertTrue(sweep.all_same([5, 5]))
        self.assertFalse(sweep.all_same([1, 1, 1, 3, 1]))
        self.assertFalse(sweep.all_same([1, 1, 1, 5]))

class TestMaxRun(unittest.TestCase):
    def test_run(self):
        before = [1, 1, 3, 3, 3, 5]
        saved = before.copy()
        self.assertEqual(sweep.max_run(before), 3)
        self.assertEqual(before, saved)
        self.assertEqual(sweep.max_run([]), 0)
        self.assertEqual(sweep.max_run([42]), 1)
        self.assertEqual(sweep.max_run([1, 2, 3]), 1)
        self.assertEqual(sweep.max_run([3, 3, 3, 2, 3]), 3)
        self.assertEqual(sweep.max_run([1, 2, 2, 3]), 2)
        self.assertEqual(sweep.max_run([3, 4, 5, 5, 5]), 3)

class TestDedup(unittest.TestCase):
    def test_dedup(self):
        before = [1, 1, 3, 3, 3, 5]
        saved = before.copy()
        self.assertEqual(sweep.dedup(before), [1, 3, 5])
        self.assertEqual(before, saved)
        self.assertEqual(sweep.dedup([]), [])
        self.assertEqual(sweep.dedup([1]), [1])
        self.assertEqual(sweep.dedup([3, 7, 4]), [3, 7, 4])
        self.assertEqual(sweep.dedup([7, 7, 7]), [7])

if __name__ == "__main__":
   unittest.main()
