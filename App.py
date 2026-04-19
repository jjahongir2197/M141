from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hobby", methods=["GET", "POST"])
def hobby():
    if request.method == "POST":
        hobbies = request.form.getlist("hobby")

        result = ", ".join(hobbies)

        return render_template("result23.html", result=result)

    return render_template("index23.html")

if __name__ == "__main__":
    app.run(debug=True)
