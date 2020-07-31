def google_casify(sentence):
    """
    Returns the provided string in Google Case by
    first splitting the string into a list, filtering
    out any empty elements (extra spaces) and then
    looping through the result to make the first
    letter lowercase and the rest of the word uppercase.

    :param sentence: the string to be converted
    :return: a string representing the converted sentence
    """
    sentence_list = filter(None, sentence.split(" "))
    converted = []
    for word in sentence_list:
        converted.append(word[0].lower() + word[1:].upper())
    return " ".join(converted)


def camel_casify(sentence):
    """
    Returns the provided string in Camel Case by
    first spiltting the string into a list, filtering
    out any empty elements (extra spaces) and then
    looping through the resulting list of elements (words)

    The first element is dropped to lowercase, while the
    rest have the first character capitalized and the remaining
    changed to lowercase.

    :param sentence: the string to be converted
    :return: a string representing the converted sentence
    """
    sentence_list = list(filter(None, sentence.split(" ")))
    converted = []
    for ndex in range(0, len(sentence_list)):
        if ndex == 0:
            converted.append(sentence_list[ndex].lower())
        else:
            converted.append(sentence_list[ndex][0].upper() +
                             sentence_list[ndex][1:].lower())
    return "".join(converted)


def main():
    while True:
        sentence = ""
        while not sentence:
            sentence = input("Enter sentence to convert >> ")
        if sentence.lower() in ["quit", "q"]:
            break
        else:
            print("Google Case: {}".format(google_casify(sentence)))
            print("Camel Case: {}".format(camel_casify(sentence)))


main()
