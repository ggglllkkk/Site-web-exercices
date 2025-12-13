from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import databaseManager as dbM

app = Flask("site bou", template_folder="templates", static_folder="static")

@app.route("/")
def Index():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def Login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        userId=request.form.get("userId")
        if not dbM.IdExists(userId):
            return render_template("login.html")
        return redirect(url_for("Exercice", exerciceId=0, userId=userId))

@app.route("/register", methods=["GET", "POST"])
def Register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        userId=dbM.registerNew()
        return redirect(url_for("Registered", userId=userId))

@app.route("/registered", methods=["GET", "POST"])
def Registered():
    userId=request.args.get("userId")
    if request.method=="GET":
        return render_template("registered.html", userId=userId)
    else:
        return redirect(url_for("Exercice", exerciceId="0", userId=userId))

@app.route("/exercice/<exerciceId>", methods=["GET", "POST"])
def Exercice(exerciceId):
    print(exerciceId)
    return render_template("exercice.html")


if __name__ == '__main__':
    #app.run(host="0.0.0.0", debug=True)
    app.run(debug=True)