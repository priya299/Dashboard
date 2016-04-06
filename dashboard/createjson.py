"""
Author: Priya V

"""

import json
import jwzthreading_r as th
import sys
import perceval.backends as backend

msg_ids = []
msg_json = []
def create_json(mbox_files, output_file):
    """
    This function uses perceval to parse the mailing list archieve
    and gets the message ids. Then threading algorithm is run over
    the mbox files to group messages belonging to same thread and
    it is written to 'new.json' file.

    :param perceval_out : perceval output containing message ids
    :param mbox_files : mbox file of xen-devel list
    :param output_file : new.json file containing messages belonging to same thread

    """
    mbox_parser = backend.mbox.MBox(
	origin="http://lists.xenproject.org/archives/html/mbox/"+mbox_files,
	dirpath='.'
    )
    perceval_out = mbox_parser.fetch()
    for item in perceval_out:
        msg_json.append(item)

    messages = th.message_details(mbox_files)
    with open(output_file,'a') as f:
        for key, value in messages.items():
            for k in msg_json:
                if key == k['Message-ID'].strip('<>'):
                    k['property'] = key
                    json.dump(k, f, ensure_ascii=True, indent=4)

            if value:
                for i in value:
                    for j in msg_json:
                        if i == j['Message-ID'].strip('<>'):
                            j['property'] = key
                            json.dump(j, f, ensure_ascii=True, indent=4)
                            break
        f.close()

if __name__ == "__main__":
    create_json(sys.argv[1],sys.argv[2])
    print("new.json file has been created")