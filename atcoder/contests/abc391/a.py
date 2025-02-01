def direction_mapping(direction):
    if direction == "N":
        return "S"
    elif direction == "S":
        return "N"
    elif direction == "E":
        return "W"
    elif direction == "W":
        return "E"
    elif direction == "NE":
        return "SW"
    elif direction == "SE":
        return "NW"
    elif direction == "SW":
        return "NE"
    elif direction == "NW":
        return "SE"


def main():
    n = input()
    print(direction_mapping(n))


if __name__ == "__main__":
    main()
