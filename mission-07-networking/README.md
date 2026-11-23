# Mission 7 — How computers communicate

## 1. Task / objective
The goal of this mission was to learn how computer networks work, understand common networking terms like LAN, WAN, and DNS, test network connectivity and address lookup using Terminal commands (`ping` and `nslookup`), and write a simple 5-to-7 step explanation of what happens when you open a website in a browser.

## 2. Work completed
- Filled out the network concepts table with explanations and simple examples.
- Ran a connectivity test using `ping` to see if my computer could reach `example.com`.
- Ran a DNS lookup using `nslookup` to see the IP address behind `example.com`.
- Answered questions about what ping tests, what DNS lookups show, and why DNS is important.
- Wrote a 6-step breakdown of how a browser opens a website, using the required terms: *client*, *server*, *DNS*, and *protocol*.

## 3. Commands / tools used
- `ping -c 3 example.com`: Sent 3 test packets to see if the website server was responding.
- `nslookup example.com`: Looked up the IP address linked to the domain name.

## 4. My understanding

### Task 7.1 — Explain network concepts

| Concept | Explain it in your own words | Example |
| :--- | :--- | :--- |
| **LAN** | A local network that connects computers and devices in a small area. | A home Wi-Fi network connecting a laptop, phone, and TV. |
| **MAN** | A network that covers a larger area like a whole city or a college campus. | A university network connecting all the buildings and hostels across campus. |
| **WAN** | A wide network that connects computers across cities, countries, or the whole world. | The Internet. |
| **DNS** | The system that turns human-friendly website names into numbers (IP addresses) that computers use. | Translating `example.com` into `104.20.23.154`. |
| **Router** | A device that forwards data between different networks and directs traffic to the right place. | A home Wi-Fi router connecting my devices to the internet. |
| **Protocol** | A set of rules that computers follow so they can understand each other. | HTTP or HTTPS for web pages, and TCP for reliable data transfer. |
| **Packet switching** | Breaking down data into small pieces called packets that travel across the network and get put back together at the destination. | Sending a message or loading a web page over the internet. |
| **Client-server** | A system where one computer (client) asks for information, and another computer (server) provides it. | A web browser asking for a web page from a web server. |

---

### Task 7.2 — Observe network information
- **Connectivity test (`ping`):**
  - Command: `ping -c 3 example.com`
  - Observation: Sent 3 packets and received all 3 back with `0.0% packet loss`. The average round-trip time was about 8 milliseconds.
- **DNS lookup (`nslookup`):**
  - Command: `nslookup example.com`
  - Observation: The DNS resolver returned IP address `104.20.23.154` (and `172.66.147.243`).
- **Questions & Explanations:**
  - **What a connectivity test helps you check:**  
    It tells you if your computer can actually reach another computer or server on the network, how long the message takes to go and come back, and whether any data packets were lost.
  - **What information a DNS lookup displays:**  
    It shows the domain name you searched for, the name server that answered, and the IP address mapped to that name.
  - **Role of DNS when you enter a website name in a browser:**  
    Humans remember names like `example.com`, but computers need numeric IP addresses to find each other on the network. When you type a name into a browser, DNS looks up the IP address so the browser knows where to send the request.

---

### Task 7.3 — What happens when you open a website?
Here is what happens in order when you type a website name into your browser and press Enter:

1. **Entering the website name:** You open your web browser (which is the **client**) and type in a web address like `https://example.com`.
2. **Looking up the address via DNS:** Your browser needs the computer address (IP address) for that name, so it asks a **DNS** server to translate `example.com` into its IP address (`104.20.23.154`).
3. **Connecting through the network:** Once the browser has the IP address, it uses the network **protocol** (like TCP and HTTPS) to start a connection.
4. **Sending the request through the router:** The request is broken into packets and sent through your local **router**, which forwards them across the internet toward the website's location.
5. **The server responds:** The remote web **server** gets the request, finds the requested web page data, and sends it back in packets across the network.
6. **Displaying the page:** The browser client receives all the packets, puts the data together, and displays the web page text and images on your screen.

## 5. Difficulties faced
Understanding how `ping` and `nslookup` differ.

## 6. How I resolved them
I realized that `nslookup` only looks up the IP address in the phonebook (DNS), while `ping` actually sends test packets to see if the server is online and responding.

## 7. Evidence / files
- Mission 7 documentation: `mission-07-networking/README.md`

## 8. Commit details
- **Commit message:** `Explain networking concepts and website communication`
- **Branch:** `main`
- **Push status:** Pushed to GitHub
