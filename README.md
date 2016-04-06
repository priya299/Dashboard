# Dashboard
Write a script to use the Perceval email backend to feed data from the xen-devel mailing list to an ElasticSearch database, and annotating in it messages in the same thread. For identifying threads, you can use the Zawinski algorithm
The result of the script would be an ElasticSearch search index, with one JSON document per message (it could be the same document produced by Perceval), with one extra field (property), with the same value for messages in in the same thread. The value could be the message-id of the first message in the thread.

Instructions
============

    git clone https://github.com/priya299/Dashboard.git
    
    cd Dashboard
    
    python createjson.py 'Perceval Ouputfile' 'mbox file' 'output_file'

eg: python createjson out.json xen-devel-2016-03 new.json

"new.json" json file will be created with each message belong to a single thread having an additional attribute "property". The property attribute will have message id of the first message in the thread.
