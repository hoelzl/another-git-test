def say_hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    greeting = say_hello(name)
    print(greeting)
