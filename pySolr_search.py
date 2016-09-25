# If on Python 2.X
from __future__ import print_function
import sys
sys.path.append('/Users/ankitverma/Documents/IR_project/pysolr-3.4.0')
import pysolr

# Setup a Solr instance. The timeout is optional.
solr = pysolr.Solr('http://localhost:8983/solr/#/gettingstarted/', timeout=10)
#http://localhost:8983/solr/#/gettingstarted
#http://localhost:8983/solr/
# How you'd index data.
solr.add([
    {
        "id": "doc_1",
        "title": "A test document",
    },
    {
        "id": "doc_2",
        "title": "The Banana: Tasty or Dangerous?",
    },
])

# Later, searching is easy. In the simple case, just a plain Lucene-style
# query is fine.
results = solr.search('bananas')

# The ``Results`` object stores total results found, by default the top
# ten most relevant results and any additional data like
# facets/highlighting/spelling/etc.
print("Saw {0} result(s).".format(len(results)))

# Just loop over it to access the results.
for result in results:
    print("The title is '{0}'.".format(result['title']))

# For a more advanced query, say involving highlighting, you can pass
# additional options to Solr.
results = solr.search('bananas', **{
    'hl': 'true',
    'hl.fragsize': 10,
})

# You can also perform More Like This searches, if your Solr is configured
# correctly.
similar = solr.more_like_this(q='id:doc_2', mltfl='text')

# Finally, you can delete either individual documents...
solr.delete(id='doc_1')

# ...or all documents.
solr.delete(q='*:*')