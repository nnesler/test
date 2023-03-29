from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

all_movies_dict = [

    {

        "title": "The Hunger Games",

        "director": "Suzanne Collins",

        "time": 220,

        "genre": "fiction",

        "viewing": "theater, again",

        "streaming": "Netflix",

    },]

@app.route("/", methods=["GET", "POST"])

def index():

    return render_template("index.html", pageTitle="My Movies", movies=all_movies_dict)

 

@app.route("/", methods=["GET", "POST"])
def homepage():
    return redirect(url_for("index"))


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        director = form["director"]
        time = form["time"]
        genre = form["genre"]
        viewing = form["movie"]
        streaming = form.getlist("streaming")

        print(title)
        print(director)
        print(time)
        print(genre)
        print(viewing)
        print(streaming)

        streaming_string = ", ".join(streaming)

        movie_dict = {
            "title": title,
            "director": director,
            "time": time,
            "genre": genre,
            "viewing": viewing,
            "streaming": streaming_string,
        }

        print(movie_dict)
        all_movies_dict.append(
            movie_dict
        ) 
        print(all_movies_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route('/about')
def about():
    return render_template(
        "about.html", pageTitle="Web form template", movies=all_movies_dict
    )


if __name__ == "__main__":
    app.run(debug=True)