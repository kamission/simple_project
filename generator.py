def letter_generator(name):
    for letter in name:
        print(f"Letters left {len(name) - (name.index(letter) + 1)}")
        yield name
