def scoreWord(word):
    score = 0
    for i in word:
        if (i.isalpha() == True):
            num = 0
            if (ord(i) > 64) and (ord(i) < 91):
                num = ord(i) - 65
            if (ord(i) > 96) and (ord(i) < 123):
                num = ord(i) - 97
            score = score + num
    return score



if __name__ == '__main__':
    provided = [
        "One",
        "oNE",
        "supercalifragilisticexpialidocious",
        "t",
        "aAaA",
        "Zap!",
        "Tr!ck3d y4!",
        "G0t it!"
    ]

    # For each word in the provided list, give the word to the function score word and print some fancy formatted output
    for word in provided:
        print(f"The score of {word} is: {scoreWord(word)}")

    # Should Output:
        # The score of One is: 31
        # The score of oNE is: 31
        # The score of supercalifragilisticexpialidocious is: 345
        # The score of t is: 19
        # The score of aAaA is: 0
        # The score of Zap! is: 40
        # The score of Tr!ck3d y4! is: 75
        # The score of G0t it! is: 52