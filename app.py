from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

tasks = []

def process_text(input_text):
    """Apply simple text manipulations."""
    reversed_text = input_text[::-1]
    word_count = len(input_text.split())
    char_count = len(input_text)
    is_palindrome = "Yes" if input_text.lower() == input_text.lower()[::-1] else "No"

    return {
        "original": input_text,
        "reversed": reversed_text,
        "word_count": word_count,
        "char_count": char_count,
        "palindrome": is_palindrome
    }

@app.route("/", methods=["GET", "POST"])
def index():
    processed_text = None
    if request.method == "POST":
        task_content = request.form.get("task")
        if task_content:
            tasks.append(task_content)
            processed_text = process_text(task_content)  # Process text input
    return render_template("index.html", tasks=tasks, processed_text=processed_text)

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)