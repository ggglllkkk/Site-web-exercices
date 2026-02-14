import sqlite3
from os import getcwd, listdir
from threading import Lock
import questions as q

cwd = getcwd()
print(cwd)

def registerNew(studentName):
    with sqlite3.connect("database.db") as connexion:
        cursor=connexion.cursor()

        for k in range(len(q.questionSetList)):
            cursor.execute(f"INSERT INTO serie{k+1} (studentName) VALUES (?);", (studentName,))

        connexion.commit()

def IdExists(username):
    with sqlite3.connect("database.db") as connexion:
        cursor=connexion.cursor()

        studentNames=cursor.execute(f"SELECT * FROM serie1 WHERE studentName = ?;", (username,))
        return studentNames.fetchall() != []

def registerAnswer(username, setId, exerciceId, answers, textInput):
    answer=textInput

    for k in range(len(answers)):
        if answers[k]:
            answer=(q.questionSetList[setId-1][exerciceId].reponses[k])
    
    with sqlite3.connect("database.db") as connexion:
        cursor=connexion.cursor()

        cursor.execute(f"UPDATE serie{setId} SET question{exerciceId}=? WHERE studentName=?;", (answer, username))

        connexion.commit()

def registerCours(userId, setId, exerciceId):
    with open(cwd+"/database.csv", "r") as f:
        a=f.readlines()

    curr=a[(userId-1)*len(q.questionSetList)+setId].split(",")
    curr[exerciceId*2+3]="X"
    a[(userId-1)*len(q.questionSetList)+setId]=",".join(curr)

    with open(cwd+"/database.csv", "w") as f:
        f.write("".join(a))

def resetDatabase():
    with open("database.db", "w"):
        pass

    with sqlite3.connect("database.db") as connexion:
        cursor=connexion.cursor()

        for k in range(len(q.questionSetList)):
            command=f"CREATE TABLE serie{k+1} (studentName VARCHAR(4) PRIMARY KEY, {",".join([f"question{n+1}Answer VARCHAR(50), question{n+1}Lesson BOOLEAN DEFAULTS false" for n in range(len(q.questionSetList[k].questionsList))])});"
            cursor.execute(command)

        connexion.commit()

def getDatabaseInfos():
    with open(cwd+"/database.csv", "r") as f:
        a=f.readlines()

    a=[k.rstrip().split(",") for k in a[1:]]
        
    return a

def checkDatabaseExists():
    if not "database.csv" in listdir():
        resetDatabase()

checkDatabaseExists()