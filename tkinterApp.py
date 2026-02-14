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

            appProcess = multiprocessing.Process(target=runApp, args=(True,))
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

        databaseCanvasFrame.grid(row=5, sticky="nswe")
        showDatabaseButton.configure(text="Hide database")
        updateDatabaseButton.grid(row=6)
    else:
        showDatabaseButton.configure(text="Show database")
        updateDatabaseButton.grid_forget()
        databaseCanvasFrame.grid_forget()

def updateDatabase():
    bgColors=["red", "green"]

    for widget in databaseFrame.winfo_children():
        widget.destroy()

    databaseInfo = getDatabaseInfos()

    temp=["studentName", "setId"]+list(range(1, getMaxNumberOfColumns()+1))
    for n in range(len(temp)):
        a=ctk.CTkFrame(databaseFrame)
        b=ctk.CTkLabel(a, text=temp[n], padx=5)
        b.pack(padx=1, pady=1, fill="both", expand=True)
        a.grid(row=0, column=n, sticky="nswe")

    for k in range(len(databaseInfo[0])):
        studentNameLabel=ctk.CTkLabel(databaseFrame, text=databaseInfo[0][k][0], padx=5)
        studentNameLabel.grid(row=k*len(databaseInfo)+1, column=0)

        for n in range(len(databaseInfo)):
            setIdLabel=ctk.CTkLabel(databaseFrame, text=str(n+1), padx=5)
            setIdLabel.grid(row=k*len(databaseInfo)+n+1, column=1)

            for i in range((len(databaseInfo[n][0])-1)//2):
                if databaseInfo[n][k][i*2+1] != "":
                    a=ctk.CTkFrame(databaseFrame)
                    b=ctk.CTkLabel(a, text=databaseInfo[n][k][i*2+1], padx=5, bg_color=bgColors[databaseInfo[n][k][i*2+2]], corner_radius=0)

                    b.pack(padx=1, pady=1, fill="both", expand=True)
                    a.grid(row=k*len(databaseInfo)+n+1, column=i+2, sticky="nswe")
    
    databaseFrame.update_idletasks()
    databaseCanvas.configure(scrollregion=databaseCanvas.bbox("all"))

def onFrameConfigure(event):
    databaseCanvas.configure(scrollregion=databaseCanvas.bbox("all"))

def onCanvasConfigure(event):
    databaseCanvas.itemconfig(databaseFrameWindow, width=event.width)

def onMouseWheel(event):
    databaseCanvas.yview_scroll(int(-1*(event.delta/120)), "units")


window = ctk.CTk()
window.title="App"
window.columnconfigure(0, weight=1)
window.rowconfigure(5, weight=1)

bgColor=window.cget("background")


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


databaseCanvasFrame=ctk.CTkFrame(window, fg_color=bgColor, border_width=0)
databaseCanvasFrame.columnconfigure(0, weight=1)
databaseCanvasFrame.rowconfigure(0, weight=1)

databaseCanvas=ctk.CTkCanvas(databaseCanvasFrame, bg=bgColor, highlightthickness=0)
databaseCanvas.grid(row=0, column=0, sticky="nswe")

databaseFrame=ctk.CTkFrame(databaseCanvasFrame)
databaseFrameWindow=databaseCanvas.create_window((0,0), window=databaseFrame, anchor="nw")

vsb=ctk.CTkScrollbar(databaseCanvasFrame, orientation="vertical", command=databaseCanvas.yview)
vsb.grid(row=0, column=1, sticky="ns")

hsb=ctk.CTkScrollbar(databaseCanvasFrame, orientation="horizontal", command=databaseCanvas.xview)
hsb.grid(row=1, column=0, sticky="we")

databaseCanvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
window.bind("<MouseWheel>", onMouseWheel)
databaseFrame.bind("<Configure>", onFrameConfigure)


if __name__ == "__main__":
    multiprocessing.freeze_support()

    window.mainloop()
    changeAppStatus(True)