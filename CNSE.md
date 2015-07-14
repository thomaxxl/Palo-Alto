### Platforms and Architecture
- Platforms
- [Single-Pass Parallel Processing Architecture](http://www.paloguard.com/SP3-Architecture.asp)
    App,User,Content-ID
- Control- & Data Plane
- Flow Logic
- Initial config 
```
set deviceconfig system ip-address 192.168.1.1 netmask y.y.y.y default-gateway z.z.z.z dns-setting servers primary v.v.v.v
```
- Application Command Center : dynamic reports w/ links to log info
- CLI
```
find command keyword fpga
```
### Administration and Management
- Passwords
- Certificates : usage, generate, ocsp, csr, CA
- Log forwarding 
    - configured in sec policy or zone protection
    - debugging
    ```
    debug log-receiver statistics
    debug syslog-ng stats
    debug syslog-ng [trace-on|trace-off]
    less mp-log syslog-ng.log
    tcpdump snaplen 1500 filter "tcp port 514"
    view-pcap no-dns-lookup yes no-port-lookup yes verbose yes hex-ascii yes mgmt-pcap mgmt.pcap 
    ```
- __Objects>Applications__:Customize application settings : timeout, risk
- Reports

### Interface Configuration
- vlans & interfaces
- QoS Policy & Profile, monitoring
- 
### Layer 3 Configuration

### More
http://palo-alto-firewall.blogspot.be/2014/01/cnse.html
https://live.paloaltonetworks.com/docs/DOC-6220

####
[Nat](https://live.paloaltonetworks.com/servlet/JiveServlet/previewBody/1517-102-7-11647/Understanding_NAT-4.1-RevC.pdf)
[DNAT](https://live.paloaltonetworks.com/videos/1550)
