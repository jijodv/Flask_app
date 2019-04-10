from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Balaji Vellaichamy',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 10, 2019'
    },
    {
        'author': 'Aaradhana',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 11, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/aara")
def aara():
    return render_template('aara.html', title='Aara')

if __name__ == "__main__":
    app.run(debug=True)
