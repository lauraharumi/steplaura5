#!/usr/bin/env python
#coding=utf8
import webapp2
import random
import time
import json

localtime = time.asctime( time.localtime(time.time()) )
html = open("main.html","r").read()
output = json.load(open("data.json","r"))
out_data = json.load(open("outrages.json","r"))

def create_graph(output): 
    graph = {}
    for line_stations_map in output:
        eki_list = line_stations_map['Stations']
        for i, eki in enumerate(eki_list):
            if eki not in graph: 
                graph[eki] = []
            for j in (i-1, i+1):
                if 0 <= j < len(eki_list):
                    graph[eki].append(eki_list[j])
    return graph
    
def outrages(graph, out_data):
    for from_to in out_data:
        graph[from_to['From']].remove(from_to['To'])
    return graph
    
def find_route(graph, start, end, route=[]):
    route = route + [start]
    if start == end:
        return route
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in route:
            newroute = find_route(graph, node, end, route)
            if newroute: return newroute
    return None

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(localtime + html)
        start, end = self.request.get("from"), self.request.get("to")
        out_checked = self.request.get("check")
        self.response.write("<h4> From: " + start + " To: "+ end + out_checked + "</h4><br>")
        if out_checked: 
            route = find_route(outrages(create_graph(output), out_data), start, end)
        else: 
            route = find_route(create_graph(output), start, end)
        for station in route: 
            self.response.write(station + " --> ")
            
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
