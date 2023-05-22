import xmltodict

with open('1.osm', 'r', encoding='utf-8') as f:
    dct = xmltodict.parse(f.read())

k = 0
hotels = []
for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if tag['@k'] == "name":
                    name = tag['@v']
                if tag['@k'] == 'tourism' and tag['@v'] == 'hotel':
                    k+=1
                    hotels.append(name)
                elif 'tag' in node and isinstance(node['tag'], dict):
                    if node['tag']['@k'] == 'hotel':
                        k+=1
                        hotels.append(name)

print(k, sorted(hotels))