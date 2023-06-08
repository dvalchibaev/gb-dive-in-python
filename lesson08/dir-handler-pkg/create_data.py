from random import randint, random, choices, choice
from string import ascii_letters
import os


def create_data(n: int = 12) -> bool:
    TYPES = ('dir', 'byte')
    os.mkdir('TEST')
    for _ in range(n):
        name = ''.join(choices(ascii_letters, k=randint(6, 10)))
        file_type = choice(TYPES)
        if file_type == 'dir':
            os.mkdir(f'TEST/{name}')
            print(name)
        else:
            print(f'file: {name}')
    return True


if __name__ == "__main__":
    create_data()


