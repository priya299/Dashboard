#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Bitergia
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Priya V <vppriya9@gmail.com>
#

import sys
import json
import argparse
import logging

import jwzthreading_r as th
import perceval.backends as backend


msg_ids = []
msg_json = []


class MboxParser:

    def getmbox(self, mbox_files):
        mbox_parser = backend.mbox.MBox(
                origin = mbox_files,
                dirpath='.'
        )
        return mbox_parser.fetch()

    def create_json(self, mbox_files, output_file, file=False):
        """

        This function uses perceval to parse the mailing list archieve
        and gets the message ids. Then threading algorithm is run over
        the mbox files to group messages belonging to same thread and
        it is written to the output file.

        :param mbox_files: mbox file of xen-devel list
        :param output_file: output file name
        """
        percevalout = self.getmbox(mbox_files)
        message_id = ''
        for item in percevalout:
            message_id = item['data']['Message-ID']
            if message_id not in msg_ids:
                msg_ids.append(message_id)
                msg_json.append(item)

        messages = th.message_details(mbox_files, file)
        with open(output_file,'a') as f:
            for key, value in messages.items():
                for k in msg_json:
                    try:
                        if key == k['data']['Message-ID'].strip('<>'):
                            k['property'] = key
                            json.dump(k, f, ensure_ascii=True, indent=4)
                            break
                    except KeyError:
                            logging.debug('Received an email without the correct Message Id %s', str(k))

                if value:
                    for i in value:
                        for j in msg_json:
                            try:
                                if i == j['data']['Message-ID'].strip('<>'):
                                    j['property'] = key
                                    json.dump(j, f, ensure_ascii=True, indent=4)
                                    break
                            except KeyError as e:
                                logging.debug('Received an email without the correct Message Id')

            f.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mbox",required=True,help="Give the name of the mbox file to be parsed")
    parser.add_argument("--output", required=True, help="Name of the output json file")
    args = parser.parse_args()
    logging.basicConfig(filename='perceval_mbox_parse.log', level=logging.DEBUG)
    mparser = MboxParser()
    mparser.create_json(args.mbox,args.output)
    print("Output file %s created"%args.output)

if __name__ == "__main__":
    main()


