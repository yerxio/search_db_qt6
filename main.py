from src.Query_ import SelectorAc
import sys
from PyQt6 import QtWidgets, uic
from src.tableShow import MainWindow as TableShow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui_files/S.ui', self)  # 替换为你的 .ui 文件名
        self.Query = SelectorAc()
        self.tableW = None


        # 连接按钮点击事件
        self.queryButton.clicked.connect(self.query)

    def query(self):
        query_rid = self.queryData.text()
        if self.tableList.currentText() == '会员详单(无*, 远堪前数据)':
            result = self.Query.selectYkq(query_rid)
            headers = ["DLpayAmount", "DLpayCount", "TGPayAccount", "USDTAccount", "YH", "accountStatus", "accountid", "activeTime", "agpayAccount", "aipayAccount", "alipayAccount", "bankname", "betCount", "betNeed", "betTotal", "boxcoin", "channel", "cloudpayAccount", "cloudpayRealName", "coin", "createTime", "createchannel", "creditCardNum", "dailyGameProfit", "defeatednum", "defeatedtime", "diamond", "empiricValue", "exchangedBoxCoin", "exchangedCoin", "from", "interactiveProps", "invitedrid", "kdouAccount", "kdouRealName", "lastLoadIp", "lastLoadTerrace", "losecnt", "lotteryDraw", "name", "nameOfCreditCardBelong", "payCount", "phone", "pid", "playCardNumber", "realName", "registerIp", "remark", "slipwayDues", "status", "statusName", "succeednum", "succeedtime", "suspendedlasttime", "todayPay", "todayStore", "topayAccount", "totalbet", "totalbettoday", "totalbetyestarday", "totalpay", "type", "typeName", "userLevelWhite", "vip", "wincnt", "xopayAccount", "xxpayAmount", "xxpayCount", "cardNumber", "closureReason", "closureRemark", "jetonNum", "operateRemark", "payAmount", "talkDuration", "talkRemark"]
            headers_2 = ["代理付费金额", "代理付费次数", "TGPayAccount", "USDT-TRC20账号", "开户银行", "账号状态", "游戏id", "最后登陆时间", "agpay钱包", "aipay钱包", "支付宝账号", "开户支行", "历史总打码", "betNeed", "betTotal", "boxcoin", "登录渠道", "云支付账号", "cloudpayRealName", "coin", "注册时间", "登录渠道", "银行卡卡号", "每日游戏利润", "提现失败金额", "提现失败次数", "diamond", "empiricValue", "exchangedBoxCoin", "流动金币量", "from", "interactiveProps", "invitedrid", "K豆钱包", "kdouRealName", "最后登陆IP", "最后登陆时间", "losecnt", "lotteryDraw", "游戏昵称", "持卡人姓名", "线上付费次数", "手机号码", "pid", "playCardNumber", "支付宝实名", "注册IP", "remark", "slipwayDues", "状态", "状态名称", "提现成功金额", "succeedtime", "suspendedlasttime", "今日总打码", "todayStore", "topay钱包", "历史总打码", "今日总打码", "totalbetyestarday", "线上付费金额", "type", "登录类型", "userLevelWhite", "vip", "wincnt", "xopay钱包", "xxpayAmount", "xxpayCount", "cardNumber", "closureReason", "closureRemark", "jetonNum", "operateRemark", "payAmount", "talkDuration", "talkRemark"]

            # print(result)


        elif self.tableList.currentText() == '会员详单(带*)':
            result = self.Query.selectHyxd(query_rid)
            headers = ["DLpayAmount", "DLpayCount", "TGPayAccount", "USDTAccount", "YH", "accountStatus", "accountid", "activeTime", "agpayAccount", "aipayAccount", "alipayAccount", "bankname", "betCount", "betNeed", "betTotal", "boxcoin", "channel", "cloudpayAccount", "cloudpayRealName", "coin", "createTime", "createchannel", "creditCardNum", "dailyGameProfit", "defeatednum", "defeatedtime", "diamond", "empiricValue", "exchangedBoxCoin", "exchangedCoin", "from", "interactiveProps", "invitedrid", "kdouAccount", "kdouRealName", "lastLoadIp", "lastLoadTerrace", "losecnt", "lotteryDraw", "name", "nameOfCreditCardBelong", "payCount", "phone", "pid", "playCardNumber", "realName", "registerIp", "remark", "slipwayDues", "status", "statusName", "succeednum", "succeedtime", "suspendedlasttime", "todayPay", "todayStore", "topayAccount", "totalbet", "totalbettoday", "totalbetyestarday", "totalpay", "type", "typeName", "userLevelWhite", "vip", "wincnt", "xopayAccount", "xxpayAmount", "xxpayCount", "cardNumber", "closureReason", "closureRemark", "jetonNum", "operateRemark", "payAmount", "talkDuration", "talkRemark", "邀请人ID"]
            headers_2 = ["代理付费金额", "代理付费次数", "TGPay账号", "USDT-TRC20账号", "开户银行", "账号状态", "游戏id", "最后登陆时间", "agpay钱包", "aipay钱包", "支付宝账号", "开户支行", "betCount", "betNeed", "betTotal", "boxcoin", "登录渠道", "云支付账号", "cloudpayRealName", "coin", "注册时间", "登录渠道", "银行卡卡号", "dailyGameProfit", "提现失败金额", "提现失败次数", "diamond", "empiricValue", "exchangedBoxCoin", "流动金币量", "from", "interactiveProps", "invitedrid", "K豆钱包", "kdouRealName", "最后登陆IP", "lastLoadTerrace", "losecnt", "lotteryDraw", "游戏昵称", "持卡人姓名", "线上付费次数", "手机号码", "pid", "playCardNumber", "支付宝实名", "注册IP", "remark", "slipwayDues", "status", "账号状态", "提现成功金额", "succeedtime", "suspendedlasttime", "todayPay", "todayStore", "topay钱包", "历史总打码", "今日总打码", "totalbetyestarday", "线上付费金额", "type", "登录类型", "userLevelWhite", "vip", "wincnt", "xopay钱包", "xxpayAmount", "xxpayCount", "cardNumber", "closureReason", "closureRemark", "jetonNum", "operateRemark", "payAmount", "talkDuration", "talkRemark", "邀请人ID"]

            # print(result)

        elif self.tableList.currentText() == '邀请榜':
            result = self.Query.selectYqb(query_rid)
            headers = ["名次", "邀请人ID", "级别", "直属人数", "非直属人数", "今日邀请人数", "受邀充值总额", "今日受邀充值额", "受邀抽水总奖", "非直属抽水总奖", "待领取金额"]
            headers_2 = None
            # print(result)

        elif self.tableList.currentText() == '提现申请':
            result = self.Query.selectYTxsq(query_rid)
            headers = ["account", "accounttype", "bankcode", "bankname", "banktypename", "canbesign", "cashask", "cashexport", "cashfee", "channel", "createtime", "exchange", "exchangeCashexport", "gamerolename", "isadmin", "isfirst", "issys", "operatedesc", "operatedescag", "operator", "orderid", "providerid", "providername", "realname", "rid", "states", "submitorder", "sysremark", "updatetime", "updatetime_datetime"]
            headers_2 = ["账户号码", "账户类型", "bankcode", "开户行信息", "商户名", "canbesign", "提现金额", "出款金额", "提现费率", "登录渠道", "申请时间", "汇率", "出款U", "游戏ID", "isadmin", "isfirst", "issys", "工单处理", "操作人员备注", "操作人员", "订单ID", "providerid", "商户名", "真实姓名", "游戏ID", "状态更新时间", "当前状态", "submitorder", "sysremark", "状态更新时间", "updatetime_datetime"]

            # print(result)
        elif self.tableList.currentText() == '线上充值':
            result = self.Query.selectXscz(query_rid)
            headers = ["adminoperator", "channel", "createtime", "orderID", "payCoding", "payDetailType", "payOrder",
                         "paySpeciesMess", "payType", "payTypeMess", "paytime", "peratorstate", "price", "remark",
                         "rid", "state", "statemess", "updatetime"]
            headers_2 = ["adminoperator", "会员渠道", "创建时间", "订单号", "支付编码", "payDetailType", "payOrder",
                         "支付方式", "payType", "商户", "支付时间", "peratorstate", "金额", "备注",
                         "游戏号", "状态", "statemess", "更新时间"]
            # print(result)

        elif self.tableList.currentText() == '线下充值':
            result = self.Query.selectXxcz(query_rid)
            headers = ["adminid", "adminname", "channel", "offlinepayid", "order", "price", "remark", "rid", "status", "time", "type", "typenum"]

            headers_2 = ["操作人员", "adminname", "channel", "充值id", "order", "金额", "备注", "游戏ID", "status", "充值时间", "类型", "typenum"]
            # print(result)


        else:
            print("无效的表名")
            return

        # 显示结果
        if result:
            self.tableW = TableShow(result, headers, headers_2)
            self.tableW.show()
        else:
            QtWidgets.QMessageBox.warning(self, '提示', '没有查询到结果')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
