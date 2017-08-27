import pymysql
import decimal

class DBConnect:
    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("A instance already exists!")

        self.dbhost = "localhost"
        self.dbuser = "admin"
        self.dbpass = "escape"
        self.database = "coin"

    def getConnection(self):
        return pymysql.connect(self.dbhost, self.dbuser, self.dbpass, self.database, charset='utf8')

    @classmethod
    def getInstance(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = DBConnect()
        return cls.INSTANCE

    def executeQuery(self, query, args):
        conn = self.getConnection()
        curs = conn.cursor()
        curs.execute(query, args)
        conn.commit()
        curs.close()
        conn.close()

    def selectQuery(self, query, args):
        conn = self.getConnection()
        curs = conn.cursor()
        curs.execute(query, args)
        result = curs.fetchall()
        curs.close()
        conn.close()
        return result
    #
    # def updateOrderBook(self, exchange, coin, bid, ask):
    #     for i in range(0,5) :
    #         curs.execute("""UPDATE ORDER_BOOK
    #                         SET TICK = %s
    #                           , QNTY = %s
    #                         WHERE IDX = %s AND BID_ASK = 'BID' AND EXCHANGE = %s AND COIN = %s
    #                      """, (bid['tick'][i] , bid['qnty'][i], i+1, exchange, coin))
    #
    #     for i in range(0,5) :
    #         curs.execute("""UPDATE ORDER_BOOK
    #                         SET TICK = %s
    #                           , QNTY = %s
    #                         WHERE IDX = %s AND BID_ASK = 'ASK' AND EXCHANGE = %s AND COIN = %s
    #                      """, (ask['tick'][i] , ask['qnty'][i], i+1, exchange, coin))