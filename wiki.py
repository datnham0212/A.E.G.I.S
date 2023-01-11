import wikipedia as wiki

# def something_idk():
#     result = wiki.search('USA');
#     for each in result:
#         try:
#             print(wiki.page(each).summary);
#         except Exception:
#             pass

def read_wiki(query):
    try:
        result = wiki.search(query);
        for each in result:
            try:
                return wiki.page(each).summary
            except Exception:
                pass
    except Exception:
        return "Sorry, I couldn't find any information on that."


