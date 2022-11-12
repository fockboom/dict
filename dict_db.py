import  pymysql
class Dictdata:
    def __init__(self):
        self.kwargs = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': 'xiaopet1',
            'database': 'dict_project',
            'charset': 'utf8',
        }
        self.db=pymysql.connect(**self.kwargs)
        self.cur=self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()