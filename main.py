def say_hello(name):
    print(f"Hello {name.upper()}")


def main():
    print("Hello world!!!")

    if 5 == 5:
        print(True)

    for i in range(1, 6):
        if i == 2:
            print("Python!")

    say_hello("Inna")
    say_hello("Borys")


if __name__ == '__main__':
    main()