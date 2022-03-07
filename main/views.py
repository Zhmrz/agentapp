import requests
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


URL_AUTH = "https://developers.lingvolive.com/api/v1.1/authenticate/"
URL_TRANSLATE = "https://developers.lingvolive.com/api/v1/Minicard/"
URL_SOUND = "https://developers.lingvolive.com/api/v1/Sound/"


def auth():

    key = "Basic ZjQ0NDI1ZjEtNjUzOS00ZjI4LTk5NGYtZjZhYThiOTc1ZjhhOmYzNDUzOWI0MGNmMDRmZWE4MmY5MzMzMjZiNTA2YmE5"
    auth_token = requests.post(URL_AUTH, headers={"Authorization": key})
    authorization = "Bearer " + auth_token.text
    return authorization


headers_auth = auth()


def get_translate_info(word):

    params = {'text': word, 'srcLang': 1049, 'dstLang': 1033}
    response_word = requests.get(URL_TRANSLATE, params=params, headers={"Authorization": headers_auth})
    translated_word_info = response_word.json()
    return translated_word_info


def get_translated_word(word):

    translated_word = get_translate_info(word)["Translation"]["Translation"]
    return translated_word


def get_sound_translated_word(word):

    sound_name = get_translate_info(word)["Translation"]["SoundName"]
    dict = get_translate_info(word)["Translation"]["DictionaryName"]
    params = {'dictionaryName': dict, 'fileName': sound_name}
    response_sound = requests.get(URL_SOUND, params=params, headers={"Authorization": headers_auth})
    return response_sound.json()