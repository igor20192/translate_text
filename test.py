import unittest
from translate import Translator
import os
from text_translate import write_file


class TestTranslations(unittest.TestCase):
    def test_translations(self):
        lang = "ru"
        translator = Translator(to_lang=lang)
        translation = translator.translate("Hello")
        self.assertEqual(translation, "Привет")


class TestWriteFile(unittest.TestCase):
    def test_write_file(self):
        lang = "ru"
        clean = True
        write_file(lang, clean)
        with open("translate.txt", "r") as f:
            contents = f.read()
            self.assertTrue("Привет" in contents)


if __name__ == "__main__":
    unittest.main()
