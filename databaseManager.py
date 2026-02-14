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

def IdExists(studentName):
    with sqlite3.connect("database.db") as connexion:
        cursor=connexion.cursor()

        studentNames=cursor.execute(f"SELECT * FROM serie1 WHERE studentName = ?;", (studentName,))
        return studentNames.fetchall() != []

def registerAnswer(studentName, setId, exerciceId, answers, textInput):
    answer=textInput

    for k in range(len(answers)):
        if answers[k]:
            answer=(q.questionSetList[setId-1][exerciceId].reponses[k])
    
    with sqlite3.connect("database.db") as connexion:
        cursor=connexion.cursor()

        cursor.execute(f"UPDATE serie{setId} SET question{exerciceId+1}Answer=? WHERE studentName=?;", (answer, studentName))

        connexion.commit()

def registerCours(studentName, setId, exerciceId):
    with sqlite3.connect("database.db") as connexion:
        cursor=connexion.cursor()

        cursor.execute(f"UPDATE serie{setId} SET question{exerciceId+1}Lesson=? WHERE studentName=?;", (True, studentName))

        connexion.commit()

def resetDatabase():
    with open("database.db", "w"):
        pass

    with sqlite3.connect("database.db") as connexion:
        cursor=connexion.cursor()

        for k in range(len(q.questionSetList)):
            command=f"CREATE TABLE serie{k+1} (studentName VARCHAR(4) PRIMARY KEY, {",".join([f"question{n+1}Answer VARCHAR(50) DEFAULT \"\", question{n+1}Lesson BOOLEAN DEFAULT false" for n in range(len(q.questionSetList[k].questionsList))])});"
            cursor.execute(command)

        connexion.commit()

def getDatabaseInfos():
    with sqlite3.connect("database.db") as connexion:
        cursor=connexion.cursor()

        data=[cursor.execute(f"SELECT * FROM serie{k+1};").fetchall() for k in range(len(q.questionSetList))]
        
    return data

def checkDatabaseExists():
    if not "database.csv" in listdir():
        resetDatabase()

checkDatabaseExists()