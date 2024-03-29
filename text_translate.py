from concurrent.futures import ThreadPoolExecutor
from translate import Translator
import logging
import fire
import os


logging.basicConfig(
    filename="translate.log", format="[%(asctime)s] [%(levelname)s] => %(message)s]"
)


def translatios():
    try:
        with open("input.txt", "r") as f:
            return list(map(str.strip, f))
    except Exception as error:
        logging.exception("%s", error.__doc__)


def write_file(lang, clean=None):
    translator = Translator(to_lang=lang)
    if clean:
        os.system(":> $PWD/translate.txt")
    try:
        with open("translate.txt", "a") as f:
            with ThreadPoolExecutor() as executor:
                results = executor.map(translator.translate, translatios())
            for row in results:
                f.write(f"{row}\n")
        os.system("vim translate.txt")
    except Exception as error:
        logging.exception("%s", error.__doc__)


if __name__ == "__main__":
    fire.Fire({"--translate": write_file, "-tr": write_file})
