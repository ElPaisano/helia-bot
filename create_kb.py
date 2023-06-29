from superpowered import *
import os

os.environ["SUPERPOWERED_API_KEY_ID"] = ""
os.environ["SUPERPOWERED_API_KEY_SECRET"] = ""

ipfs_overview_urls = [
    "https://docs.ipfs.tech/concepts/what-is-ipfs/",
    "https://docs.ipfs.tech/concepts/ipfs-solves/",
    "https://docs.ipfs.tech/concepts/how-ipfs-works/",
    "https://docs.ipfs.tech/concepts/lifecycle/",
]

helia_overview_md = [
    './resources/Branding.md',
    './resources/FAQ.md',
    './resources/Manifesto.md',
    './resources/Meta.md',
]

helia_dev_urls = [
    "https://raw.githubusercontent.com/ipfs-examples/helia-examples/main/examples/helia-101/README.md",
    "https://raw.githubusercontent.com/ipfs-examples/helia-examples/main/examples/helia-101/101-basics.js",
    "https://raw.githubusercontent.com/ipfs-examples/helia-examples/main/examples/helia-101/201-storage.js",
    "https://raw.githubusercontent.com/ipfs-examples/helia-examples/main/examples/helia-101/301-networking.js",
    "https://github.com/ipfs/helia/wiki/Migrating-from-js-IPFS",
]

def init_kb(title):
    kb = create_knowledge_base(title=title)
    kb_id = kb["id"]
    print(f"Created knowledge base with id: {kb_id}")
    return kb_id

def kb_add_urls(kb_id, urls):
    for url in urls:
        create_document_via_url(
            knowledge_base_id=kb_id,
            url=url,
            title=None,                                  
            description=None,  
            supp_id=None                      
        )

def kb_add_files(kb_id, files):
    for f in files:
        create_document_via_file(
            knowledge_base_id=kb_id,
            file_path=f,
            description=None,                            
            supp_id=None                                  
        )

kb_id = init_kb("Helia")
kb_add_urls(kb_id, ipfs_overview_urls)
kb_add_files(kb_id, helia_overview_md)
kb_add_urls(kb_id, helia_dev_urls)
print(list_knowledge_bases())
