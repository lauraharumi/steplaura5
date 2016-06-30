#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webapp2
import random
html = """
<html>
	<head>
		<meta charset = "utf-8"/>
		<title>Suffle Words</title> 
	</head>
	<body style="margin: 20%">
		<h3>Enter two words to mess order </h3>
		<form>
			Word 1: <input name="word1" type="text" value="" /><br/>
			Word 2: <input name="word2" type="text" value=""/><br/>
			<br>
		  	<button type="submit">Mess</button>
		</form>
		<hr /> 
	</body>
</html> 
"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(html)

    # def post(self):
    	word1, word2 = self.request.get("word1"), self.request.get("word2")
    	new = []

    	if len(word1) < 1 or len(word2) < 1:
    		self.response.write("<h2>input two words! </h2>" )
    	else: 
	    	if len(word2)> len(word1):
	    		longer, shorter= word2, word1
	    	else: 
	    		longer, shorter = word1, word2
    	 	
		for i in xrange(len(shorter)):
			new += shorter[i],longer[i]
		new += longer[len(shorter):len(longer)]
		self.response.write("<h2>New word: " + ''.join(new) + "</h2>")
app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)


