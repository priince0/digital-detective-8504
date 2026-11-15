# Mission 7 — How computers communicate

## 1. Task / objective
The objective of this mission was to explore computer networking fundamentals, understand standard network topologies and conceptual models, observe network connectivity and domain name resolution using command-line diagnostic tools (`ping`, `nslookup`), and construct a structured 5-to-7 step explanation detailing the end-to-end communication process when accessing a website.

## 2. Work completed
- Populated the network concepts table explaining LAN, MAN, WAN, DNS, Router, Protocol, Packet Switching, and the Client-Server model with realistic examples.
- Conducted an ICMP echo connectivity test to verify reachability and latency to a public domain (`example.com`).
- Performed a DNS name resolution lookup using `nslookup` to discover IP addresses mapped to `example.com`.
- Explained the purpose of connectivity testing, DNS records, and the browser resolution flow.
- Authored a 6-step breakdown tracing how a web browser requests, receives, and renders a web page using correct networking terminology (*client*, *server*, *DNS*, and *protocol*).

## 3. Commands / tools used
- `ping -c 3 example.com`: Sent 3 ICMP echo request packets to measure round-trip time and packet loss.
- `nslookup example.com`: Queried configured DNS servers to resolve the domain name to its IPv4 addresses.

## 4. My understanding

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN (Local Area Network)** | A computer network connecting devices within a limited, localized physical geographic area under unified management. | Home Wi-Fi network connecting a laptop, smartphone, and smart TV. |
| **MAN (Metropolitan Area Network)** | A communication network spanning an entire city, municipal area, or sprawling university campus. | A university campus network interconnecting departmental academic buildings and student hostels across a town. |
| **WAN (Wide Area Network)** | A telecommunications network spanning large geographic distances across cities, countries, or continents. | The global Internet, or an international banking network connecting branches worldwide. |
| **DNS (Domain Name System)** | A hierarchical distributed naming system that translates human-friendly domain names into machine-routable numerical IP addresses. | Translating `example.com` into destination IP `104.20.23.154`. |
| **Router** | A networking layer-3 device that inspects destination IP headers and routes packets across differing networks. | A home wireless gateway router forwarding packets between the local private subnet and the ISP network. |
| **Protocol** | An established, standardized set of rules and message formats governing how devices format, transmit, and verify data. | HTTP / HTTPS for web pages, TCP for reliable transport, IP for packet routing. |
| **Packet switching** | A transmission paradigm where digital data is broken down into small, independently addressed packets that traverse various network paths before reassembly at the destination. | Web pages split into standard TCP/IP packets traveling across diverse optical fiber routers across the Internet. |
| **Client-server** | A distributed computing architecture where client programs initiate service requests and central server programs fulfill and respond to those requests. | A web browser (client) requesting an HTML document from a remote web server (server) hosting the site. |

---

### Task 7.2 — Observe network information
- **Network reachability test (`ping`):**
  - Command: `ping -c 3 example.com`
  - Output summary:
    - 3 packets transmitted, 3 packets received, `0.0% packet loss`.
    - Round-trip latency: min = `4.371 ms`, avg = `8.144 ms`, max = `15.622 ms`.
- **DNS name resolution (`nslookup`):**
  - Command: `nslookup example.com`
  - Output summary:
    - Resolver: `8.8.8.8#53` (Public DNS)
    - Resolved Addresses: `104.20.23.154`, `172.66.147.243`
- **Questions & Explanations:**
  - **What a connectivity test helps you check:**
    A tool like `ping` tests whether a remote host is online, reachable across the network, and responding to ICMP packets. It measures network round-trip time (latency) and detects packet loss or routing dropouts.
  - **What information a DNS lookup displays:**
    A DNS lookup tool displays the domain name queried, the resolver server answering the query, and the associated resource records (such as IPv4 `A` records or IPv6 `AAAA` records) mapping the name to IP addresses.
  - **Role of DNS when entering a website name in a browser:**
    Because humans remember names (like `example.com`) while network routing protocols require numerical IP addresses (like `104.20.23.154`), DNS acts as the Internet's address book. The browser queries DNS before initiating any connection so it knows where to send TCP packets.

---

### Task 7.3 — What happens when you open a website?
When a user types a website address (such as `https://example.com`) into a browser and presses Enter, the following sequence occurs:

1. **URL Parsing & Cache Check:** The web browser (**client**) inspects the entered URL, identifies the **protocol** (`https`), and checks local browser and OS caches to see if the IP address for the domain name is already known.
2. **DNS Resolution:** If the IP address is not cached, the client issues a **DNS** query to the configured recursive resolver. The resolver traverses the DNS hierarchy (Root, TLD, and Authoritative servers) to translate `example.com` into its destination IP address (`104.20.23.154`) and returns it to the client.
3. **TCP Connection & TLS Handshake:** The client initiates a reliable network connection with the destination IP address using the TCP **protocol** (three-way handshake: SYN, SYN-ACK, ACK). For HTTPS, a TLS cryptographic handshake follows to negotiate encryption keys and verify identity.
4. **Packet Routing Across Network:** Network packets carrying the request leave the client machine and are directed by the local home or office **router**, which routes the packets across intermediate ISP routers and optical backbones toward the destination network.
5. **Server Processing:** The remote web **server** listening on port 443 receives the encrypted HTTP GET request packets, reassembles them, decrypts the payload, processes the request, and generates an HTTP response containing the HTML, CSS, JavaScript, and asset resources.
6. **Response Transmission & Browser Rendering:** The server transmits the response packets back across the network to the client. The browser client receives the packets, parses the HTML document structure, downloads associated assets, executes JavaScript, and renders the visual web page on the user's screen.

## 5. Difficulties faced
Distinguishing between network-level reachability (ICMP ping responses) and application-level availability (HTTP status responses), as some firewalls block ping packets while still serving web pages.

## 6. How I resolved them
Verified connectivity using both `ping` and `nslookup`, confirming that `example.com` was actively responding to ICMP echo requests with zero packet loss and resolving valid IP records.

## 7. Evidence / files
- Mission 7 documentation: `mission-07-networking/README.md`

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Branch:** `main`
- **Push status:** Pushed to `https://github.com/priince0/digital-detective-8504.git`
