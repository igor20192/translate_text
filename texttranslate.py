from translate import Translator
import logging
import fire
import os
import time

logging.basicConfig(
    filename="translate.log", format="[%(asctime)s] [%(levelname)s] => %(message)s]"
)

start_time = time.perf_counter()


def translatios(lang):
    translator = Translator(to_lang=lang)
    try:
        with open("input.txt", "r") as f:
            for row in f:
                translation = translator.translate(f"""{row}""")
                yield translation
    except Exception as error:
        logging.exception("%s", error.__doc__)


def write_file(lang, clean=None):
    if clean:
        os.system(":> $PWD/translate.txt")
    try:
        with open("translate.txt", "a") as f:
            for row in translatios(lang):
                f.write(f"{row}\n")
        os.system("vim translate.txt")
        print("Время выполнения: ", end_time - start_time, "секунд")
    except Exception as error:
        logging.exception("%s", error.__doc__)


end_time = time.perf_counter()

if __name__ == "__main__":
    fire.Fire({"--translate": write_file, "-tr": write_file})
