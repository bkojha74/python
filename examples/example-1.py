import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass(frozen=False)
class DecoratePerson:
    name: str
    address: str
    active: bool = True
    email_address: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self.search_string = f"NAME:{self.name} ADDRESS:{self.address}"
    

class Person:
    def __init__(self, name:string, address:string):
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name}, {self.address}"

def main() -> None:
    person = Person("Bipin", "GoldenPark Appartments")
    decoratePerson = DecoratePerson("Bipin", "GoldenPark Appartments")
    print(person)
    print(decoratePerson)

if __name__ == "__main__":
    main()

