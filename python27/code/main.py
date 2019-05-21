#!/usr/bin/python
import web

urls = ('/.*', 'Redir')

app = web.application(urls, globals())

class Redir:

    def GET(self):
        #Change the following to your target subdomain...
        #be sure to add the trailing slash '/' this saves a redirect
        raise web.seeother('https://www.example.com/')


app = app.gaerun()
