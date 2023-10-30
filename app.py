from flask import Flask , render_template,request
import stories 
from stories import Story

app = Flask(__name__)

@app.route("/form")

def show_form():
    return render_template("form.html")

@app.route("/story")
def get_story():
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]
    story_class = Story
    story_var = stories.story
    ans = {"place":place, "noun":noun, "verb":verb, "adjective":adjective, "plural_noun":plural_noun}
    return render_template("story.html", story =story_var.generate(ans))



