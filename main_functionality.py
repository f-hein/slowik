import requests
import random
from langs_shortcuts import dict_of_langs
from api_key import api_key

get_langs = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs' + api_key
get_detect_lang = 'https://translate.yandex.net/api/v1.5/tr.json/detect' + api_key
get_translate = 'https://translate.yandex.net/api/v1.5/tr.json/translate' + api_key

languages = requests.get(get_langs)
languages = languages.json()
all_possible_combinations = dict()


def make_shortcuts(sh_from, sh_to):
    return '{}-{}'.format(sh_from, sh_to)


def translate_word(sh_from, sh_to, word):
    translate_shortcuts = make_shortcuts(sh_from, sh_to)
    translated_word = requests.get(get_translate + "&text={}&lang={}".format(word, translate_shortcuts))
    translated_word = translated_word.json()['text'][0]
    print(make_shortcuts(dict_of_langs[sh_from], dict_of_langs[sh_to]), '||', translated_word)
    return translated_word


def get_random_translation(lang_shortcut, word):
    random_lang = random.choice(all_possible_combinations[lang_shortcut])
    translated_word = translate_word(lang_shortcut, random_lang, word)
    return random_lang, translated_word, make_shortcuts(lang_shortcut, random_lang)


def path_to_original_language(predicted_lang, output_lang, history):
    if predicted_lang in all_possible_combinations[output_lang]:
        history.append(make_shortcuts(output_lang, predicted_lang))
        return history
    else:
        for i in all_possible_combinations[output_lang]:
            history.append(make_shortcuts(output_lang, i))
            val = path_to_original_language(predicted_lang, i, history)
            return val


for one_combination in languages['dirs']:
    first_lang, second_lang = one_combination.split('-')
    if first_lang in all_possible_combinations:
        all_possible_combinations[first_lang].append(second_lang)
    else:
        all_possible_combinations[first_lang] = [second_lang]


if __name__ == '__main__':
    while True:
        list_of_jumps = list()
        to_translate = input("Write something to translate: ")
        number_of_jumps = input("Number of jumps: ")
        response = requests.get(get_detect_lang+'&text={}'.format(to_translate))
        predicted_lang = response.json()['lang']
        output_lang, output_word, output_shortcuts = '', '', ''
        for i in range(int(number_of_jumps)):
            if i == 0:
                print(i+1, end='. ')
                output_lang, output_word, output_shortcuts = get_random_translation(predicted_lang, to_translate)
                list_of_jumps.append([output_shortcuts, to_translate, output_word])
            else:
                print(i+1, end='. ')
                temp = output_word
                output_lang, output_word, output_shortcuts = get_random_translation(output_lang, output_word)
                list_of_jumps.append([output_shortcuts, temp, output_word])
        paths_of_translation = path_to_original_language(predicted_lang, output_lang, [])
        for translation in paths_of_translation:
            print('R', end='| ')
            sh_from, sh_to = translation.split('-')
            temp = output_word
            output_word = translate_word(sh_from, sh_to, output_word)
            list_of_jumps.append([translation, temp, output_word])
