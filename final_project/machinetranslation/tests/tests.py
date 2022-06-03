import unittest
from translator import english_to_french, french_to_english

class Testfrench(unittest.TestCase): 
    def test1(self):
        self.assertIsNone(english_to_french(None))

    def test2(self):
         self.assertEqual(english_to_french('Hello'), 'Bonjour')
         self.assertNotEqual(english_to_french('Bonjour'), 'Hello')
        
        

class Testenglish(unittest.TestCase): 
    def test1(self):
        self.assertIsNone(french_to_english(None))

    def test2(self):
         self.assertEqual(french_to_english('Bonjour'), 'Hello')
         self.assertNotEqual(french_to_english('Hello'), 'Bonjour')
        
unittest.main()
