import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(text)

    orgs = []
    persons = []
    locations = []

    for ent in doc.ents:

        if ent.label_ == "ORG":
            orgs.append(ent.text)

        elif ent.label_ == "PERSON":
            persons.append(ent.text)

        elif ent.label_ in ["GPE", "LOC"]:
            locations.append(ent.text)

    # fallback: if empty, use simple heuristics
    if not orgs and "news" in text.lower():
        orgs.append("News Media")

    return (
        ",".join(set(orgs)),
        ",".join(set(persons)),
        ",".join(set(locations))
    )