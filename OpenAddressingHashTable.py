from HashTable import HashTable


# OpenAddressingBucket represents a bucket with a key and a value
class OpenAddressingBucket:
    def __init__(self, bucket_key=None, bucket_value=None):
        self.key = bucket_key
        self.value = bucket_value

    def isEmpty(self):
        if self is OpenAddressingBucket.EMPTY_SINCE_START:
            return True
        return self is OpenAddressingBucket.EMPTY_AFTER_REMOVAL


# Initialize two special bucket types: empty-since-start and empty-after-removal
OpenAddressingBucket.EMPTY_SINCE_START = OpenAddressingBucket()
OpenAddressingBucket.EMPTY_AFTER_REMOVAL = OpenAddressingBucket()


# OpenAddressingHashTable is a base class for an open addressing hash table
class OpenAddressingHashTable(HashTable):
    def __init__(self, initialCapacity):
        self.table = [OpenAddressingBucket.EMPTY_SINCE_START] * initialCapacity

    def probe(self, key, i):
        # Each derived class must implement
        pass

    # Inserts the specified key/value pair. If the key already exists, the
    # corresponding value is updated. If inserted or updated, True is returned.
    # If not inserted, then False is returned.
    def insert(self, key, value):

        # add your code here

        return False  # no empty bucket found

    # Searches for the specified key. If found, the key/value pair is removed
    # from the hash table and True is returned. If not found, False is returned.
    def remove(self, key):

        # add your code here
        return False  # key not found

    # Searches for the key, returning the corresponding value if found, null if
    # not found.
    def search(self, key):

        # add your code here

        return None  # key not found

    def __str__(self):
        result = ""
        for i in range(len(self.table)):
            result += "%d: " % i
            if self.table[i] is OpenAddressingBucket.EMPTY_SINCE_START:
                result += "EMPTY_SINCE_START\n"
            elif self.table[i] is OpenAddressingBucket.EMPTY_AFTER_REMOVAL:
                result += "EMPTY_AFTER_REMOVAL\n"
            else:
                result += "%s, %s\n" % (self.table[i].key, self.table[i].value)
        return result