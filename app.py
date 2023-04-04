from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_random_string"

all_movies_dict = [

    {

        "title": "The Hunger Games",

        "director": "Suzanne Collins",

        "time": 220,

        "genre": "fiction",

        "viewing": "theater, again",

        "streaming": "Netflix",

    },]

# Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

# Handling error 500 and displaying relevant web page
@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


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
        viewing = form.getlist("movie")
        streaming = form["service"]

        print(title)
        print(director)
        print(time)
        print(genre)
        print(viewing)
        print(streaming)

        viewing_string = ", ".join(viewing)

        movie_dict = {
            "title": title,
            "director": director,
            "time": time,
            "genre": genre,
            "viewing": viewing_string,
            "streaming": streaming,
        }

        print(movie_dict)
        all_movies_dict.append(
            movie_dict
        ) 
        print(all_movies_dict)
        flash('Sucess! Your record has been added.', 'success')
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