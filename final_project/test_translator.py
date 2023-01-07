import unittest
import translator

class TestTranslator(unittest.TestCase):
    def test_translator(self):

        data = 'boire'
        result = translator.french_to_english(data)
        print("frenchToEnglish - assertEqual")
        self.assertEqual(result, 'Drink')
        print("frenchToEnglish - assertNotEqual")
        self.assertNotEqual(result, 'boire')

        data = 'drink'
        result = translator.english_to_french(data)
        print("englishToFrench - assertEqual")
        self.assertEqual(result, 'Boisson')
        print("englishToFrench - assertNotEqual")
        self.assertNotEqual(result, 'drink')

if __name__ == '__main__':
    unittest.main()
