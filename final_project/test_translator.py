import unittest
import translator

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        data = 'drink'
        result = translator.english_to_french(data)
        self.assertEqual(result, 'Boisson')
        self.assertNotEqual(result, 'drink')

    def test_french_to_english(self):
        data = 'boire'
        result = translator.french_to_english(data)
        self.assertEqual(result, 'Drink')
        self.assertNotEqual(result, 'boire')

if __name__ == '__main__':
    unittest.main()
