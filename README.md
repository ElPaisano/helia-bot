# HeliaBot

> HeliaBot is a hacky experiment, not a production-ready application :D

HeliaBot is a terminal-based chatbot application that answers users questions about IPFS Helia using the [data sources listed](#data-sources).

Under the hood, the bot uses the [Superpowered AI Python SDK](https://github.com/SuperpoweredAI/superpowered-python-sdk) with ChatGPT, which ensures that the bot will only use sources provided and will not make up wacky answers using unknown or outdated sources, which is what ChatGPT will do if left to it's own devices.

* [Data sources](#data-sources)
  + [Adding new data sources](#adding-new-data-sources)
* [How to use the bot](#how-to-use-the-bot)
  + [Prerequisites](#prerequisites)
  + [Setup](#setup)
  + [Chat with the bot](#chat-with-the-bot)
* [Utilities](#utilities)
  + [List all knowledge bases](#list-all-knowledge-bases)
  + [Delete all knowledge bases](#delete-all-knowledge-bases)

## Data sources

HeliaBot uses a subset of resources from the following information sources:

- [The Helia project wiki](https://github.com/ipfs/helia/wiki)
- [The Helia example apps repo](https://github.com/ipfs-examples/helia-examples/tree/main)

In addition, the bot draws on sources from the [IPFS docs](https://docs.ipfs.tech/):

- https://docs.ipfs.tech/concepts/what-is-ipfs/
- https://docs.ipfs.tech/concepts/ipfs-solves/
- https://docs.ipfs.tech/concepts/how-ipfs-works/
- https://docs.ipfs.tech/concepts/lifecycle/

All sources are defined in the lists in https://github.com/ElPaisano/helia-bot/blob/main/create_kb.py.

### Adding new data sources

This section is currently under construction. For the moment, please reach out directly to @ElPaisano for information on how to do this.

## How to use the bot

As described above, HeliaBot is currently an experiemental app. As such, setting it up and using it is a little hacky.

### Prerequisites

1. Python 3.10.9 or higher

1. The Superpowered AI Python SDK

    ```shell
    pip install superpowered-sdk
    ```
    
1. The OpenAI Python SDK

    ```shell
    pip install openai
    ```
    
1. An OpenAI account 

1. An OpenAI API key

1. A [Superpowered AI account](https://superpowered.ai/)

1. A Superpowered AI key and key secret (you can create this from your account dashboard)

1. A text editor 

1. A terminal application

### Setup

Once you've met the prerequisites, you must complete some intital set up to use the bot.

1. Clone this repository:

   ```shell
   git clone https://github.com/ElPaisano/helia-docs-bot.git
   ```
   
1. Navigate to the `helia-bot` repository:

   ```shell
   cd helia-bot
   ```
   
1. In your favorite text editor, open `create_kb.py`.

1. Enter your Superpowered API key and secret on the correct lines, which should now look something like:

   ```shell
   os.environ["SUPERPOWERED_API_KEY_ID"] = "fake-key-12ey31811kjhgjk03"
   os.environ["SUPERPOWERED_API_KEY_SECRET"] = "fake-secret-86483264289342893"
   ```
   
1. Close and save the file.

1. In a terminal, run `create_kb.py` to create the knowledge base that the bot will use to answer questions.

   ```shell
   python create_kb.py
   ```
   
   The script outputs a knowledge base ID in the terminal. **You will need this in next steps, so don't forget it.**
   
   ```shell
   Created knowledge base with id: fake-6b55-b396-1278hjcdwvyuw1278
   ```

1. In your favorite text editor, open `chat.py`.

1. On the correct lines, enter the following info:

   - Your Superpowered AI key and secret
   - Your OpenAI API key
   - The ID of the knowledge base you created

   Your `chat.py` should look something like:
   
   ```shell
   os.environ["OPENAI_API_KEY"] = "fake-z6HVRmnFAKENXzdptT3BlbkFJhp4"
   os.environ["SUPERPOWERED_API_KEY_ID"] = "fake1123256789"
   os.environ["SUPERPOWERED_API_KEY_SECRET"] = "alsofake-cewyb56789YYhbjdg"

   knowledge_base_id = "532fake259-109f-478a-aa63-fe3c0ab3d3ab"
   ```

1. Close and save the file.

Yay! You've completed the setup! Now, you can use the bot.

### Chat with the bot

Now that the set up is complete, fire up the bot and start asking questions. 

> A note on latency: Responses to questions may experience a latency of at least a few seconds and the terminal may hang briefly.

> To exit the application, type `exit` in the `USER` field and press the **ENTER** key.

1. Run the bot.

   ```shell
   python chat.py
   ```
   
   You should see something like:
   
   ```shell
   GREETINGS HUMAN, I WILL ANSWER YOUR QUESTIONS ABOUT Helia. BOOP.
   ...
   ENTER YOUR QUESTION BELOW.


   USER: 
   ```
1. In the `USER` field, type your question and press the **ENTER** key. 

   Here's an example question and response:

   ```shell
   GREETINGS HUMAN, I WILL ANSWER YOUR QUESTIONS ABOUT HELIA. BOOP.
   ...
   ENTER YOUR QUESTION BELOW.


   USER: Create a simple app using IPFS Helia, and explain it to me.

   CHATBOT: To create a simple app using IPFS Helia, you can follow the example provided in the sources. The example is called "101-basics.js" and it demonstrates the basic usage of Helia.

   First, you need to install all the dependencies listed in the "package.json" file using the command `npm install`.

   Then, in the "101-basics.js" file, you can see how to create a Helia node:

   import { createHelia } from 'helia'

   // create a Helia node
   const helia = await createHelia()

   This node allows you to add blocks and retrieve them.

   Next, you can use the `@helia/unixfs` module to add some data to the node:

   import { unixfs } from '@helia/unixfs'

   // create a filesystem on top of Helia, in this case it's UnixFS
   const fs = unixfs(helia)

   // we will use this TextEncoder to turn strings into Uint8Arrays
   const encoder = new TextEncoder()
   const bytes = encoder.encode('Hello World 101')

   // add the bytes to your node and receive a unique content identifier
   const cid = await fs.addBytes(bytes)

   console.log('Added file:', cid.toString())


   In this example, the code creates a UnixFS filesystem on top of the Helia node. It uses the `TextEncoder` to convert the string "Hello World 101" into a Uint8Array, and then adds the bytes to the node using the `addBytes` method. The method returns a unique content identifier (CID) for the added file.

   You can run this example to see how it works. Keep in mind that this is just a basic example, and you can explore more advanced features and use cases of Helia by referring to the documentation and examples provided in the sources.
   ```

## Utilities

The `util.py` file defines 2 utility functions, `pretty_print_kbs(kbs)` and `delete_all_kbs(kbs)`, for a given list `kbs` of Superpowered AI knowledge bases. The first function is useful for cataloging listing knowledge bases and their metadata (and for when you forget your IDs :D). The second function deletes all knowledge bases, which is useful if you goof and want to start over.

### List all knowledge bases

1. Open `util.py`
2. Uncomment `pretty_print_kbs(kbs)`
3. Make sure `delete_all_kbs(kbs)` is commented out
4. Run `util.py`
   ```shell
   python util.py
   ```

   Your knowledge bases display on the command line.

### Delete all knowledge bases

1. Open `util.py`
2. Uncomment `delete_all_kbs(kbs)`
3. Make sure `pretty_print_kbs(kbs)` is commented out
4. Run `util.py`
   ```shell
   python util.py
   ```

   Your knowledge bases display on the command line. The script hangs for a moment before deleting all listed knowledge bases.
