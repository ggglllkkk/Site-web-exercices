import customtkinter as ctk
import multiprocessing; multiprocessing.freeze_support
import socket
from app import runApp, resetDatabase, getDatabaseInfos, getMaxNumberOfColumns

appProcess = None
databaseStatus = False
resetDatabaseStatus = False

def resetDatabaseCheck():
    global resetDatabaseStatus

    if not resetDatabaseStatus:
        resetDatabaseButton.configure(fg_color="red", hover_color="brown", text="Press to validate entry")
        resetDatabaseEntry.grid(row=3)
    else:
        if resetDatabaseEntry.get() == "confirm":
            resetDatabase()
            updateDatabase()

        resetDatabaseButton.configure(fg_color=runAppButton.cget("fg_color"), hover_color=runAppButton.cget("hover_color"), text="Reset database")
        resetDatabaseEntry.grid_forget()
        resetDatabaseEntry.delete(0, ctk.END)
        resetDatabaseEntry._activate_placeholder()
    
    resetDatabaseStatus = not resetDatabaseStatus

def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def changeAppStatus(isWindowClosed=False):
    global appProcess

    if __name__ == "__main__":
        if appProcess == None or not appProcess.is_alive():
            if isWindowClosed: return

            appProcess = multiprocessing.Process(target=runApp, args=(False,))
            appProcess.start()

            runAppButton.configure(text="Stop Server")

            appAdressLabel.configure(state=ctk.NORMAL)
            appAdressLabel.delete("1.0", ctk.END)
            appAdressLabel.insert("1.0", f"Server is running on adress : {getLocalIP()}:5000")
            appAdressLabel.configure(state=ctk.DISABLED)
        else:
            appProcess.terminate()
            appProcess.join()
            appProcess=None

            if isWindowClosed: return

            runAppButton.configure(text="Start Server")

            appAdressLabel.configure(state=ctk.NORMAL)
            appAdressLabel.delete("1.0", ctk.END)
            appAdressLabel.insert("1.0", "Server not running")
            appAdressLabel.configure(state=ctk.DISABLED)

def changeDatabaseStatus():
    global databaseStatus

    databaseStatus = not databaseStatus

    if databaseStatus:
        updateDatabase()

        databaseFrame.grid(row=5, sticky="nsew")
        showDatabaseButton.configure(text="Hide database")
        updateDatabaseButton.grid(row=6)
    else:
        showDatabaseButton.configure(text="Show database")
        updateDatabaseButton.grid_forget()
        databaseFrame.grid_forget()

def updateDatabase():
    bgColors=["red", "green"]

    for widget in databaseFrame.winfo_children():
        widget.destroy()

    databaseInfo = getDatabaseInfos()

    temp=["userId", "setId"]+list(range(1, getMaxNumberOfColumns()))
    for n in range(len(temp)):
        a=ctk.CTkFrame(databaseFrame)
        b=ctk.CTkLabel(a, text=temp[n], padx=5)
        b.pack(padx=1, pady=1)
        a.grid(row=0, column=n)

    for k in range(len(databaseInfo)):
        userIdLabel=ctk.CTkLabel(databaseFrame, text=databaseInfo[k][0], padx=5)
        userIdLabel.grid(row=k+1, column=0)
        setIdLabel=ctk.CTkLabel(databaseFrame, text=databaseInfo[k][1], padx=5)
        setIdLabel.grid(row=k+1, column=1)

        for n in range(2, len(databaseInfo[k]), 2):
            if databaseInfo[k][n] != "":
                a=ctk.CTkFrame(databaseFrame)
                b=ctk.CTkLabel(a, text=databaseInfo[k][n], padx=5, bg_color=bgColors[databaseInfo[k][n+1]=="X"], corner_radius=0)
            
                b.pack(padx=1, pady=1)
                a.grid(row=k+1, column=n//2+1)


window = ctk.CTk()
window.title="App"
window.columnconfigure(0, weight=1)
window.rowconfigure(5, weight=1)


appAdressLabel = ctk.CTkTextbox(window, height=25, width=300)
appAdressLabel.insert("1.0", "Server not running")
appAdressLabel.configure(state=ctk.DISABLED)
appAdressLabel.grid(row=0)

runAppButton = ctk.CTkButton(window, text="Start Server", command=changeAppStatus)
runAppButton.grid(row=1)

resetDatabaseButton = ctk.CTkButton(window, text="Reset database", command=resetDatabaseCheck)
resetDatabaseButton.grid(row=2)

resetDatabaseEntry = ctk.CTkEntry(window, placeholder_text="\"confirm\" to confirm")

showDatabaseButton = ctk.CTkButton(window, text="Show database", command=changeDatabaseStatus)
showDatabaseButton.grid(row=4)

updateDatabaseButton = ctk.CTkButton(window, text="Update database", command=updateDatabase)

databaseFrame=ctk.CTkScrollableFrame(window)


if __name__ == "__main__":
    multiprocessing.freeze_support()

    window.mainloop()
    changeAppStatus(True)