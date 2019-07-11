

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.storage = capacity * [None]
        self.size = capacity




# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, table_max=1):
    djb2 = 5381
    for i in string:
        i = ord(i)
        djb2 = djb2 * (2 ** 5) + djb2 + i
    key = djb2 % table_max
    return key


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    pair = Pair(key, value)
    hashkey = hash(key, hash_table.size)
    if hash_table.storage[hashkey] is not None:
        print("Warning, data loss!")

    hash_table.storage[hashkey] = pair
    return


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hashkey = hash(key, hash_table.size)

    if hash_table.storage[hashkey] == None:
        print("Futile action!")

    hash_table.storage[hashkey] = None
    return




# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    hashkey = hash(key, hash_table.size)

    loc = hash_table.storage[hashkey]
    if loc is not None:
        return loc.value
    else:
        return None



def Testing():
    ht = BasicHashTable(16)

    hash("line!")

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")

Testing()
    