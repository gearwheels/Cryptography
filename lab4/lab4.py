import random

def split_words(a_text):
    cur_word = ''
    prev_is_alpha = False

    for letter in a_text:
        if letter.isdigit():
            continue
        if  (letter.isalpha() and prev_is_alpha):
            cur_word += letter
        elif (letter.isalpha() and not prev_is_alpha):
            if cur_word: yield cur_word
            cur_word = letter
            prev_is_alpha = not prev_is_alpha
        else:
            if cur_word: yield cur_word
            cur_word = ''
            prev_is_alpha = False
    if cur_word: yield cur_word

def generate_random_chars(alphabet, lenght):
    ans = ""
    max_idx = len(alphabet) - 1
    for _ in range(lenght):
        ans += alphabet[random.randint(0, max_idx)]
    return ans

def generate_random_words(base, lenght):
    gen_len = 0
    ans = ""
    while gen_len < lenght:
        possible_words = list(filter(lambda x: len(x) <= lenght - gen_len, base))
        idx = random.randint(0, len(possible_words)-1)
        ans += possible_words[idx]
        gen_len += len(possible_words[idx])
        if gen_len < lenght:
            ans += " "
            gen_len += 1
    return ans

def compare_texts(text1, text2):
    if len(text1) != len(text2):
        raise ValueError
    lenght = len(text1)
    equals = 0
    for i in range(lenght):
        if text1[i] == text2[i]:
            equals += 1
    return equals / lenght

def clean_dict(old_dict):
    new_dict = set()
    for symbol in old_dict:
        if((symbol >= 'а' and symbol <= 'я') or symbol == ' '):
            new_dict.add(symbol)

    return new_dict


if __name__ == '__main__':
    filepath = "D:\\education\\education\\Cripta\\lab4\\resource\\oblako.txt"
    random.seed(42)
    oblako = ""
    with open(filepath, 'r', encoding='utf-8') as txt:
        oblako = txt.read()

    oblako_words = list(map(lambda x: x.lower(), split_words(oblako)))
    print(oblako_words[:15])

    oblako_text = " ".join(oblako_words)
    print(oblako_text[:100])

#####################################################################################################

    print("\nОсмысленные тексты: \n")

    text_len = len(oblako_text) // 2

    human_text1 = oblako_text[:text_len]
    print("Длина полученного текста №1:", len(human_text1))

    with open("D:\\education\\education\\Cripta\\lab4\\resource\\human1.txt", 'w') as f:
        f.write(human_text1)

    human_text2 = oblako_text[text_len:2 * text_len]
    print("Длина полученного текста №2:", len(human_text2))

    with open("D:\\education\\education\\Cripta\\lab4\\resource\\human2.txt", 'w') as f:
        f.write(human_text2)

##################################################################################################

    print("\nТексты сгенерированные по словам: \n")

    old_alphabet = list(set(oblako_text))
    alphabet = list(clean_dict(old_alphabet))
    print("Длина алфавита:", len(alphabet))

    chars_text1 = generate_random_chars(alphabet, text_len)
    print("Длина сгенерированного текста №1:", len(chars_text1))

    with open("D:\\education\\education\\Cripta\\lab4\\resource\\chars1.txt", 'w') as f:
        f.write(chars_text1)

    chars_text2 = generate_random_chars(alphabet, text_len)
    print("Длина сгенерированного текста №2:", len(chars_text2))

    with open("D:\\education\\education\\Cripta\\lab4\\resource\\chars2.txt", 'w') as f:
        f.write(chars_text2)

    word_base = list(set(oblako_words))

###################################################################################################

    print("\nТексты сгенерированные по буквам: \n")

    words_text1 = generate_random_words(word_base, text_len)
    print("Длина сгенерированного текста №1:", len(words_text1))

    with open("D:\\education\\education\\Cripta\\lab4\\resource\\words1.txt", 'w') as f:
        f.write(words_text1)

    words_text2 = generate_random_words(word_base, text_len)
    print("Длина сгенерированного текста №2:", len(words_text2))

    with open("D:\\education\\education\\Cripta\\lab4\\resource\\words2.txt", 'w') as f:
        f.write(words_text2)

#################################################################################################

    ans = compare_texts(human_text1, human_text2)
    print(f"\nДоля совпадений в словах осмысленных текстов: {ans * 100:.2f}% \n")

    mean = 0

    ans = compare_texts(human_text1, chars_text1)
    mean += ans
    print(f"Доля совпадений в словах осмысленного текста №1 и сгенерированного из букв текста №1: {ans * 100:.2f}%")

    ans = compare_texts(human_text1, chars_text2)
    mean += ans
    print(f"Доля совпадений в словах осмысленного текста №1 и сгенерированного из букв текста №2: {ans * 100:.2f}%")

    ans = compare_texts(human_text2, chars_text1)
    mean += ans
    print(f"Доля совпадений в словах осмысленного текста №2 и сгенерированного из букв текста №1: {ans * 100:.2f}%")

    ans = compare_texts(human_text2, chars_text2)
    mean += ans
    print(f"Доля совпадений в словах осмысленного текста №2 и сгенерированного из букв текста №2: {ans * 100:.2f}%")

    print(f"Средняя доля совпадений в словах: {(mean / 4) * 100:.2f}% \n")

    mean = 0

    ans = compare_texts(human_text1, words_text1)
    mean += ans
    print(f"Доля совпадений в словах осмысленного текста №1  и сгенерированного из слов текста №1: {ans * 100:.2f}%")

    ans = compare_texts(human_text1, words_text2)
    mean += ans
    print(f"Доля совпадений в словах осмысленного текста №1  и сгенерированного из слов текста №2: {ans * 100:.2f}%")

    ans = compare_texts(human_text2, words_text1)
    mean += ans
    print(f"Доля совпадений в словах осмысленного текста №2  и сгенерированного из слов текста №1: {ans * 100:.2f}%")

    ans = compare_texts(human_text2, words_text2)
    mean += ans
    print(f"Доля совпадений в словах осмысленного текста №2  и сгенерированного из слов текста №2: {ans * 100:.2f}%")

    print(f"Средняя доля совпадений в словах: {(mean / 4) * 100:.2f}%\n")

    ans = compare_texts(chars_text1, chars_text2)
    print(f"Доля совпадений в словах сгенерированного из букв текста №1 и сгенерированного из букв текста №2: {ans * 100:.2f}%")

    ans = compare_texts(words_text1, words_text2)
    print(f"Доля совпадений в словах сгенерированного из слов текста №1 и сгенерированного из слов текста №2: {ans * 100:.2f}%")

