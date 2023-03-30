import unittest
import os
from unittest.mock import patch, mock_open
from concurrent.futures import ThreadPoolExecutor
from translate import Translator
from text_translate import translatios, write_file


class TestTranslations(unittest.TestCase):
    def test_translations(self):
        lang = "ru"
        translator = Translator(to_lang=lang)
        translation = translator.translate("Hello")
        self.assertEqual(translation, "Привет")


class TestWriteFile(unittest.TestCase):
    def setUp(self):
        self.mock_open = mock_open()

    @patch("main.open", new_callable=self.mock_open)
    def test_write_file(self, mock_file):
        lang = "ru"
        clean = True

        # Мокаем результат функции translatios()
        with patch("main.translatios") as mock_translations:
            mock_translations.return_value = ["Привет", "Мир"]
            write_file(lang, clean)

        # Проверяем, что файл создан и записан корректно
        mock_file.assert_called_once_with("translate.txt", "a")
        handle = mock_file()
        handle.write.assert_has_calls(
            [unittest.mock.call("Привет\n"), unittest.mock.call("Мир\n")]
        )

    def test_write_file_no_clean(self):
        lang = "ru"
        clean = False

        # Мокаем результат функции translatios()
        with patch("main.translatios") as mock_translations:
            mock_translations.return_value = ["Привет", "Мир"]
            write_file(lang, clean)

        # Проверяем, что файл создан и записан корректно
        with open("translate.txt", "r") as f:
            contents = f.read()
            self.assertIn("Привет", contents)
            self.assertIn("Мир", contents)


class TestConcurrency(unittest.TestCase):
    def test_concurrency(self):
        lang = "ru"
        with ThreadPoolExecutor(max_workers=2) as executor:
            future = executor.submit(translatios, lang)
            self.assertIsInstance(future.result(), list)


if __name__ == "__main__":
    unittest.main()
