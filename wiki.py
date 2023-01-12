import wikipedia as wiki

def read_from_wiki(query):
    try:
        result = wiki.search(query);
        for each in result:
            try:
                return wiki.page(each).summary
            except Exception:
                pass
    except Exception:
        return "Sorry, I couldn't find any information on that."


