import re
import json
file = '../rfc/BGPv4_annotation_sp.txt'
events_file = '../rfc/def_events.txt'
id2events = {}
events2id = {}
with open(events_file, 'r') as fp:
    for line in fp:
        if "BGPv4" in line:
            list = line.split("	")
            id2events[list[2][:-1]] = list[1]
            events2id[list[1].upper()] = list[2][:-1]
    print(id2events)
    print(events2id)

blocks = []
trans = []

block_text = ""
trans_text = ""
pre_line = ""
cur_state = ""

first_line = True
start_tag = "State:"
start_tag2 = "   "
with open(file, 'r') as fr:
    for line in fr:
        if first_line:
            pre_line = line
            first_line = False
            continue
        if start_tag in pre_line and len(pre_line.split()) == 2:
            if block_text and cur_state and trans:
                blocks.append({
                    "text" : block_text,
                    "cur_state": cur_state,
                    "trans" : trans
                })
            cur_state = pre_line.split(start_tag)[0].strip()
            trans = []
            block_text = ""
            block_text += pre_line
            pre_line = line
        elif pre_line == '\n':
            if trans_text:
                trans.append(trans_text)
            trans_text = ""
            block_text += pre_line
            pre_line = line
        else:
            trans_text += pre_line.strip() + " "
            block_text += pre_line
            pre_line = line

    if block_text and cur_state and trans:
        blocks.append({
            "text" : block_text,
            "cur_state": cur_state,
            "trans" : trans
        })

transitions = []
data = []
event_tag = "Event"
change_tag = "changes its state to"
stay_tag = "stays in the"
remain_tag = "remains in the"
id = 0
oid = 0
for block in blocks:
    for tran in block["trans"]:
        # print("-" * 100)
        # print(f'{oid} : {tran}')
        if event_tag in tran and ( change_tag in tran or stay_tag in tran or remain_tag in tran):
            print("*" * 100)
            print(f'{id} : {tran}')
            id += 1
            print(block['cur_state'])

            event = ""
            eids = []
            result = re.findall(r'(Event \d+)', tran)
            if not result:
                result = re.findall(r'\((Events.*?)\)',tran)
                events = result[0][6:].split(",")

                for eid in events:
                    if "-" in eid:
                        start_id = int(eid.split('-')[0])
                        end_id = int(eid.split('-')[1])
                        for id in range(start_id, end_id+1):
                            eids.append(id)
                    else:
                        eids.append(int(eid))
                for eid in eids:
                    event += id2events[str(eid)] + '\n'
            else:
                for res in result:
                    eid = res.split()[1]
                    event += id2events[eid] + '\n'

            event = event[:-1]
            print(event)
            if result:
                for res in result:
                    print(res)


            new_state = ""
            if change_tag in tran:
                new_state = tran.split(change_tag)[1].strip()
            elif stay_tag in tran:
                new_state = tran.split(stay_tag)[1].strip()
            else:
                new_state = tran.split(remain_tag)[1].strip()
            if new_state:
                new_state = new_state.split()[0]
                if new_state.endswith("."):
                    new_state = new_state[:-1]
                print(new_state)


            transitions.append({
                "text" : tran,
                "cur_state" : block['cur_state'],
                "event" : event,
                "new_state" : new_state,
            })
    block["transition"] = transitions
    block.pop("trans")
    # data.append({
    #     "text" : block["text"],
    #     "transition" : transitions
    # })
    transitions = []


with open("../../demo/data/bgpv4.json", 'w') as fp:
    json.dump(blocks, fp)