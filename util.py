from superpowered import *
import os

os.environ["SUPERPOWERED_API_KEY_ID"] = ""
os.environ["SUPERPOWERED_API_KEY_SECRET"] = ""

# list kbs
kbs = list_knowledge_bases()

# print kbs line by line
def pretty_print_kbs(kbs):
    for kb in kbs:
        print(kb)

# delete all kbs
def delete_all_kbs(kbs):
    for kb in kbs:
        print(kb)
        id = kb.get('id')
        delete_knowledge_base(id)

#pretty_print_kbs(kbs)
delete_all_kbs(kbs)
