from langchain_community.tools.tavily_search import TavilySearchResults

def search_linkedin_profile_url(name: str):
    search = TavilySearchResults()
    res = search.run(name)
    print('&&&&&&&&&', name, res)
    return res

