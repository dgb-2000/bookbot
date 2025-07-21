def get_num_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count


def get_char_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(items):
    return items["num"]


def get_report(dict):
    dict_list = []
    for char in dict:
        char_dict = {
            "char": char,
            "num": dict[char]
        }
        dict_list.append(char_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
