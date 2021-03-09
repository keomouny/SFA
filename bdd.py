import psycopg2
import psycopg2.extras
import os
from dotenv import load_dotenv
from setup_logger import logger


class BDD():

    logger.info('Connection with postgress in database')
    load_dotenv()

    def __init__(self):
        self.query_specify = None
        self.mydb = psycopg2.connect(
            host=os.environ.get('POSTGRES_HOST'),
            dbname=os.environ.get('POSTGRES_DBNAME'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD'),
            sslmode="require"
        )

    def create_table(self):
        logger.info('create table console_game')
        try:
            self.query_specify = 'CREATE TABLE IF NOT EXISTS console_game (id SERIAL PRIMARY KEY NOT NULL, name VARCHAR (100), date_out INT, constructor_console VARCHAR (100), type_console VARCHAR(100));'
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(self.query_specify)
        except psycopg2.Error as err:
            logger.error(err)
            exit()

    def insert_data(self, query_plus):
        logger.info('insert data')
        self.query_specify = 'INSERT INTO console_game (name, date_out, constructor_console, type_console) VALUES (%s, %s, %s, %s)'
        try:
            self.mycursor = self.mydb.cursor()
            self.mycursor.executemany(self.query_specify, query_plus)
        except psycopg2.Error as err:
            logger.error(err)
            exit()

    def select_from_db(self, id_element=None):
        self.query_specify = 'SELECT * FROM console_game'
        if id_element != None:
            logger.info(f'select element by id : {id_element}')
            self.query_specify += f' WHERE id in ({id_element});'
            try:
                self.mycursor = self.mydb.cursor(
                    cursor_factory=psycopg2.extras.DictCursor)
                self.mycursor.execute(self.query_specify)
                result = self.mycursor.fetchone()
                return result
            except psycopg2.Error as err:
                logger.error(err)
                logger.error('error for get one element')
                exit()
        else:
            try:
                logger.info('select all element for welcome page')
                self.query_specify += ';'
                self.mycursor = self.mydb.cursor(
                    cursor_factory=psycopg2.extras.DictCursor)
                self.mycursor.execute(self.query_specify)
                result = self.mycursor.fetchall()
            except psycopg2.Error as err:
                logger.error(err)
                logger.error('error for get all elements in page welcome')
                exit()

        dict_result = []
        for i in result:
            dict_single_result = {}
            dict_single_result['id'] = i['id']
            dict_single_result['name'] = i['name']
            dict_single_result['date'] = i['date_out']
            dict_single_result['constructor'] = i['constructor_console']
            dict_single_result['type'] = i['type_console']
            dict_result.append(dict_single_result)
        return dict_result

    def __disconnect__(self):
        logger.info('disconnect from database')
        self.mydb.commit()
        self.mydb.close()
