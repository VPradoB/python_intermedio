def run():
    super_list: list = [
        {"firstname": "Victor", "lastname": "Prado"},
        {"firstname": "Angel", "lastname": "Ramirez"},
        {"firstname": "Ismael", "lastname": "Prado"},
    ]
    super_dict = {
        "natural_number": [1, 2, 3, 4],
        "integer_number": [1, -2, 3, -4],
        "floating_number": [1.1, -2.3, 3.4, -4.5],
    }

    for i, v in super_dict.items():
        print(f"{i}: {v}")

    for i, v in enumerate(super_list):
        print(f"{i}: {v}")


if __name__ == "__main__":
    run()
