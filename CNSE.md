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

- U-turn NAT https://live.paloaltonetworks.com/docs/DOC-1678
- DNS Proxy (advanced? cli?)
- Overlapping subnets
- PBF

### More
http://palo-alto-firewall.blogspot.be/2014/01/cnse.html
https://live.paloaltonetworks.com/docs/DOC-6220


[Nat](https://live.paloaltonetworks.com/servlet/JiveServlet/previewBody/1517-102-7-11647/Understanding_NAT-4.1-RevC.pdf)
[DNAT](https://live.paloaltonetworks.com/videos/1550)


https://www.paloaltonetworks.com/content/dam/paloaltonetworks-com/en_US/assets/pdf/datasheets/education/Palo%20Alto%20Networks%20PCNSE6%20Study%20Guide%20Feb%202015.pdf


## focus:
- wildfire flow
- nat objects vs sec objects
- vpn cli output
- bgp
- AA HA
- certificates


## random
block lists in policies
shared-vsys
tap interface
session monitor
url content filtering
content locks
data filtering

user id enabled per zone

safe search

vwire ip address
dns sinkholing : https://live.paloaltonetworks.com/docs/DOC-6220

decryption port mirroring
application filter

the order of evaluation within a url filtering profile is

passive dns monitoring

Anti-virus updates are released daily. Application and Threat updates are released weekly

threat sigs..

zone protection
inter-vsys routing
application override
master key

session overview: https://live.paloaltonetworks.com/docs/DOC-4785

Application Incomplete, Insufficient Data, Not-Applicable:  https://live.paloaltonetworks.com/docs/DOC-1549

video: how to configure url filtering https://live.paloaltonetworks.com/docs/DOC-9549

https://www.paloaltonetworks.com/content/dam/paloaltonetworks-com/en_US/assets/pdf/datasheets/education/CNSE%205.1%20Study%20Guide%20v2.2.pdf

https://live.paloaltonetworks.com/servlet/JiveServlet/previewBody/1628-102-4-37824/DOC-1628.pdf


## WildFire
- decision flow
- file types: apk, pe, pdf, ms office, pdf, java
- subscription ...

## Panorama
- Access domains: limit administrative access to specified device groups ( for custom admin roles / radius VSAs )

### Device Groups 
- Panorama pushed policies are not synchronized between firewall HA peers.

### Templates
- Cannot enable operational modes such as multi-vsys mode, FIPS mode, or CC mode using templates; these operational settings must be configured locally on each device.
- Cannot configure the IP address details for the firewall HA pair.
- Cannot configure a master key and diagnostics.
