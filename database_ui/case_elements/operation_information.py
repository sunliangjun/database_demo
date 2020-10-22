from database_ui.case_run.position_elements import PositionElements as PE


# 系统资源信息采集
class OperationInformation(object):
    # 时间设置
    def time_task(self, start_element, start_time, end_element, end_time):
        PE.input_time(PE, start_element, start_time)
        PE.input_time(PE, end_element, end_time)

    # 下拉框选择服务器
    def system_information(self, element_key, value, type_key, type_value):
        # 服务器选择
        PE.select_element(PE, element_key, value, type_key, type_value)

    # 刷新纪录/当前信息/历史信息
    def service_refresh(self, element_key, value):
        PE.url_element(PE, element_key, value).click()


# 数据库节点设置
class DatabaseInformation(object):
    def time_task(self, element_key, start_time, key, value, time_interval, button_key, button_value):
        # 开始时间
        PE.input_time(PE, element_key, start_time)
        # 间隔时间
        PE.url_element(PE, key, value).send_keys(time_interval)
        # 确定
        PE.url_element(PE, button_key, button_value).click()

    def download_file(self, element_key, value):
        # 选中下载文件/删除文件，传入index作为要下载文件的标识
        PE.url_element(PE, element_key, value).click()

    # 保存下载文件
    def save_file(self, element_key, value):
        # 下载
        PE.download_file(PE, element_key, value)

    # 删除文件
    def delete_file(self, element_key, value):
        PE.url_element(PE, element_key, value).click()
