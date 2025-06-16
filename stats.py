def get_num_words(content):
    words = content.split()
    return len(words)

def count_characters(content):
    result = {}
    content = content.lower()
    for letter in content:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

def sort_on(dict):
    return dict["num"]

def sorted(dict):
    result = [{"char": k, "num": v} for k, v in dict.items()]
    result.sort(reverse=True, key=sort_on)
    return result