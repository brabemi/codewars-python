def add_helper(char_set, key, val):
    if key not in char_set.keys():
        char_set[key] = set()
    char_set[key].add(val)


def recoverSecret(triplets):
    fwd = {}
    bwd = {}
    retval = []
    for triplet in triplets:
        add_helper(fwd, triplet[0], triplet[1])
        add_helper(fwd, triplet[1], triplet[2])
        add_helper(bwd, triplet[1], triplet[0])
        add_helper(bwd, triplet[2], triplet[1])
    fwd_keys = set(fwd.keys())
    first = (fwd_keys - set(bwd.keys())).pop()
    retval.append(first)
    while first in fwd_keys:
        tmp_first = None
        for e in fwd[first]:
            bwd[e].remove(first)
            if len(bwd[e]) == 0:
                tmp_first = e
        first = tmp_first
        retval.append(first)

    return ''.join(retval)

secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets), secret)
