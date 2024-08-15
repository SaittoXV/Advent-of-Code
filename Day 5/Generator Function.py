
def main():
    print("before generator object created")
    generatorObject = generator()
    # print(next(generatorObject))
    # print("after generator object created")

    x = (i for i in range(10))
    for item in iter(x):
        print(item)


def generator():
    for i in range(1, 100000):
        yield i
        print(i)


if __name__ == "__main__":
    main()
