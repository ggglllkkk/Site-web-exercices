from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask("site bou", template_folder="templates", static_folder="static")

@app.route('/')
def Index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)