#!/bin/env python

from xml.dom import minidom
from xml.dom.ext import PrettyPrint
from xml.dom.minidom import Node
from xml.xpath import Evaluate

from urllib import urlopen
import sys, os
import logging

class PA_API():

    def __init__(self,address, username, password):
        '''
            Retrieve the session key
        '''
        self.address  = address
        self.username = username
        self.password = password
        self.apiurl= 'https://%s/esp/restapi.esp'%address
        self.log = logging.getLogger()
        self.key   = self.get_key(username,password)

    def get_key(self,username,password):
        url      = '%s?type=keygen&user=%s&password=%s'%(self.apiurl,username,password)
        response = self.get_xml(url)
        status   = response.attributes['status'].value

        if status != "success":
            self.log.error("Login failed")
            return None
        else:
            return response.getElementsByTagName('key')[0].firstChild.nodeValue

    def get_xml(self,url):
        '''
            Get the xml repsonse from the PA api url
            This function rturns None if the query failed
        '''

        try:
            res   = urlopen(url)
            xml   = minidom.parse(res)
            response = xml.getElementsByTagName('response')
        except Exception as e:
            self.log.error("get_xml : %s" % str(e) )
            self.log.error("get_xml url : %s" % url )
            return None

        return response[0]


    def query(self, xmlcmd):
        '''
            query the PA api
        '''

        url      = '%s?key=%s&type=op&' % (self.apiurl,self.key)
        url     += 'cmd=' + xmlcmd
        response = self.get_xml(url)
        status   = response.attributes['status'].value

        if status != "success":
            self.log.error("query failed: status is '%s'" % status)
            self.log.error("query url : %s" % url )
            self.log.error(PrettyPrint(response))
            return None

        return response

    def get_resource_mon(self):
        cmd = '<show><running><resource-monitor><minute></minute></resource-monitor></running></show>'
        return self.query(cmd)

    def get_resource_util(self,dp):
        res_mon = self.get_resource_mon()
        entries = Evaluate("//data-processors/%s/minute/resource-utilization/entry"%dp,contextNode=res_mon)
        return entries

    def get_dp_stats(self, timeframe = 'minute'):
        res_mon = self.get_resource_mon()
        dps = Evaluate("//data-processors",contextNode=res_mon)
        if not dps:
            log.error("no data-processors")
            return None

        dps = dps[0]
        for dp in dps.childNodes:
            if dp.nodeType == Node.ELEMENT_NODE:
                dp_name = dp.nodeName
                cores = Evaluate(".//%s/cpu-load-average/entry"%timeframe,contextNode=dp)
                for core in cores:
                    val = core.getElementsByTagName('value')[0].nodeValue
                    coreid = Evaluate(".//coreid",contextNode=core)
                    values = Evaluate(".//value",contextNode=core)

        return res_mon

    def get_load(self,coreid,type='average'):
        try:
            dp   = coreid.split('.')[0]
            core = coreid.split('.')[1]
            res_mon = self.get_resource_mon()
            entries = Evaluate("//%s/minute/cpu-load-%s/entry"%(dp,type),contextNode=res_mon)
            for entry in entries:
                if entry.getElementsByTagName("coreid")[0].firstChild.nodeValue == core:
                    node_value = entry.getElementsByTagName("value")[0].firstChild.nodeValue
                    return node_value

        except Exception as e:
            self.log.error("get_load_average error")

        return None

    def get_uid_agents(self):
        result = {}
        cmd = '<show><user><user-id-agent><statistics></statistics></user-id-agent></user></show>'
        response = self.query(cmd)
        agents = response.getElementsByTagName('entry')
        for agent in agents:
            if agent and agent.getAttribute('name'):
                #print '--' ,PrettyPrint(agent) , '--'
                #print dir(agent)
                aname = agent.getAttribute('name')
                connected = agent.getElementsByTagName("connected")[0].firstChild.nodeValue
                result[aname] = connected
        return result

    def get_pkt_recv(self):
        cmd = '<show><counter><global><name>pkt_recv</name></global></counter></show>'
        response = self.query(cmd)
        if not response:
            log.error('no response for pkt_recv')
            return None
        value = response.getElementsByTagName('value')[0].firstChild.nodeValue
        return int(value)

    def get_counter(self,counter):
        cmd = '<show><counter><global><name>%s</name></global></counter></show>'%counter
        response = self.query(cmd)
        if not response:
            log.error('no response for %s'%counter)
        value = response.getElementsByTagName('value')[0].firstChild.nodeValue
        return int(value)

    def get_system_resources(self):
        cmd = '<show><system><resources></resources></system></show>'
        response = self.query(cmd)
        return response.getElementsByTagName('result')[0].firstChild.wholeText



def get_properties(*args):
    # imporing dmd results in corruption, spawn a separate process
    cmd = "get-property.py %s"%" ".join(args)
    result = os.popen(cmd).read().splitlines()
    return result

if __name__ == "__main__":

    address  = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    dp = sys.argv[4]

    pa_api = PA_API(address, username, password)

    print pa_api.get_system_resources()
    #print pa_api.get_pkt_recv()
    #response = pa_api.get_dp_stats()
    #dps = response.getElementsByTagName("data-processors")[0]
    #print PrettyPrint(dps)
    #print pa_api.get_uid_agents()
    #print pa_api.get_resource_util('dp0')
    #print response[0].attributes['response'].value
    #print PrettyPrint(response)
