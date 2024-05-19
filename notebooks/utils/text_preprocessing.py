import re

def cleanText(text):
    # Lower casing
    text = text.lower()

    # Filtering
    text = re.sub(r"http\S+", "", text)
    text = " ".join(filter(lambda x: x[0] != "@", text.split()))
    text = " ".join(re.sub("[^a-zA-Z]+", " ", text).split())

    # Tokenization
    text = text.split()

    # TODO: Slang and abbreviation
    text = text

    # TODO: Stemming
    text = text

    return text

def filterWordLengthTextDataFrame(df, text_column, min_length=3):
    return df[df[text_column].apply(lambda x: len(x) >= min_length)]


def preprocessTextDataFrame(df, text_column):
    df[text_column] = df[text_column].apply(cleanText)
    return df