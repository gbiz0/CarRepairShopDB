const electron = require("electron");
const url = require("url");
const path = require("path");

const { PythonShell } = require("python-shell");
const serverShell = PythonShell.run("src/main.py", { mode: "text" }, (err, results) => {
    if (err)
        throw err;
    
    console.log(results);
});

const { app, BrowserWindow } = electron;

let mainWindow;
app.on( "ready", () => {
    setTimeout(() => {
        mainWindow = new BrowserWindow({ webPreferences: { nodeIntegration: true }});
        
        mainWindow.setMenuBarVisibility(false);
        mainWindow.loadURL("http://127.0.0.1:3001/");
        
        mainWindow.on("closed", () => {
            mainWindow = null;
            serverShell.childProcess.kill("SIGINT");
            app.quit()
        });
    }, 2000);
});
