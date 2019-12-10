with open('input.txt') as f:
    map_data = f.readlines()

map_data = [x.rstrip() for x in map_data]
test_data = '''G)H
B)C
C)D
D)E
E)F
D)I
E)J
B)G
J)K
K)L
COM)B'''.split('\n')


def checksum(orbital_map):
    out = []
    primary_order = [x.split(')')[0] for x in orbital_map]
    satellite_order = [x.split(')')[1] for x in orbital_map]
    c = 0
    for relationship in orbital_map:
        primary = relationship.split(')')[0]
        out.append([relationship])
        while primary != 'COM':
            index_map = satellite_order.index(primary)
            out[c].append(orbital_map[index_map])
            primary = primary_order[index_map] 

        c += 1

    return out

ans = checksum(map_data)
print(ans[0])

def recursive_len(item):
    if type(item) == list:
        return sum(recursive_len(subitem) for subitem in item)

    else:
        return 1


'''
for i, relationship[0] in enumerate(map_data):
    if relationship.split(')')[1] == 'SAN' or relationship.split(')')[1] == 'YOU':
        print(i)

print(set(map_data[611]) & set(map_data[861]))
'''