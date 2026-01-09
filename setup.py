from cx_Freeze import setup, Executable

build_exe_options = {"include_files": ["static", "templates"]}

# On appelle la fonction setup
setup(
    name = "Site web exercices",
    version = "1",
    description = "Site web mesurant des réponses à des exercices ainsi que la fréquence de consultation du cours.",
    executables = [Executable("tkinterApp.pyw")],
    options={"build_exe": build_exe_options},
)
