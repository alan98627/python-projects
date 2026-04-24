from validator import validate
from data import medical_records


def main() -> None:
    print("Running Medical Data Validator...\n")

    result = validate(medical_records)

    if result:
        print("\nAll records are valid ")
    else:
        print("\nSome records are invalid ")


if __name__ == "__main__":
    main()