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


def generate_system(orbital_map):
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


def checksum(item):
    if type(item) == list:
        return sum(checksum(subitem) for subitem in item)

    else:
        return 1


system = generate_system(map_data)
print(checksum(system))


# planet YOU/SAN's can be found be searching for the planet in the list of lists
for i, path in enumerate(system):
    first_element = path[0].split(')')[1]
    if 'YOU' in first_element:
        YOU = i

    elif 'SAN' in first_element:
        SAN = i

# len(YOU) + len(SAN) - 2*LCA - 2
#  LCA = lost common ancestor 
print(len(system[YOU])+len(system[SAN])-2*len(set(system[YOU]) & set(system[SAN]))-2)
