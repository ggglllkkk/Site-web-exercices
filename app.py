from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import databaseManager as dbM
import questions as q

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
        return redirect(url_for("Exercice", exerciceId=1, userId=userId))

@app.route("/register", methods=["GET", "POST"])
def Register():
    if request.method=="GET":
        userId=dbM.registerNew()
        return render_template("register.html", userId=userId)
    else:
        userId=request.args.get("userId")
        return redirect(url_for("Exercice", exerciceId=1, userId=userId))

@app.route("/exercice/<exerciceId>", methods=["GET", "POST"])
def Exercice(exerciceId):
    userId=int(request.args.get("userId"))
    exerciceId=int(exerciceId)
    if request.method=="GET":
        if exerciceId-1>=len(q.questionsList):
            return render_template("termine.html")
        (enonce, image, htmlQ, reponses, textInput) = q.questionsList[exerciceId-1].GetQuestion()
        return render_template("exercice.html", exerciceId=exerciceId, userId=userId, enonce=enonce, image=image, htmlQ=htmlQ, reponses=reponses, textInput=textInput)
    else:
        textInput=request.form.get("textInput")
        answers=[request.form.get(str(k))=="on" for k in range(len(q.questionsList[exerciceId-1].reponses))]
        dbM.registerAnswer(userId, exerciceId-1, answers, textInput)
        return redirect(url_for("Exercice", exerciceId=exerciceId+1, userId=userId))

@app.route("/cours/<exerciceId>", methods=["GET"])
def Cours(exerciceId):
    exerciceId=int(exerciceId)
    userId=int(request.args.get("userId"))

    dbM.registerCours(userId, exerciceId-1)
    (enonce, image, htmlC) = q.questionsList[exerciceId-1].GetCours()
    return render_template("cours.html", userId=userId, exerciceId=exerciceId, enonce=enonce, image=image, htmlC=htmlC)


if __name__ == '__main__':
    #app.run(host="0.0.0.0", debug=True)
    app.run(debug=True)