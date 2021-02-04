from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator

from couchbase.cluster import QueryOptions

from couchbase.exceptions import CouchbaseException
from couchbase.cluster import AnalyticsOptions

user = 'Administrator'
password = 'password'
host_url = 'couchbase://localhost'

def connect_couchbase(bucket_name):
    # get a reference to our cluster
    cluster = Cluster(host_url, ClusterOptions(PasswordAuthenticator(user, password)))

    # get a reference to our bucket
    cb = cluster.bucket('default')
    # get a reference to the default collection
    collection = cb.default_collection()
    return collection

def upsert_document(cb_coll, key, doc):
    print("\nUpsert CAS: ")
    try:
        result = cb_coll.upsert(key, doc)
        print(result.cas)
    except Exception as e:
        print(e)


def get_by_key(cb_coll, key):
    try:
        result = cb_coll.get(key)
        return result.content_as[str]
    except Exception as e:
        print(e)
