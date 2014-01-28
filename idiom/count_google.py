# -*- coding: utf-8 -*-
import requests

class GoogleSearcher(object):
    """ google result counter """

    # -------------------------------------------------------------------------
    # constant
    # -------------------------------------------------------------------------
    search_url = 'http://ajax.googleapis.com/ajax/services/search/web'
    search_ver = '1.0'

    def __init__(self):
        super(GoogleSearcher, self).__init__()

    # -------------------------------------------------------------------------
    # core
    # -------------------------------------------------------------------------
    def search(self, query):
        """ Search a sentence / phrase by Google and get the number of results
            as well as a few matching examples. Since the result count is
            roughly estimated, it is not necessary accurate.

            Parameters
            ----------
            query : string
                The query sentence / phrase.

            Returns
            -------
            count : int
                The result count. It is negative if any exception occurs when
                parsing the search result, and non-negative otherwise.
            examples : list
                List of a few examples matching the query sentence / phrase.
        """
        count, examples = -1, []
        payload = {'v': self.search_ver, 'q': '"%s"' % query}
        r = requests.get(self.search_url, params=payload)
        try:
            r_json = r.json()
            data = r_json['responseData']
            count = data['cursor']['estimatedResultCount']
            examples = [item['content'] for item in data['results'] \
                        if query.lower() in item['content'].lower()]
        except:
            pass
        return count, examples

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    google_searcher = GoogleSearcher()
    count, examples = google_searcher.search('It should be noted that')
    print count
    for example in examples:
        print '----------------------------'
        print example