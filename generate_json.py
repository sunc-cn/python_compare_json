#!/usr/bin/python

#encoding=utf-8


import json

dest_dict = {"xx":2}
dict1 = {"uu":"uu"}
dict2 = {"double_key":1.2}
dict1["third"] = dict2
dest_dict["second"] = dict1

print(json.dumps(dest_dict))


