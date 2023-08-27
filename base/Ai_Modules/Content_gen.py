import wikipedia
from django.http import JsonResponse
import random
import nltk
from nltk.corpus import wordnet
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re

def get_answer_from_given_link(question_url):
    code = ''
    response = requests.get(question_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        question_title = soup.find('a', class_='question-hyperlink').get_text()
        code_blocks = soup.find_all('pre')
        for code_block in code_blocks:
            code = code + str(code_block)
    except:
        code = soup.get_text()
    return code

def get_stackoverflow_link(question, site='stackoverflow.com'):
    num_results = 30
    search_results = search(question, num_results=num_results)
    search_results = list(search_results)  # Convert generator to list
    for result in search_results:
        if site in result:
            return result
    return search_results[0] if search_results else None

def respond_to_input(user_input):
    question_words = ["what", "which", "where", "when", "how","who"]
    if user_input.lower().startswith(tuple(question_words)):
        tokens = nltk.word_tokenize(user_input.lower())
        pos_tags = nltk.pos_tag(tokens)
        verbs = [token for token, pos in pos_tags if pos.startswith('V')]
        if len(verbs) > 0:
            link = get_stackoverflow_link(user_input)
            code = get_answer_from_given_link(link)
            if code:
                return code
            else:
                wikipedia.set_lang("en")
                page = wikipedia.page(user_input)
                summary = page.summary
                return summary
    link = get_stackoverflow_link(user_input)
    code = get_answer_from_given_link(link)
    if code:
        return code
    else:
        wikipedia.set_lang("en")
        page = wikipedia.page(user_input)
        summary = page.summary
        
        return summary

# print(respond_to_input("python"))

# def chatbot_res(request):
#     if request.method == "GET":
#         message = request.GET.get("message")
#         response = respond_to_input(message)
#         return JsonResponse({"response": response})
#     else:
#         return JsonResponse({"error": "Invalid request method"})
