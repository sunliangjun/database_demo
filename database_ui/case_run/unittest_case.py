import unittest, time, datetime
from database_ui.case_run.position_elements import PositionElements as PE
from database_ui.case_run.read_data import ReadData as RD
from database_ui.case_elements.operation_information import DatabaseInformation as DI
from database_ui.case_elements.operation_information import OperationInformation as OI


class unittestCase(unittest.TestCase):
    # 测试用例执行前执行
    @classmethod
    def setUpClass(cls) -> None:
        PE.start_url(PE)

    # 测试用例执行完之后执行
    @classmethod
    def tearDownClass(cls) -> None:
        PE.driver_close(PE)

    # 读取数据
    def read(self, path):
        return RD.read(RD, path)

    # 定位元素
    def position_element(self, key, value):
        element = PE.url_element(PE, key, value)
        return element

    # 断言
    def asserequal(self, result, expected_result):
        report = self.assertEqual(result, expected_result)
        return report

    # 添加配置信息
    def test_1_configure_imormation(self):
        path = "D:/pycharm/workspace/unittest_demo/case_data/configure_information.json"
        # 读取数据
        message = self.read(path)
        # print(message)
        # 系统用户名
        self.position_element("id", "id").send_keys(message["system_name"])
        # 系统密码
        self.position_element("id", "id").send_keys(message["system_password"])
        # 安装路劲
        self.position_element("id", "id").send_keys(message["path"])
        # 程序名称
        self.position_element("id", "id").send_keys(message["program_name"])
        # 绑定命令
        self.position_element("id", "id").send_keys(message["bind_command"])
        self.position_element("id", "id").click()
        # 判断数据是否添加成功
        # 无误添加配置信息后的标识
        # 判断断言结果（1是获得的结果，2是预期结果）
        # self.assertEqual(1, 2)

    # 开启监控
    def test_2_open_monitor(self):
        # 点击开启监控
        self.position_element("id", "id").click()
        # 读取数据
        path = "D:/pycharm/workspace/unittest_demo/case_data/configure_information.json"
        message = self.read(path)
        # 定位输入用户界面，是frame还是alert
        self.position_element("", "").send_keys(message["user"])
        self.position_element("", "").send_keys(message["password"])
        self.position_element("", "").click()
        # 判断登录是否成功
        # 成功登录后的标识
        # 判断断言结果

    # 设定时间和间隔时间
    def test_3_setup_time(self):
        """
        #时间加0.5天
        offset = datetime.timedelta(days=0.5)
        #时间加0.5小时
        offset = datetime.timedelta(hours=0.5)
        #时间加1分钟
        offset = datetime.timedelta(minutes=1)
        #时间加1秒钟
        offset = datetime.timedelta(seconds=1)
        :return:
        """
        # 将开始时间设置为当前时间的后一分钟
        now_time = datetime.datetime.now()
        offset = datetime.timedelta(minutes=1)
        input_time = (now_time + offset).strftime("%Y/%m/%d %H:%M:%S")
        # 开始时间属性值，开始时间，时间间隔属性、属性值、时间间隔(默认设置为10秒)，按钮属性和属性值
        DI.time_task(DI, "id", input_time, "id", "id", 10, "id", "id")

    # 下载文件
    def test_4_download_database_file(self):
        # 判断里面是否有数据
        flag = self.position_element("id", "id")
        # 定位复选框然后点击
        if len(flag) != 0:
            pass
        # 点击下载
        else:
            DI.download_file(DI, "id", "id")

    # 删除文件
    def test_5_delete_database_file(self):
        flag = self.position_element("id", "id")
        if len(flag) != 0:
            pass
        # 点击删除
        else:
            DI.delete_file(DI, "ID", "ID")

    # 查看历史信息
    def test_6_show_history_message(self):
        # 点击查看历史
        self.position_element("id", "id").click()
        # 输入开始和结束时间（假定开始时间要在结束时间之前，先试用一种正确的输入方式）
        OI.time_task(OI, "ID", "2020/09/06 11:12:13", "id", "2020/09/07 12:13:13")
        OI.system_information(OI, "ID", "ID", "ID", "ID")
        OI.service_refresh(OI, "ID", "ID")

    # 查看当前信息
    def test_7_show_now_message(self):
        self.position_element("id", "id").click()
        # 如果可以选择开始时间和结束时间就选择
        OI.time_task(OI, "ID", "2020/09/06 11:12:13", "id", "2020/09/07 12:13:13")
        OI.system_information(OI, "ID", "ID", "ID", "ID")
        OI.service_refresh(OI, "ID", "ID")

    # 不选择时间选择服务器查看信息
    def test_8_no_time_message(self):
        # 服务器下拉框属性和属性值，按钮属性和属性值
        OI.system_information(OI, "ID", "ID", "ID", "ID")
        OI.service_refresh(OI, "ID", "ID")


if __name__ == '__main__':
    unit = unittestCase()
    unit.test_1_configure_imormation()
