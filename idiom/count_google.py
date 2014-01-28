# -*- coding: utf-8 -*-
import requests

class GoogleCounter(object):
    """ google result counter """

    # -------------------------------------------------------------------------
    # constant
    # -------------------------------------------------------------------------
    search_url = 'http://ajax.googleapis.com/ajax/services/search/web'
    search_ver = '1.0'

    def __init__(self):
        super(GoogleCounter, self).__init__()

    # -------------------------------------------------------------------------
    # core
    # -------------------------------------------------------------------------
    def count(self, query):
        """ Get the number of results from Google when searching a query
            sentence. The result count is roughly estimated. Thus it is not
            necessary accurate.

            Parameters
            ----------
            query : string
                The query sentence.

            Returns
            -------
            result count : int
                If everything goes well, return the result count; Otherwise,
                return -1.
        """
        count = -1
        payload = {'v': self.search_ver, 'q': '"%s"' % query}
        r = requests.get(self.search_url, params=payload)
        try:
            r_json = r.json()
            count = r_json['responseData']['cursor']['estimatedResultCount']
        except:
            pass
        return count

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    google_counter = GoogleCounter()
    count = google_counter.count('on my way home')
    print count