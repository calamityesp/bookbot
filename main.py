def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    num_letters = char_count(words)
    print_report(num_letters, words)


def char_count(wordlist):
    letter_dict = {}
    if len(wordlist) == 0:
        return None

    for word in wordlist:
        for letter in word:
            letter = letter.lower()
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict


def print_report(letterDict, words):
    print("--- Begin Report of books/frankenstein.txt ---")
    print(f"{len(words)} words was found in the document")
    print()

    # convert dictionary to list
    letterItems = list(letterDict.items())
    letterItems.sort()
    for item in letterItems:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
