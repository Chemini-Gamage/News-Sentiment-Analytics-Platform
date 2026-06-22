import re

STOPWORDS = {
    "the","a","an","and","or","of","to","for","in","on","at","with",
    "live","updates","breaking","news","today"
}

def extract_keywords(text):

    words = re.findall(r"[a-zA-Z]+", text.lower())

    cleaned = []

    for w in words:

        if len(w) > 3 and w not in STOPWORDS:
            cleaned.append(w)

    # remove duplicates but preserve order
    seen = set()
    final = []

    for w in cleaned:
        if w not in seen:
            final.append(w)
            seen.add(w)

    return ",".join(final[:5])