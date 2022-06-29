import json

files = ['bgpv4', 'isis', 'ospf']

paths = ['../../demo/data/{}.json'.format(file) for file in files]

trans_num = 0
for path in paths:
    with open(path, 'r') as fp:
        data = json.load(fp)
        for block in data:
            trans_num += len(block['transition'])
    print('{} : {}'.format(path.split('/')[-1].split(',')[0],trans_num))
    trans_num = 0