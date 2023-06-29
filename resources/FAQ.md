> Please open an issue if you'd like something addressed here

### What is the relationship of Helia to js-IPFS?

[IPFS] is a suite of specifications and tools that concern data addressing and transfer. Historically it's also been the name of two applications that implement those protocols in Go ([Kubo]) and JavaScript ([js-IPFS]).

With [Filecoin] development, [Protocol Labs] found that progress towards the goal of "one protocol multiple implementations" was smoother when implementations did not contain the word "Filecoin" as by including that term, people consciously or unconsciously assume that one project is somehow "blessed", favoured or otherwise more important than another.

So in [late 2021](https://github.com/ipfs/ipfs/issues/470) a plan was enacted to remove the word "IPFS" from go-IPFS and js-IPFS and free up the space for multiple alternative implementations, which would be free to innovate on their own terms and perhaps specialize for certain tasks or environments.

go-ipfs was renamed [Kubo] and carried on as usual, but for js-IPFS we wanted to take the opportunity to have another look at what an implementation of IPFS in JS could look like and to apply learnings from the previous years of development.

The result of this is Helia - a new implementation of IPFS in JavaScript that is designed to be more modular and lightweight than js-IPFS which focusses on the most important use cases of IPFS in JavaScript.

It shares some internal components with js-IPFS - [libp2p], [bitswap] etc but has a [redesigned API](https://ipfs.github.io/helia/interfaces/_helia_interface.Helia.html) that will enable the next generation of distributed applications.

[js-IPFS is being retired in favour of Helia](https://github.com/ipfs/js-ipfs/issues/4336).  Read more about the [thought processes](./MANIFESTO.md) that informed Helia's design, check out the [examples](https://github.com/ipfs-examples/helia-examples) and start porting your application today!

### How does Helia guarantee compatibility with Kubo and other IPFS implementations?

Each Helia component has an interop suite that tests compatibility with other IPFS implementations.  These tests run during CI as part of each PR and before a release.

Initially they test compatibility with Kubo, but if you maintain another IPFS implementation, please open an issue or a PR to get added to the test matrix.

See:

* [helia interop](./packages/interop)
* [@helia/ipns interop](https://github.com/ipfs/helia-ipns/tree/main/packages/interop)
* [@helia/unixfs interop](https://github.com/ipfs/helia-unixfs/tree/main/packages/interop)

Other modules should implement an interop suite which can be linked to from here.

Note that Helia does not rely on https://github.com/ipfs/interop.  That repo is relied upon by Kubo for its interoperability with other implementations.

### How does it perform compared to other implementations including js-IPFS?

For the areas that have been benchmarked, very favourably.

There is a [benchmarking suite](./benchmarks) in this repository which will be extended to cover most functional areas such as [data transfer](https://github.com/ipfs/helia/issues/88).

#### Garbage collection

Helia uses reference counting for garbage collection.  This has proven to be much more scalable than the approaches taken by js-IPFS or Kubo.

* [#36](https://github.com/ipfs/helia/pull/36#issuecomment-1441403221) contains for graphs and discussion of the results.
* The Pinning & Garbage Collection section of this talk on [Helia performance at the 2023 IPFS Althing](https://youtu.be/zPeLYosZ3Ak?t=616) has a similar treatment

### Why consider using Helia over js-IPFS?

Helia is a fresh look at what a fully-featured IPFS implementation written in JavaScript could look like.

From it's inception js-IPFS was intended to be an API-compatible clone of what was go-IPFS and has since been renamed Kubo.  Over time this began to make less sense as more and more features were added to Kubo, js-IPFS struggled to keep pace and even then not all of the added features made sense in a JS context.

Although compatible on the wire with Kubo and other interfaces, Helia is not constrained by the Kubo API and is free to innovate in ways that empower JS use cases.  For example there's no need to follow the kitchen-sink approach of the Kubo/js-IPFS, instead users can keep their applications lightweight but just pulling in the features they use.

js-IPFS is [deprecated](https://github.com/ipfs/js-ipfs/issues/4336) and will receive no further updates outside of emergency security fixes.

### Why use Helia over the kubo-rpc-client?

Helia and the kubo-rpc-client are fundamentally different beasts.

When running the kubo-rpc-client you also must run an accompanying Kubo daemon which means managing a separate go runtime which is opaque to familiar JS monitoring and inspection tools and you must also protect an HTTP RPC API with very little in the way of built in security.

Running Helia allows you to embed an IPFS node into your application giving you the lowest latency and best possible performance.  For server applications this reduces the amount of moving parts and deployment tasks and for browser applications it's the only way to run a full IPFS node for every user.

It also means the user can use their JS expertise to tune and monitor their node using the same skillset and tools they'd use to inspect their application.

### What mechanisms does Helia have for content and peer routing?

Helia supports all of the existing libp2p content and peer routing mechanisms.

These include but are not limited to:

* [@libp2p/kad-dht](https://github.com/libp2p/js-libp2p-kad-dht)
* [@libp2p/ipni-content-routing](https://github.com/libp2p/js-ipni-content-routing)
* [@libp2p/reframe-content-routing](https://github.com/libp2p/js-reframe-content-routing)

### What data transports does Helia have?

Helia supports all of the existing [libp2p transports](https://libp2p.io/implementations/#transports).

These include but are not limited to:

* [@libp2p/webtransport](https://github.com/libp2p/js-libp2p-webtransport)
* [@libp2p/webrtc](https://github.com/libp2p/js-libp2p-webrtc)
* [@libp2p/websockets](https://github.com/libp2p/js-libp2p-websockets)
* [@libp2p/tcp](https://github.com/libp2p/js-libp2p-tcp)

### How does Helia "identify" itself?
Unless manually specified in the `libp2p` instance, Helia will use the following string to identify itself during `Indetify`:

`helia/x.x.x libp2p/x.x.x UserAgent=$USER_AGENT`

where $USER_AGENT is either the current node.js version (e.g., `v18.16.0`) or the browser's user agent string (e.g., `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36`).

See [`addHeliaToAgentVersion`](https://github.com/ipfs/helia/blob/ed4985677b62021f76541354ad06b70bd53e929a/packages/helia/src/index.ts#L144) for the source.


[ipfs]: https://ipfs.io
[js-IPFS]: https://github.com/ipfs/js-ipfs
[kubo]: https://github.com/ipfs/kubo
[filecoin]: https://filecoin.io
[Protocol Labs]: https://protocol.ai
[libp2p]: https://github.com/libp2p/js-libp2p
[bitswap]: https://github.com/ipfs/js-ipfs-bitswap