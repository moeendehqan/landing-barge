from flask import Flask, render_template, redirect, url_for,send_from_directory


app = Flask(__name__)

lst = [
    {'title':'جرائم', 'content':'1.html' , 'route':'جرائم', 'date':'2024-01-17', 'category':'قوانین', 'image':"Law-of-tax-crimes.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blogs')
def blogs():
    return render_template('blogs.html', lst=lst)

@app.route('/blog/<route>')
def blog(route):
    target_dic = filter(lambda item: item['route'] == route, lst)
    result = next(target_dic, None)
    if result:
        return render_template('blog.html', dic=result)
    return redirect(url_for('blogs'))

@app.route('/robots.txt')
def robots_txt():
    return send_from_directory(app.static_folder, 'robots.txt')


if __name__ == '__main__':
    app.run(debug=True)
