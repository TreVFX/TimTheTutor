import wikipedia

def get_info(query, language=None):
  query = wikipedia.search(query, results=1, suggestion=True)
  if language != None:
    wikipedia.set_lang(language)
  else:
    wikipedia.set_lang("en")
    
  try:
    Q = wikipedia.page(query[0][0])
    interm_answer = wikipedia.summary(Q, sentences=8)
    fav = Q.images
    return interm_answer, fav[0]
  except Exception:
    apology_cookie = "https://media.tenor.com/images/cb1e23e8e8ccc6934876368ada5a17ce/tenor.gif"
    return "As a new system I still have bugs. Your query sadly couldn't be answered by the current algorithm. Please accept this cookie as my way of saying sorry.", apology_cookie
