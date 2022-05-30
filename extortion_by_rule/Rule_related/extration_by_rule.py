import re
import json

with open('./chapter8.json', 'r') as fp:
    raw = json.load(fp)

pattern = []
pattern.append(re.compile(r'([Ww]hen .*?\.)'))
# pattern.append(re.compile(r'.*([Ww]hen .*?\.)'))
pattern.append(re.compile(r'([Ii]f .*?\.)'))
# pattern.append(re.compile(r'.*([Ii]f .*?\.)'))

extract_pattern = []
extract_pattern.append(re.compile(r'([Ww]hen.*?), the IS shall.*?adjacencyState.*?to .(.*?).,'))
extract_pattern.append(re.compile(r'([Ii]f.*?) then the IS shall.*?adjacencyState.*?to .(.*?).,'))
extract_pattern.append(re.compile(r'([Ii]f.*?), the IS shall.*?adjacencyState.*?to .(.*).,'))

extract_pattern.append(re.compile(r'([Ww]hen.*?), the IS shall.*?(adjacencyStateChange \(.*?\)).*'))
extract_pattern.append(re.compile(r'([Ii]f\s.*?), the IS shall.*?(adjacencyStateChange \(.*?\)).*'))

dic = {0:['when','When'],1:['if','If']}
def clean(pid, sentence):
    pid = 1 if pid > 1 else pid
    keys = dic[pid]
    max_pos = 0
    for key in keys:
        pos = sentence.rfind(key + ' ')
        if max_pos < pos:
            max_pos = pos
    return sentence[max_pos:]

if_when_sentence = []
for i, item in enumerate(raw):
    text = item['text']
    title = item['title']

    print(f'----------{i}----------')
    print(title)

    candidates = []
    for p in pattern:
        res = re.findall(p, text.replace('\n', ' ').replace('i.','i)'))
        if res:
            candidates.extend(res)

    # if_when_sentence.extend(candidates)
    extractions = []
    idx = 0
    for sentence in candidates:
        # print(sentence)
        conditions = []
        states = []
        for pid, p in enumerate(extract_pattern):
            res = re.search(p, sentence)
            if res:
                print('*'*50)
                print(f'text: {sentence}')
                print(f'condition: {clean(pid,res.group(1))}')
                print(f'state: {res.group(2)}')
                conditions.append(clean(pid,res.group(1)))
                states.append(res.group(2))
        if conditions and states:
            extractions.append({
                'id':idx,
                'text':sentence,
                'present_state':['unknown' for i in range(len(states))],
                'condition':conditions,
                'new_state':states
            })
            idx += 1
    raw[i]['extraction'] = extractions
print("ok")
with open('./data.json', 'w') as fp:
    json.dump(raw,fp)
