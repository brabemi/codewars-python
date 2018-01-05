from collections import Counter

BRC_MATCH = {'(': ')', '[': ']', '{': '}'}

def parse_molecule(formula):
    atoms = Counter()
    elem, qnt, brc = formula[0], '', ''
    if formula[0] in '([{':
        elem = ''
        brc = BRC_MATCH[formula[0]]

    for c in formula[1:]:
        if brc:
            if c == brc:
                brc = ''
                elem = parse_molecule(elem)
            else:
                elem += c
        elif 'A' <= c <= 'Z' or c in '([{':
            if isinstance(elem, Counter):
                atoms += Counter({key: val * (int(qnt) if qnt else 1) for key, val in elem.items()})
            else:
                atoms += Counter({elem: int(qnt) if qnt else 1})
            elem, qnt = c, ''
            if c in '([{':
                elem = ''
                brc = BRC_MATCH[c]
        elif 'a' <= c <= 'z':
            elem += c
        elif '0' <= c <= '9':
            qnt += c

    if isinstance(elem, Counter):
        atoms += Counter({key: val * (int(qnt) if qnt else 1) for key, val in elem.items()})
    else:
        atoms += Counter({elem: int(qnt) if qnt else 1})
    return atoms



def equals_atomically(obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True


print(equals_atomically(parse_molecule("(C5H5)Fe(CO)2CH3"),
                              {'H': 2, 'O': 1}), "Should parse water")
# print(equals_atomically(parse_molecule("H2O"),
                            #   {'H': 2, 'O': 1}), "Should parse water")
# print(equals_atomically(parse_molecule("Mg(OH)2"), {
            # 'Mg': 1, 'O': 2, 'H': 2}), "Should parse magnesium hydroxide: Mg(OH)2")
# print(equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {
            # 'K': 4,  'O': 14,  'N': 2,  'S': 4}), "Should parse Fremy's salt: K4[ON(SO3)2]2")
