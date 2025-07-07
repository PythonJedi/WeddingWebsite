from flask import Flask, make_response, render_template, url_for
from markupsafe import escape
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

import sys
if "--debug" not in sys.argv:
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )

class Story:
    def __init__(self):
        pass

    def render(self):
        return render_template('story.html')

class Registry:
    def __init__(self):
        pass

    def render(self):
        return render_template('registry.html')

class Rsvp:
    def __init__(self):
        pass

    def render(self):
        return render_template('rsvp.html')

class Gallery:
    photos = ["American Gothic",
              "Ring",
              "Forehead Kisses",
              "Bench",
              "Noses",
              "Disney Stare",
              "Bridge"]

    def __init__(self, index=0):
        self.index = index

    def prev(self):
        return (self.index-1) % len(self.photos)

    def next(self):
        return (self.index+1) % len(self.photos)

    def name(self):
        return self.photos[self.index]

    def path(self):
        return f"/static/{self.name().replace(' ', '')}.jpg"

    def render(self):
        return render_template('gallery.html', current=self, indices=range(len(self.photos)))


class Tab:
    tabs = {}

    def __init__(self, id, name, obj):
        self.id = id
        self.name = name
        self.obj = obj
        self.tabs[id] = self

    def render(self):
        return render_template('tabview.html', tabs=self.tabs, selected=self.id)

story = Tab("story", "Our Story", Story())
rsvp = Tab("rsvp", "RSVP", Rsvp())
registry = Tab("registry", "Registry", Registry())
gallery = Tab("gallery", "Gallery", Gallery())

@app.route("/htmz/tab/<string:id>")
def tab_view(id):
    assert(id in Tab.tabs)
    return Tab.tabs[id].render()

@app.route("/htmz/gallery/<int:index>")
def gallery_view(index):
    g = Gallery(index)
    assert(index in range(len(g.photos)))
    return g.render()

@app.route("/story.html")
def story_wrap():
    return render_template('index.html', content=story)

@app.route("/rsvp.html")
def rsvp_wrap():
    return render_template('index.html', content=rsvp)

@app.route("/registry.html")
def registry_wrap():
    return render_template('index.html', content=registry)

@app.route("/gallery.html")
def gallery_wrap():
    return render_template('index.html', content=gallery)
