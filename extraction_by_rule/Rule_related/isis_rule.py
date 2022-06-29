import json

file = './data.json'

blocks = []
transition = []
text = ""
states = set()
with open(file, 'r') as fp:
    data = json.load(fp)
    for block in data:
        if block["extraction"]:
            text = block["title"] + '\n' + block["text"]
            for trans in block["extraction"]:

                cur_state = trans['present_state'][0]
                event = trans['condition'][0]
                new_state = trans['new_state'][0]
                sentence = trans['text']

                states.add(cur_state)
                states.add(new_state)
                transition.append({
                    "sentence" : sentence,
                    "cur_state" : cur_state,
                    "event" : event,
                    "new_state" : new_state
                })

            blocks.append({
                "text" : text,
                "transition" : transition
            })
            transition = []

for state in states:
    print(state)
with open('../../demo/data/isis.json', 'w') as fp:
    json.dump(blocks, fp)