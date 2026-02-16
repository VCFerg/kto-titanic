from typing import List
import unittest

MAX_NAME_LENGTH: int = 7


def greet(name: str) -> str:
    return f"Bonjour {name}"


def count_names_longer_than(names: List[str], max_length: int) -> int:
    return sum(1 for name in names if len(name) > max_length)


def describe_name_length(name: str, max_length: int) -> str:
    if len(name) > max_length:
        return f"{name} est un prénom avec un nombre de lettres supérieur à {max_length}"
    return f"{name} est un prénom avec un nombre de lettres inférieur ou égal à {max_length}"


def main() -> None:
    message: str = "C'est mon premier script !!!"
    print(message)

    first_names: List[str] = [
        "Guillaume",
        "Gilles",
        "Juliette",
        "Antoine",
        "François",
        "Cassandre",
    ]

    for first_name in first_names:
        print(describe_name_length(first_name, MAX_NAME_LENGTH))

    count: int = count_names_longer_than(first_names, MAX_NAME_LENGTH)
    print(f"Nombre de prénoms dont le nombre de lettres est supérieur à {MAX_NAME_LENGTH} : {count}")

    print(greet("Alice"))


class TestNameUtilities(unittest.TestCase):
    def test_count_names_longer_than(self) -> None:
        names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_names_longer_than(names, MAX_NAME_LENGTH)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    main()
    unittest.main()
