#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    prefix = "__"
    for name in dir(hidden_4):
        if prefix not in name:
            print(name)
