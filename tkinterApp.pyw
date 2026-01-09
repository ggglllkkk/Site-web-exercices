import customtkinter as tk
import multiprocessing; multiprocessing.freeze_support
import socket
from app import runApp, resetDatabase

appProcess = multiprocessing.Process(target=runApp)

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

def changeAppStatus():
    global appProcess
    if __name__ == "__main__":
        if not appProcess.is_alive():
            appProcess = multiprocessing.Process(target=runApp)
            appProcess.start()

            runAppButton.configure(text="Stop Server")

            appAdressLabel.configure(state=tk.NORMAL)
            appAdressLabel.delete("1.0", tk.END)
            appAdressLabel.insert("1.0", f"Server is running on adress : {getLocalIP()}:5000")
            appAdressLabel.configure(state=tk.DISABLED)
        else:
            appProcess.terminate()

            runAppButton.configure(text="Start Server")

            appAdressLabel.configure(state=tk.NORMAL)
            appAdressLabel.delete("1.0", tk.END)
            appAdressLabel.insert("1.0", "Server not running")
            appAdressLabel.configure(state=tk.DISABLED)


window = tk.CTk()
window.geometry("310x100")

appAdressLabel = tk.CTkTextbox(window, height=25, width=300)
appAdressLabel.insert("1.0", "Server not running")
appAdressLabel.configure(state=tk.DISABLED)
appAdressLabel.pack()

runAppButton = tk.CTkButton(window, text="Start Server", command=changeAppStatus)
runAppButton.pack()

resetDatabaseButton = tk.CTkButton(window, text="Reset database", command=resetDatabase)
resetDatabaseButton.pack()

if __name__ == "__main__":
    multiprocessing.freeze_support()

    window.mainloop()