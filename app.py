from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from waitress import serve
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
            return render_template("login.html", error="L'id n'existe pas, vérifier le numéro ou revenir à l'accueil pour recréer un compte")
        return redirect(url_for("SetSelection", userId=userId))

@app.route("/register", methods=["GET", "POST"])
def Register():
    if request.method=="GET":
        userId=dbM.registerNew()
        return render_template("register.html", userId=userId)
    else:
        userId=request.args.get("userId")
        return redirect(url_for("SetSelection", userId=userId))
    
@app.route("/setSelection", methods=["GET", "POST"])
def SetSelection():
    userId=int(request.args.get("userId"))

    if not dbM.IdExists(userId):
        return render_template("message.html", error="Id n'existe pas, il faut recréer un compte depuis l'accueil")
    
    if request.method=="GET":
        return render_template("setSelection.html", userId=userId)
    else:
        try:
            exerciceSet=int(request.form.get("setId"))
            if not q.SetIdExists(exerciceSet):
                return render_template("setSelection.html", userId=userId, error="Le numéro de série d'exercice n'existe pas, vérifie avec le professeur.")
            return redirect(url_for("Exercice", setId = exerciceSet, exerciceId=1, userId=userId))
        except:
            return render_template("setSelection.html", userId=userId, error="Le numéro de série d'exercice n'existe pas, vérifie avec le professeur.")


@app.route("/exercice/<setId>/<exerciceId>", methods=["GET", "POST"])
def Exercice(setId, exerciceId):
    userId=int(request.args.get("userId"))
    setId=int(setId)
    exerciceId=int(exerciceId)

    if not dbM.IdExists(userId):
        return render_template("message.html", error="Id n'existe pas, il faut recréer un compte depuis l'accueil")

    if request.method=="GET":
        if exerciceId-1>=len(q.questionSetList[setId-1]):
            return render_template("termine.html")
        (enonce, image, htmlQ, reponses, textInput) = q.questionSetList[setId-1][exerciceId-1].GetQuestion()
        return render_template("exercice.html", exerciceId=exerciceId, setId=setId, userId=userId, enonce=enonce, image=image, htmlQ=htmlQ, reponses=reponses, textInput=textInput)
    else:
        textInput=request.form.get("textInput")
        answers=[request.form.get(str(k))=="on" for k in range(len(q.questionSetList[setId-1][exerciceId-1].reponses))]
        dbM.registerAnswer(userId, setId, exerciceId-1, answers, textInput)
        return redirect(url_for("Exercice", exerciceId=exerciceId+1, setId=setId, userId=userId))

@app.route("/cours/<setId>/<exerciceId>", methods=["GET"])
def Cours(setId, exerciceId):
    exerciceId=int(exerciceId)
    setId=int(setId)
    userId=int(request.args.get("userId"))
    
    if not dbM.IdExists(userId):
        return render_template("message.html", error="Id n'existe pas, il faut recréer un compte depuis l'accueil")

    dbM.registerCours(userId, setId, exerciceId-1)
    (enonce, image, htmlC) = q.questionSetList[setId-1][exerciceId-1].GetCours()
    return render_template("cours.html", userId=userId, exerciceId=exerciceId, enonce=enonce, image=image, htmlC=htmlC)

def runApp(debug=False):
    if debug:
        app.run(host="0.0.0.0", threaded=True)
    else:
        serve(app, host="0.0.0.0", port=5000)

def resetDatabase():
    dbM.resetDatabase(q.MaxNumberOfQuestions())

def getDatabaseInfos():
    return dbM.getDatabaseInfos()

def getMaxNumberOfColumns():
    return q.MaxNumberOfQuestions()