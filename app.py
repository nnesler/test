from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

all_books_dict = [

    {

        "title": "The Hunger Games",

        "author": "Suzanne Collins",

        "pages": 384,

        "classification": "fiction",

        "details": "read, highly recommend",

        "acquisition": "library",

    },]

@app.route("/", methods=["GET", "POST"])

def index():

    return render_template("index.html", pageTitle="My Library", books=all_books_dict)

 

@app.route("/", methods=["GET", "POST"])
def homepage():
    return redirect(url_for("index"))


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["title"]
        author = form["author"]
        pages = form["pages"]
        classification = form["genre"]
        details = form["book"]
        acquistion = form.getlist("how")

        print(title)
        print(author)
        print(pages)
        print(classification)
        print(details)
        print(acquistion)

        acquistion_string = ", ".join(acquistion)

        book_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "classification": classification,
            "details": details,
            "acquisition": acquistion_string,
        }

        print(book_dict)
        all_books_dict.append(
            book_dict
        ) 
        print(all_books_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route('/about')
def about():
    return render_template(
        "about.html", pageTitle="Web form template", books=all_books_dict
    )


if __name__ == "__main__":
    app.run(debug=True)