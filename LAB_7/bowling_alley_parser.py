def format_player_name(name):
    """
    Safely formats a player name.
    Converts the name to title case and limits it to 10 characters.
    """
    if not isinstance(name, str):
        return ""

    return name.strip().title()[:10]


def parse_frame(text):
    """
    Safely converts bowling frame notation into pins knocked down.

    X  -> (10, 0)
    7/ -> (7, 3)
    45 -> (4, 5)

    Invalid inputs return (0, 0).
    """
    if not isinstance(text, str):
        return (0, 0)

    text = text.strip().upper()

    if text == "X":
        return (10, 0)

    if len(text) != 2:
        return (0, 0)

    if text[0] not in "0123456789":
        return (0, 0)

    first = int(text[0])

    if text[1] == "/":
        return (first, 10 - first)

    if text[1] not in "0123456789":
        return (0, 0)

    second = int(text[1])

    if first + second > 10:
        return (0, 0)

    return (first, second)


def parse_scoreboard(text):
    """
    Safely parses scoreboard entries into a dictionary.
    Invalid entries are ignored.
    """
    scores = {}

    if not isinstance(text, str):
        return scores

    for entry in text.split(","):
        parts = entry.split(":")

        if len(parts) != 2:
            continue

        name = parts[0].strip()
        score_text = parts[1].strip()

        if not name or not score_text:
            continue

        try:
            score = int(score_text)
        except ValueError:
            continue

        scores[name] = score

    return scores


def main():
    print("==== Running format_player_name ====")
    value = input("Enter a player name for the scoreboard: ")
    print("Scoreboard name:", format_player_name(value))

    print("\n==== Running parse_frame ====")
    value = input(
        "Enter a frame as X (strike), 7/ (spare) or two digits (e.g. 45): "
    )
    print("Pins (first roll, second roll):", parse_frame(value))

    print("\n==== Running parse_scoreboard ====")
    value = input(
        "Enter scores as NAME:SCORE separated by commas "
        "(e.g. Asha:150,Ravi:132): "
    )
    print("Scoreboard:", parse_scoreboard(value))


if __name__ == "__main__":
    main()