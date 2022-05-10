def run():
    my_dict = {i: i**3 for i in range(1, 101) if i ** 3 % 3 != 0}
    print(my_dict)

    home_work = {i: round(i**0.5, 2) for i in range(1, 1001)}
    print(home_work)


if __name__ == "__main__":
    run()
