from flask import Flask, render_template, request
from helpers import diary

app: Flask = Flask(__name__)

diary_list: list[diary] = []
diary_count: int = 1

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/create-diary', methods=["GET", "POST"])
def create_diary():
    if request.method == "POST":
        global diary_list
        global diary_count
        
        title: str = request.form['title']
        genre: str = request.form['genre']
        review: str = request.form['review']
        
        if title == '':
            return render_template("create-diary.html")
        
        new_diary: diary = diary(diary_count, title, genre, review) 
        diary_list.append(new_diary)

        diary_count += 1

        return render_template("success.html", title=title, genre=genre, review=review) 
    
    if request.method == "GET":
        return render_template("create-diary.html")
    
    return render_template("create-diary.html")

@app.route('/view-diary-list')
def view_diary_list():
    return render_template('view-list.html', diary_list=diary_list)

if __name__ == '__main__':
    app.run(debug=True)