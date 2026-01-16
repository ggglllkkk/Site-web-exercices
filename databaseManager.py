from sqlite3 import *
from os import getcwd
import questions as q

cwd = getcwd()
print(cwd)

def registerNew():
    with open(cwd+"/database.csv", "r") as f:
        a=f.readlines()
        if len(a)!=1:
            lastId=(len(a)-1)//len(q.questionSetList)
        else:
            lastId=0
    with open(cwd+"/database.csv", "w") as f:
        f.write("".join(a)+"\n")
        f.write(str(lastId+1)+",0"+",,"*(len(q.questionSetList[0])))
        print(len(q.questionSetList))
        for k in range(1, len(q.questionSetList)):
            f.write("\n"+","+str(k+1)+",,"*(len(q.questionSetList[k])))
    return lastId+1

def IdExists(userId):
    try:
        with open(cwd+"/database.csv", "r") as f:
            maxId=(len(f.readlines())-1)//len(q.questionSetList)
        return 1<=int(userId)<=int(maxId)
    except:
        return False

def registerAnswer(userId, setId, exerciceId, answers, textInput):
    realAnswers=[]
    if textInput!=None:
        realAnswers.append("\""+textInput+"\"")
    for k in range(len(answers)):
        if answers[k]:
            realAnswers.append(q.questionSetList[setId-1][exerciceId].reponses[k])

    with open(cwd+"/database.csv", "r") as f:
        a=f.readlines()

    curr=a[(userId-1)*len(q.questionSetList)+setId].split(",")
    curr[exerciceId*2+2]=";".join(realAnswers)
    a[(userId-1)*len(q.questionSetList)+setId]=",".join(curr)
    
    with open(cwd+"/database.csv", "w") as f:
        f.write("".join(a))

def registerCours(userId, setId, exerciceId):
    with open(cwd+"/database.csv", "r") as f:
        a=f.readlines()
    
    curr=a[(userId-1)*len(q.questionSetList)+setId].split(",")
    print(curr)
    curr[exerciceId*2+3]="X"
    a[(userId-1)*len(q.questionSetList)+setId]=",".join(curr)
    
    with open(cwd+"/database.csv", "w") as f:
        f.write("".join(a))

def resetDatabase(maxNumberOfColumns):
    a=open(cwd+"/database.csv", "w")
    a.close()

    with open(cwd+"/database.csv", "w") as f:
        f.write("userId,setId,"+",".join(["Reponse "+str(k+1)+", Cours lu "+str(k+1) for k in range(maxNumberOfColumns)]))