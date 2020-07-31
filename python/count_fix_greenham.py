

def reader(file):
    with open(file, "r") as f:
        text = f.read()
        return text


def writer(text):
    with open("greenham_fixed.txt", "w") as f:
        f.writelines(text)
        return "Done"


def fix_i_case(text):
    corrected_text = ""
    error_counter = 0
    for ndex in range(0, len(text)):
        if (text[ndex] == "i" and not text[ndex - 1].isalpha() and
            not text[ndex + 1].isalpha()):
            corrected_text += "I"
            error_counter += 1
        else:
            corrected_text += text[ndex]
    return (error_counter, corrected_text)


text = reader("greenham.txt")

results = fix_i_case(text)
print(results[0])
writer(results[1])
