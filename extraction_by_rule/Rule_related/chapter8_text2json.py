import json
import re

data = []
with open('./raw_text/chapter8.txt', 'r') as f:
    lines = f.readlines()
    title = ""
    text = ""
    tmp = None
    id = 0
    for line in lines:
        if line.startswith('8'):
            data.append({
                'id': id,
                'title': title,
                'text': text
            })
            id += 1
            title = line[:9] if re.match('\d.\d.\d.\d.\d', line) else line
            text = line[9:].replace('\n' ,' ') if re.match('\d.\d.\d.\d.\d', line) else ""
        else:
            if line == '\n':
                continue
            # text += line.strip()
            text += line

with open('./Rule_related/chapter8.json', 'w') as fp:
    json.dump(data[1:],fp)

# with open('./chapter8.json', 'r') as fp:
#     data = json.load(fp)
#     for i in range(5):
#         print(data[i]['id'])
#         print(data[i]['title'])
#         print(data[i]['text'])