"""
Author: Priya V

The following code parses the json file 'out.json',
which is a perceval output to get the message ids.
Then I have run the threading algorithm over the
mbox files to group messages belonging to same thread
and it is written to 'new.json' file.

"""

import json
import jwzthreading_r as th
import sys

msg_ids = []
msg_json = []
def create_json(perceval_out, mbox_files):
    """
    This function parses the perceval output, which
    is a json file 'out.json' to get the message ids.
    Then threading algorithm is run over the mbox files
    to group messages belonging to same thread
    and it is written to 'new.json' file.

    :param perceval_out: perceval output, which is a json file.
    :param mbox_files : mbox file of xen-devel list
    """
    with open(perceval_out) as f:
        for line in f:
            while True:
                try:
                    jfile = json.loads(line)
                    break
                except ValueError:
                    line += next(f)
            if jfile['Message-ID'] not in msg_ids:
                msg_ids.append(jfile['Message-ID'].strip('<>'))
                msg_json.append(jfile)

    messages = th.message_details(mbox_files)
    with open('new.json','a') as f:
        for key, value in messages.iteritems():
            for k in msg_json:
                if key == k['Message-ID'].strip('<>'):
                    k['property'] = key
                    json.dump(k, f, ensure_ascii=True, indent=4)

            if value:
                for i in value:
                    for j in msg_json:
                        if i == j['Message-ID'].strip('<>'):
                            j['property'] = i
                            json.dump(j, f, ensure_ascii=True, indent=4)
                            break
        f.close()

if __name__ == "__main__":
    create_json(sys.argv[1],sys.argv[2])
    print "'new.json' file has been created"