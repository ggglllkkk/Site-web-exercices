from cx_Freeze import setup, Executable

exe = [Executable("tkinterApp.py", target_name="app.exe")] #, base="gui")]
build_exe_options = {"include_files": ["static", "templates"]}

# On appelle la fonction setup
setup(
    name = "Exercices website",
    version = "1",
    description = "Exercices website",
    executables = exe,
    options={"build_exe": build_exe_options},
)