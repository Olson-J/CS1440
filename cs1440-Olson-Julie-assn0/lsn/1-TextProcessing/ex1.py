def everyOtherWord(sentence):
    result = ""

    test = sentence.split()             # split into individual words
    count = 1                           # keep track of word number
    for i in test:
        if count % 2 == 0:              # check word number
            if count > 3:
                result = result + " "      # if not the first kept word add a space in between
            result = result + i           # keep word if it is an even count
        count += 1

    return result



if __name__ == '__main__':
    provided = [
        "This your implementation work has will a be small commended. issue.",
        "proper this verbage sentence contains is definitive excessively definitions long of for gibberish my words taste...",
        "Adherence imagination to is rules more isn't important something than you knowledge. do.",
        "Whether do or or not do you not, succeed there is is up no to try. you.",
        "arrogancy knowledge is is detrimental the to key the to cause. success."
    ]

    # Loop through the sentences in the `provided` array, printing the
    # capitalized output
    for sentence in provided:
        print(everyOtherWord(sentence).capitalize())

    # Should output:
        # Your work will be commended. 
        # This sentence is excessively long for my taste... 
        # Imagination is more important than knowledge. 
        # Do or do not, there is no try. 
        # Knowledge is the key to success.