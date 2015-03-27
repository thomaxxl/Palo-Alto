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
        url   = '%s?type=keygen&user=%s&password=%s'%(self.apiurl,username,password)
        res   = self.get_xml(url)
        self.key   = res.getElementsByTagName('key')[0].firstChild.nodeValue
        self.log = logging.getLogger()

    def get_xml(self,url):
        '''
            Get the xml repsonse from the PA api url
            This function rturns None if the query failed
        '''

        try:
            res   = urlopen(url)
            xml   = minidom.parse(res)
            response = xml.getElementsByTagName('response')
            print url

        except Exception as e:
            log.error("get_xml : %s" % str(e) )
            log.error("get_xml url : %s" % url )
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
            log.error("query failed: status is '%s'" % status)
            log.error("query url : %s" % url )
            log.error(PrettyPrint(response))
            return None

        return response

    def get_resource_mon(self):
        cmd = '<show><running><resource-monitor></resource-monitor></running></show>'
        return self.query(cmd)

    def get_dp_stats(self, timeframe = 'minute'):
        res_mon = self.get_resource_mon()
        print res_mon
        print dir(res_mon)
        dps = Evaluate("//data-processors",contextNode=res_mon)
        if not dps:
            log.error("no data-processors")
            return None

        dps = dps[0]
        for dp in dps.childNodes:
            if dp.nodeType == Node.ELEMENT_NODE:
                dp_name = dp.nodeName
                print 'nn:',dp_name
                cores = Evaluate(".//%s/cpu-load-average/entry"%timeframe,contextNode=dp)
                for core in cores:
                    print dir(core)
                    print PrettyPrint(core)
                    print core.firstChild.nodeValue
                    val = core.getElementsByTagName('value')[0].nodeValue
                    print dir(val)
                    coreid = Evaluate(".//coreid",contextNode=core)
                    values = Evaluate(".//value",contextNode=core)
                    print PrettyPrint(coreid)
                    print PrettyPrint(values)


        return res_mon

if __name__ == "__main__":

    address  = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]

    pa_api = PA_API(address, username, password)


    response = pa_api.get_dp_stats()
    #print response[0].attributes['response'].value
    print '--'
    #print PrettyPrint(response)
    print '--'
