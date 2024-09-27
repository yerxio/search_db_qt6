import sqlite3

class SelectorAc:
    def __init__(self):
        self.conn = sqlite3.connect(r'E:\平台分析\盛世\数据处理_db文件\盛世.db')

    def selectYkq(self, accountid):
        cursor = self.conn.cursor()  # 创建游标
        cursor.execute("SELECT * FROM `盛世娱乐会员详单_远堪前` WHERE accountid = ?", (accountid,))
        rows = cursor.fetchall()
        cursor.close()  # 关闭游标
        return rows

    def selectHyxd(self, accountid):
        cursor = self.conn.cursor()  # 创建游标
        cursor.execute("SELECT * FROM `盛世娱乐会员详单` WHERE accountid = ?", (accountid,))
        rows = cursor.fetchall()
        cursor.close()  # 关闭游标
        return rows

    def selectYqb(self, accountid):
        cursor = self.conn.cursor()  # 创建游标
        cursor.execute("SELECT * FROM `盛世娱乐代理邀请榜` WHERE `邀请人ID` = ?", (accountid,))
        rows = cursor.fetchall()
        cursor.close()  # 关闭游标
        return rows

    def selectYTxsq(self, accountid):
        cursor = self.conn.cursor()  # 创建游标
        cursor.execute("SELECT * FROM `盛世娱乐提现申请` WHERE `rid` = ?", (accountid,))
        rows = cursor.fetchall()
        cursor.close()  # 关闭游标
        return rows

    def selectXscz(self, accountid):
        cursor = self.conn.cursor()  # 创建游标
        cursor.execute("SELECT * FROM `线上充值查询` WHERE `rid` = ?", (accountid,))
        rows = cursor.fetchall()
        cursor.close()  # 关闭游标
        return rows

    def selectXxcz(self, accountid):
        cursor = self.conn.cursor()  # 创建游标
        cursor.execute("SELECT * FROM `线下充值查询` WHERE `rid` = ?", (accountid,))
        rows = cursor.fetchall()
        cursor.close()  # 关闭游标
        return rows

    def __del__(self):
        self.conn.close()  # 确保连接在对象销毁时关闭


if __name__ == '__main__':
    selector = SelectorAc()
    selector.selectYqb(1000001)
