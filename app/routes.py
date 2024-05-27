from flask import redirect, render_template, url_for, request
from app import app


dp = ['1', '2', '3', '4', '5', '6']


@app.route('/index/')
@app.route('/')
def index():
    return render_template('base.html', tasks=dp)


@app.route('/add/', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        dp.append(task)
        return redirect(url_for('index'))
    return render_template('add_task.html')


@app.route('/delete/', methods=['GET', 'POST'])
def delete_task():
    if request.method == 'POST':
        task = request.form.get('task')
        dp.remove(task)
        return redirect(url_for('index'))
    return render_template('base.html', tasks=dp)
