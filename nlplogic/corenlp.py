from textblob import TextBlob
import wikipedia


def search_wikipedia(search_term):
    print(f"Searching Wikipedia for {search_term}")

    try:
        return wikipedia.summary(search_term)
    except(wikipedia.exceptions.DisambiguationError):
        return "No results found"


def summarize_wikipedia(search_term):
    print(f"Summarizing Wikipedia for {search_term}")

    try:
        return wikipedia.summary(search_term)
    except(wikipedia.exceptions.DisambiguationError):
        return "No results found"


def get_text_blob(text):
    return TextBlob(text)


def get_phrases(text):
    return get_text_blob(summarize_wikipedia(text)).noun_phrases
