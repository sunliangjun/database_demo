import time, datetime
import unittest
import yagmail
from case_run.HTMLTestReportCN import HTMLTestRunner


class SendReport(object):
    def set_up_yagmail(self, report):
        username = "liangjunsun2020@163.com"
        password = "AGRKMKPWAWADFLZD"
        yag = yagmail.SMTP(user=username, password=password, host="smtp.163.com")
        subject = "邮件主题"
        contents = "邮件正文"
        # 收件邮件列表
        receivername = ["582675682@qq.com"]
        yag.send(receivername, subject, contents, report)

    def test_report(self):
        test_dir = "D:\\pycharm\\workspace\\unittest_demo\\case_run"
        # suit = unittest.defaultTestLoader.discover(test_dir, pattern="unittest_case.py")
        suit = unittest.defaultTestLoader.discover(test_dir, pattern="try_case.py")
        now_time = time.strftime("%Y-%m-%d %H-%M-%S")
        html_report = "D:\\pycharm\\workspace\\unittest_demo\\case_report\\" + now_time + "result.html"
        with open(html_report, "wb") as f:
            runner = HTMLTestRunner(stream=f, title="测试报告", description="运行环境:win10，Firefox浏览器", verbosity=2)
            runner.run(suit)
        self.set_up_yagmail(html_report)

    # 运行
    def run(self):
        self.test_report()

    # def txt_try(self):
    #     txt_list = ["name", "sunliangjun", "123"]
    #     now_time = time.strftime("%Y-%m-%d %H-%M-%S")
    #     html_report = "D:\\pycharm\\workspace\\unittest_demo\\case_report\\" + now_time + ".txt"
    #     with open(html_report, "w") as f:
    #         for txt in txt_list:
    #             f.write(txt)


if __name__ == '__main__':
    send_report = SendReport()
    send_report.run()
    # today = datetime.datetime.now()
    # offset = datetime.timedelta(minutes=1)
    # re_date = (today+offset).strftime("%Y/%m/%d %H:%M:%S")
    # print(re_date)
    # send_report.txt_try()
