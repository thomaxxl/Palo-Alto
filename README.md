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

- VPN 

```
show vpn ike-sa gateway
test vpn
```
