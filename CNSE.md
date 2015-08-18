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

### VPN
[troubleshooting](https://live.paloaltonetworks.com/docs/DOC-3671)
```
show vpn tunnel
show vpn gateway
show vpn ike-sa
```

### High Availability
```
admin@PA> show high-availability all
admin@PA> show high-availability state
admin@PA> show high-availability link-monitoring
admin@PA> show high-availability path-monitoring
```
### More
http://palo-alto-firewall.blogspot.be/2014/01/cnse.html
https://live.paloaltonetworks.com/docs/DOC-6220


[Nat](https://live.paloaltonetworks.com/servlet/JiveServlet/previewBody/1517-102-7-11647/Understanding_NAT-4.1-RevC.pdf)
[DNAT](https://live.paloaltonetworks.com/videos/1550)


https://www.paloaltonetworks.com/content/dam/paloaltonetworks-com/en_US/assets/pdf/datasheets/education/Palo%20Alto%20Networks%20PCNSE6%20Study%20Guide%20Feb%202015.pdf

## SSL decryption
troubleshooting:

Verify the outbound proxy 
```
>show system setting ssl-decrypt setting
```
Check counters for warnings
```
>show counter global filter category proxy
```
Check memory pools
```
>debug dataplane pool statistics
```
Check the exclude cache for the destination IP or Cert
```
>show system setting ssl-decrypt exclude-cache
```
```
debug dataplane packet-diag:

  log feature ssl basic
  log feature proxy basic
```


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
an interface in vwire mode has no mac address

[dns sinkholing](https://live.paloaltonetworks.com/docs/DOC-6220)

decryption port mirroring

[application filter](https://live.paloaltonetworks.com/docs/DOC-5477)


[URL Filtering Order](https://live.paloaltonetworks.com/docs/DOC-2731) : block/allow/custom/cached/pre-defined

passive dns monitoring

Anti-virus updates are released daily. Application and Threat updates are released weekly

threat sigs..

zone protection

inter-vsys routing

application override

master key

[session overview](https://live.paloaltonetworks.com/docs/DOC-4785)

[Application Incomplete, Insufficient Data, Not-Applicable: ](https://live.paloaltonetworks.com/docs/DOC-1549)

[Improving Performance of HTTP with DSRI](https://live.paloaltonetworks.com/docs/DOC-5996)

[video: how to configure url filtering](https://live.paloaltonetworks.com/docs/DOC-9549)
[video: How to Configure IPS aka Vulnerability Protection Profile](https://live.paloaltonetworks.com/videos/1133)
https://www.paloaltonetworks.com/content/dam/paloaltonetworks-com/en_US/assets/pdf/datasheets/education/CNSE%205.1%20Study%20Guide%20v2.2.pdf

https://live.paloaltonetworks.com/servlet/JiveServlet/previewBody/1628-102-4-37824/DOC-1628.pdf


## WildFire
- [decision flow](https://www.paloaltonetworks.com/documentation/60/wildfire/wf_admin/wildfire-overview/about-wildfire.html)
- file types: apk, pe, pdf, ms office, pdf, java
- subscription ...

## Panorama
- Access domains: limit administrative access to specified device groups ( for custom admin roles / radius VSAs )
- Distributed Log Collection : > 10K logs/sec
- admin types: panorama, device group, template, local
- group HA peers

### Device Groups 
- Panorama pushed policies are not synchronized between firewall HA peers.

### Templates
- Cannot enable operational modes such as multi-vsys mode, FIPS mode, or CC mode using templates; these operational settings must be configured locally on each device.
- Cannot configure the IP address details for the firewall HA pair.
- Cannot configure a master key and diagnostics.
