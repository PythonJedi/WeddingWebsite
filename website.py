from flask import Flask, make_response, render_template
from markupsafe import escape

app = Flask(__name__)

class Story:
    def __init__(self):
        pass

    def render(self):
        return render_template('story.html')

class Rsvp:
    def __init__(self):
        pass

    def render(self):
        return render_template('rsvp.html')

class Registry:
    def __init__(self):
        pass

    def render(self):
        return """<p>We're working on getting registered at the moment.</p>"""

class Gallery:
    photos = ["American Gothic",
              "Ring",
              "Forehead Kisses",
              "Bench",
              "Eskimo Kisses",
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
        return f"/static/{self.name().replace(" ", '')}.jpg"

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
Tab.default = story.id

@app.route("/htmz/tab/<string:id>")
def tab_view(id):
    assert(id in Tab.tabs)
    return Tab.tabs[id].render()

@app.route("/htmz/gallery/<int:index>")
def gallery_view(index):
    g = Gallery(index)
    assert(index in range(len(g.photos)))
    return g.render()


@app.route("/index.html")
def index():
    return render_template('index.html', Tab=Tab)
