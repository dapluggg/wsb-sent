import re
import emoji
import pandas as pd
import pprint

def clean_text(text_series):
    cleaned_text = []
    for item in text_series:
        print(item)
        # Remove Capitalization
        item = item.lower()
        # Remove mentions
        item = re.sub('@[^\s]+', '', item)
        # Remove URLs
        item = re.sub(r"http\S+", '', item)
        # Remove Whitespace
        item = re.sub(r'\s+', '', item)
        # Remove Emojis, replace with text
        item = emoji.demojize(item, delimiters=(' ', ' '))
        # Append itme to cleaned text
        cleaned_text.append(item)
        return cleaned_text

def fancy_print(text):
    pprint.pprint(text)
    return True