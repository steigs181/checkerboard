from flask import Flask, render_template
app = Flask (__name__)

@app.route ('/')
def display_level_1 ():
    return render_template ("index.html", box_x = 8, box_y = 8, color_x ="red", color_y= "black")

@app.route('/<int:box_x>')
def display_2 (box_x):
    return render_template("index.html", box_x = box_x, box_y = 8, color_x = "red", color_y = "black")

@app.route('/<int:box_x>/<int:box_y>')
def display_3(box_x, box_y):
    return render_template("index.html", box_x = box_x, box_y = box_y, color_x = "red", color_y = "black")

@app.route('/<int:box_x>/<int:box_y>/<string:color_x>/<string:color_y>')
def display_4 (box_x, box_y, color_x, color_y):
    return render_template("index.html", box_x = box_x, box_y = box_y, color_x = color_x, color_y = color_y)


if __name__ == "__main__":
    app.run (debug = True)