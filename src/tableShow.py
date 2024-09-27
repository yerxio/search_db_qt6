import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, result, headers, headers_2):
        super().__init__()
        uic.loadUi("../ui_files/T.ui", self)
        self.setWindowTitle("查询结果")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.tableWidget)

        if result:
            self.tableWidget.setColumnCount(len(headers))  # 设置列数为headers的长度
            self.tableWidget.setHorizontalHeaderLabels(headers)  # 使用headers作为表头


            if headers_2 != None:
                # 插入第二行并设置为headers_2
                self.tableWidget.insertRow(0)  # 在第一行插入空行
                for column_index, header_2 in enumerate(headers_2):
                    self.tableWidget.setItem(0, column_index, QTableWidgetItem(header_2))  # 设置第二行

            # 填充数据，从第二行开始
            for row_index, row_data in enumerate(result):
                if len(row_data) != len(headers):
                    print(f"Error: Row data length {len(row_data)} does not match headers length {len(headers)}.")
                    QMessageBox.warning(self, "警告", "数据长度不匹配，请检查数据源。")
                    continue

                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)
                for column_index, value in enumerate(row_data):
                    self.tableWidget.setItem(row_position, column_index, QTableWidgetItem(str(value)))

            # 自适应列和行
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.resizeColumnsToContents()

            # 设置标题行样式
            self.tableWidget.item(0, 0).setForeground(Qt.GlobalColor.white)  # 设置字体颜色
            self.tableWidget.item(0, 0).setBackground(Qt.GlobalColor.black)  # 设置背景颜色





if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 测试数据
    headers = ["DLpayAmount", "DLpayCount", "TGPayAccount", "USDTAccount", "YH", "accountStatus", "accountid", "activeTime", "agpayAccount", "aipayAccount", "alipayAccount", "bankname", "betCount", "betNeed", "betTotal", "boxcoin", "channel", "cloudpayAccount", "cloudpayRealName", "coin", "createTime", "createchannel", "creditCardNum", "dailyGameProfit", "defeatednum", "defeatedtime", "diamond", "empiricValue", "exchangedBoxCoin", "exchangedCoin", "from", "interactiveProps", "invitedrid", "kdouAccount", "kdouRealName", "lastLoadIp", "lastLoadTerrace", "losecnt", "lotteryDraw", "name", "nameOfCreditCardBelong", "payCount", "phone", "pid", "playCardNumber", "realName", "registerIp", "remark", "slipwayDues", "status", "statusName", "succeednum", "succeedtime", "suspendedlasttime", "todayPay", "todayStore", "topayAccount", "totalbet", "totalbettoday", "totalbetyestarday", "totalpay", "type", "typeName", "userLevelWhite", "vip", "wincnt", "xopayAccount", "xxpayAmount", "xxpayCount", "cardNumber", "closureReason", "closureRemark", "jetonNum", "operateRemark", "payAmount", "talkDuration", "talkRemark", "邀请人ID"]

    headers_2 = ["代理付费金额", "代理付费次数", "TGPay钱包", "USDT-TRC20账号", "开户银行", "账号状态", "游戏id",
                 "最后登陆时间", "agpay钱包", "支付宝账号", "开户支行", "betCount", "betNeed",
                 "betTotal", "boxcoin", "登录渠道", "云支付账号", "cloudpayRealName", "coin", "注册时间",
                 "登录渠道", "银行卡卡号", "dailyGameProfit", "提现成功次数", "提现失败次数", "提现失败金额",
                 "diamond", "empiricValue", "exchangedBoxCoin", "流动金币量", "from", "interactiveProps",
                 "invitedrid", "K豆钱包", "kdouRealName", "最后登陆IP", "lastLoadTerrace", "losecnt",
                 "lotteryDraw", "游戏昵称", "持卡人姓名", "线上付费次数", "手机号码", "pid", "playCardNumber",
                 "支付宝实名", "注册IP", "remark", "slipwayDues", "status", "账号状态", "提现成功金额",
                 "succeedtime", "suspendedlasttime", "todayPay", "todayStore", "topay钱包", "历史总打码",
                 "今日总打码", "totalbetyestarday", "线上付费金额", "type", "登录类型", "用户层级", "vip",
                 "wincnt", "xopay钱包", "xxpayAmount", "xxpayCount", "cardNumber", "closureReason",
                 "closureRemark", "jetonNum", "operateRemark", "payAmount", "talkDuration", "talkRemark",
                 "邀请人ID"]

    result = [(500, 10, None, None, None, 0, 4927817, '2023-08-26 18:49:05', None, None, None, None, 0, 0, 0, 0, 'IOS', '182*****871', None, 54, '2023-04-27 21:48:14', 'IOS', None, 0, 0, 0, 0, 0, 0, 0.54, '其他方式', 0, 0, None, None, '117.136.72.40', None, 0, 0, '花左杀', None, 0, '182*****871', None, 0, None, '117.136.72.253', None, 0, None, '正常【未被封停过】', 604, 6, 0, 0, None, None, 1550.54, 0.0, 0.0, 100, 0, '账号登录', None, 0, 0, None, 0, 0, 0, 0, None, 0, None, 0, 0, None, None)]

    window = MainWindow(result, headers, headers_2)
    window.show()
    sys.exit(app.exec())
