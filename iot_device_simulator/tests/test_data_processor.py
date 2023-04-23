import unittest
# from ..data_processor import data_processor
# import from parent directory
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from data_processor import data_processor

class TestdataProcessorMethods(unittest.TestCase):
    def test_get_data(self):
        elements = [1, 2, 3, 4, 5]

        processor = data_processor()
        for element in elements:
            processor.processData(element)
        
        self.assertEqual(processor.getAverage(), 3)
        self.assertEqual(processor.getMax(), 5)
        self.assertEqual(processor.getCount(), 5)
    
    def test_no_data(self):
        processor = data_processor()
        self.assertEqual(processor.getAverage(), 0)
        self.assertEqual(processor.getMax(), 0)
        self.assertEqual(processor.getCount(), 0)

if __name__ == '__main__':
    unittest.main()
