from flask import Flask, request, render_template, jsonify, redirect
import bdd
from data_console import DataConsole
from setup_logger import logger

app = Flask(__name__)
message = ''


@app.route('/admin/create_table')
def create_table():
    global message
    db_game = bdd.BDD()
    try:
        db_game.create_table()
        message = 'SUCCESS'
    except Exception as err:
        message = 'create table is failed'
        logger.error('create table is failed')
    db_game.__disconnect__()
    return redirect('/admin')


@app.route('/admin/insert_data')
def insert_data():
    global message
    db_game = bdd.BDD()
    try:
        data_console = DataConsole().data
        db_game.insert_data(data_console)
        logger.info('insert data is success')
        message = 'SUCCESS'
    except Exception as err:
        logger.error('Insert data is failed')
        message = 'ERROR'
    db_game.__disconnect__()
    return redirect('/admin')


@app.route("/console/<int:id_console>")
def single_page(id_console):
    logger.info(f'get single page for console id = {id_console}')
    try:
        db_game = bdd.BDD()
        data = db_game.select_from_db(id_console)
        db_game.__disconnect__()
    except:
        return redirect('/')
    return render_template('single.html', data=data)


@app.route('/')
def page_welcome():
    logger.info('welcome page')
    try:
        db_game = bdd.BDD()
        data = db_game.select_from_db()
        db_game.__disconnect__()
    except:
        return redirect('/admin')
    if len(data) == 0:
        return redirect('/admin')
    return render_template('index.html', data=data)


@app.route('/admin')
def page_admin():
    logger.info('welcome page admin')
    global message
    return render_template('admin.html', message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)
