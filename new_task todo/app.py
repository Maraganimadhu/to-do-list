from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

tasks = []  # List to store tasks

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    subject = request.form.get("subject")
    description = request.form.get("description")
    if subject and description:
        tasks.append({"subject": subject, "description": description})
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["POST"])
def edit_task(task_id):
    new_subject = request.form.get("subject")
    new_description = request.form.get("description")
    if 0 <= task_id < len(tasks):
        tasks[task_id]["subject"] = new_subject
        tasks[task_id]["description"] = new_description
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return jsonify({"message": "Task deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
