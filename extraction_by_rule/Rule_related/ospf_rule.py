import re
import json
file = '../rfc/OSPF_annotation_9.txt'

state_list = ["Down","Loopback","Waiting","Point-to-point","DR Other","Backup","DR"]
transitions = []
transition_text = ""
pre_line = ""
first_line = True
start_sign = "State(s)"
with open(file, 'r') as fr:
    for line in fr:
        if first_line:
            pre_line = line
            first_line = False
            continue
        if start_sign in pre_line:
            if transition_text:
                transitions.append(transition_text)
            transition_text = ""
            transition_text += pre_line
            pre_line = line
        else:
            if line:
                transition_text += pre_line
                pre_line = line
            else:
                continue
    if transition_text:
        transitions.append(transition_text)

trans = []
data = []
for text in transitions:
    # print(text)
    obj1 = re.search(r'.* State\(s\): (.*?) .*', text)
    obj2 = re.search(r'.* Event: (.*?) .*', text)
    obj3 = re.search(r'.* New state: (.*?) .*', text)
    obj4 = re.search(r'.* Action: ([\s\S]*)', text)
    cur_state = ""
    event = ""
    new_state = ""
    action = ""
    if obj1:
        cur_state = obj1.group().split(":")[1].strip()
    if obj2:
        event = obj2.group().split(":")[1].strip()
    if obj3:
        new_state = obj3.group().split(":")[1].strip()
    if obj4:
        action = obj4.group().split(":")[1].strip()
    # print(cur_state, event, new_state)
    print('-'  * 100)
    tmp = action.split("\n")
    action = ""
    for it in tmp:
        action += it.strip() + " "
    # print(action)

    if cur_state == "Any State":
        for state in state_list:
            trans.append({
                "sentence" : action,
                "cur_state" : state,
                "event" : event,
                "new_state" : new_state
            })
    elif "Depends upon action routine" in new_state:
        if " or " in cur_state:
            trans.append({
                "sentence" : action,
                "cur_state" : cur_state,
                "event" : event,
                "new_state" : "Unknown"
            })
        else:
            new_states = []
            for s in state_list:
                if s in action:
                    new_states.append(s)
            for ns in new_states:
                trans.append({
                    "sentence" : action,
                    "cur_state" : cur_state,
                    "event" : event,
                    "new_state" : ns
                })
    else:
        trans.append({
            "sentence" : action,
            "cur_state" : cur_state,
            "event" : event,
            "new_state" : new_state
        })
    data.append({
        "text" : text,
        "transition" : trans
    })
    trans = []

with open("../../demo/data/ospf.json", 'w') as fp:
    json.dump(data, fp)
