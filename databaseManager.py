from sqlite3 import *
import questions as q

def registerNew():
    with open("database.csv", "r") as f:
        a=f.readlines()
        if len(a)!=1:
            lastId=int(a[-1].rstrip().split(",")[0])
        else:
            lastId=0
    with open("database.csv", "w") as f:
        f.write("".join(a)+"\n"+str(lastId+1)+",,"*(len(q.questionsList)))
    return lastId+1

def IdExists(userId):
    with open("database.csv", "r") as f:
        maxId=len(f.readlines())-1
    return 1<=int(userId)<=int(maxId)

def registerAnswer(userId, exerciceId, answers, textInput):
    realAnswers=[]
    if textInput!=None:
        realAnswers.append("\""+textInput+"\"")
    for k in range(len(answers)):
        if answers[k]:
            realAnswers.append(q.questionsList[exerciceId].reponses[k])

    with open("database.csv", "r") as f:
        a=f.readlines()
    with open("database.csv", "w") as f:
        curr=a[userId].rstrip().split(",")
        curr[exerciceId*2+1]=";".join(realAnswers)

        a[userId]=",".join(curr)
        f.write("".join(a))

def registerCours(userId, exerciceId):
    with open("database.csv", "r") as f:
        a=f.readlines()
    with open("database.csv", "w") as f:
        curr=a[userId].rstrip().split(",")
        curr[(exerciceId+1)*2]="X"

        a[userId]=",".join(curr)
        f.write("".join(a))

def resetDatabase(numberOfColumns):
    a=open("database.csv", "w")
    a.close()

    with open("database.csv", "w") as f:
        f.write("userId,"+",".join(["Reponse "+str(k+1)+", Cours lu "+str(k+1) for k in range(numberOfColumns)]))