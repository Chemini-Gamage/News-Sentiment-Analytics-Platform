import re

STOPWORDS = {
    "the","a","an","and","or",
    "of","to","for","in","on",
    "at","with"
}

def extract_keywords(text):

    words = re.findall(r"\w+", text.lower())

    keywords = []

    for word in words:

        if len(word) > 3 and word not in STOPWORDS:
            keywords.append(word)

    return ",".join(keywords[:5])