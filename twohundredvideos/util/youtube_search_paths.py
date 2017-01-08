"""
            Youtube-standard paths for parsing search pages.
            Add more if you want to search beyond results page 10 (200 results)
"""

BASE_SEARCH_PATH = 'https://www.youtube.com/results?'

def get_search_strings(query):
    pages_to_search = ['{0}sp=SADqAwA%253D&q={1}'.format(BASE_SEARCH_PATH, query),
             '{0}sp=SBTqAwA%253D&q={1}'.format(BASE_SEARCH_PATH, query),
             '{0}sp=SCjqAwA%253D&q={1}'.format(BASE_SEARCH_PATH, query),
             '{0}q={1}&sp=SDzqAwA%253D'.format(BASE_SEARCH_PATH, query),
             '{0}sp=SFDqAwA%253D&q={1}'.format(BASE_SEARCH_PATH, query),
             '{0}q={1}&sp=SGTqAwA%253D'.format(BASE_SEARCH_PATH, query),
             '{0}sp=SHjqAwA%253D&q={1}'.format(BASE_SEARCH_PATH, query),
             '{0}sp=SIwB6gMA&q={1}'.format(BASE_SEARCH_PATH, query),
             '{0}q={1}&sp=SKAB6gMA'.format(BASE_SEARCH_PATH, query),
             '{0}q={1}&sp=SLQB6gMA'.format(BASE_SEARCH_PATH, query)
    ]
    #add more here !
    return pages_to_search
