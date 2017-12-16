from typing import Dict

class Z:
    a: int

    def __init__(self, a: int):
        self.a = a

def z(b: str) -> Dict[str, Z]:
    print(f'{z}')
    return {b: Z(2)}

print(z(''))
