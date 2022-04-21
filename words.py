def print_upper_words(words):
    """Print each word on sep line, uppercased.

        >>> print_upper_words(["Yazan", "Hi", "one", "two"])
        YAZAN
        HI
        ONE
        TWO
    """

    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """Print each word on sep line, uppercased, if starts with E or e.

        >>> print_upper_words2(["End", "Eric", "Yazan"])
        END
        ERIC
    """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["ERIC", "Ed", "Ali", "rick"],
        ...                   must_start_with=["A", "E"])
        Ed
        Ali
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
