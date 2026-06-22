import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(text)

    organizations = []
    persons = []
    locations = []

    for ent in doc.ents:

        if ent.label_ == "ORG":
            organizations.append(ent.text)

        elif ent.label_ == "PERSON":
            persons.append(ent.text)

        elif ent.label_ in ["GPE", "LOC"]:
            locations.append(ent.text)

    return (
        ",".join(set(organizations)),
        ",".join(set(persons)),
        ",".join(set(locations))
    )