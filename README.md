Palo-Alto
=========

Palo Alto commands

- Debug Flow Basic
```
debug dataplane packet-diag clear log log
debug dataplane packet-diag set filter on
debug dataplane packet-diag set filter match [ source destination ... ]

debug dataplane packet-diag set log feature flow basic
debug dataplane packet-diag show setting
debug dataplane packet-diag set log on

debug dataplane packet-diag set log off
debug dataplane packet-diag aggregate-logs 

less dp-log pan_packet_diag.log  
```

- System info

```
show jobs all
show system resources follow
show running resource-monitor
show session info
debug dataplane pool statistics
show counter global filter aspect resource
show system statistics
```

- Errors, drops

```
show counter global | match drop
show interface ethernetX/X
show system state filter * | match over
```


The following is very effective command in troubleshooting a suspect packet drop scenario. The reason for packets dropped can help narrow down on what the issue is.

```
show counter global filter severity drop
```
The above command can be used with the Delta option which allows viewing packets dropped since the last time the command was issued.
```
show counter global filter delta yes severity drop
```
Apart from the severity drop, there are various other severities that this command can be used for based on the scenario. A few examples are: error, informational and warning.

Packet filter can be enabled using the following command:

```
debug dataplane packet-diag set filter match source x.x.x.x destination y.y.y.y
debug dataplane packet-diag set filter on
```
To get the deltas:
```
show counter global filter packet-filter yes delta yes
```


- VPN 

```
show vpn ike-sa gateway
test vpn
```

- USER id 
```
show user group name Domain\user
show user ip-user-mapping all
clear user-cache ip 1.1.1.1

```

links:
http://blog.webernetz.net/2013/11/21/cli-commands-for-troubleshooting-palo-alto-firewalls/
https://live.paloaltonetworks.com/servlet/JiveServlet/previewBody/4254-102-6-17063/qrg_v6.pdf
