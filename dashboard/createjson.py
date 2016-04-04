import json
import jwzthreading_r as th

msg_ids = []
msg_json = []
with open("out.json") as f: 
    for line in f:
        while True:
            try:
                jfile = json.loads(line)
                break
            except ValueError: # Not yet a complete JSON value
                line += next(f)
        if jfile['Message-ID'] not in msg_ids:
            msg_ids.append(jfile['Message-ID'].strip('<>'))
            msg_json.append(jfile)

messages = th.message_details('advisory-board-2014-02')
with open('new.json','a') as f:
    for key, value in messages.iteritems():
        for k in msg_json:
            if key == k['Message-ID'].strip('<>'):
                json.dump(k, f, ensure_ascii=True, indent=4)
        if value:
            for i in value:
                for j in msg_json:
                    if i == j['Message-ID'].strip('<>'):
                        j['property'] = i
                        json.dump(j, f, ensure_ascii=True, indent=4)
                        break
    f.close()
