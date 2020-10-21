from selenium import webdriver
import time
import os
from selenium.webdriver.support.select import Select
from pykeyboard import PyKeyboard


class PositionElements(object):

    # 初始地址
    def start_url(self):
        fp = webdriver.FirefoxProfile()
        # 参数2为自定义下载文件路径，0是下载到默认路径
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.manager.showhenStarting", True)
        # 给定下载的绝对路径
        fp.set_preference("browser.download.dir", "D:\\pycharm\\workspace\\unittest_demo\\download")
        # 下载文件类型
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "binary/octet-stream")  # 下载文件类型
        self.driver = webdriver.Firefox(firefox_profile=fp)

    def get_url(self, url):
        self.driver.get(url)

    # 文件下载
    def download_file(self, element_key, value):
        self.url_element(element_key, value).click()
        k = PyKeyboard()
        # 使用Table键定位到弹出框的保存文件按钮，n=2按两次
        k.tap_key(k.tab_key, n=2)
        # 模拟键盘输入字符串
        # k.type_string("hello worlld")
        # Enter按键
        k.tap_key(k.enter_key)

    # 八种定位方式
    def url_element(self, element_key, value):
        element = None
        if element_key == "id":
            element = self.driver.find_element_by_id(value)
        elif element_key == "class":
            element = self.driver.find_element_by_class_name(value)
        elif element_key == "css":
            element = self.driver.find_element_by_css_selector(value)
        elif element_key == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif element_key == "name":
            element = self.driver.find_element_by_name(value)
        elif element_key == "tag_name":
            element = self.driver.find_element_by_tag_name(value)
        elif element_key == "link_text":
            element = self.driver.find_element_by_tag_name(value)
        elif element_key == "partial_link_text":
            element = self.driver.find_element_by_partial_link_text(value)
        return element

    # 八种组定位方式,返回一个元素列表
    def url_elements(self, element_key, value):
        element = None
        if element_key == "id":
            element = self.driver.find_elements_by_id(value)
        elif element_key == "class":
            element = self.driver.find_elements_by_class_name(value)
        elif element_key == "css":
            element = self.driver.find_elements_by_css_selector(value)
        elif element_key == "xpath":
            element = self.driver.find_elements_by_xpath(value)
        elif element_key == "name":
            element = self.driver.find_elements_by_name(value)
        elif element_key == "tag_name":
            element = self.driver.find_elements_by_tag_name(value)
        elif element_key == "link_text":
            element = self.driver.find_elements_by_tag_name(value)
        elif element_key == "partial_link_text":
            element = self.driver.find_elements_by_partial_link_text(value)
        return element

    # iframe表单
    def url_ifrme(self, element_key, value):
        if element_key == "id":
            self.driver.switch_to.frame(value)
        else:
            element = self.url_element(element_key, value)
            self.driver.switch_to.frame(element)

    # 截图
    def get_screenshot(self):
        image = self.driver.get_screenshot_as_png()
        os.chdir("D:/pycharm/workspace/unittest_demo/report_image")
        path = time.strftime('%Y-%m-%d %H-%M-%S') + ".jpg"
        with open(path, "wb") as f:
            f.write(image)

    # 下拉框操作
    def select_element(self, element_key, value, type_key, type_vlaue):
        element = self.url_element(element_key, value)
        element_select = Select(element)
        # 索引
        if type_key == "index":
            element_select.select_by_index(type_vlaue)
        # option属性的值
        elif type_key == "option":
            element_select.select_by_value(type_vlaue)
        # 下卡框的内容
        elif type_key == "text":
            element_select.select_by_visible_text(type_vlaue)

    # 输入时间
    def input_time(self, value, send_time):
        # 介绍3种操作方法
        # js = "document.getElementById('txtBeginDate').removeAttribute('readonly')"  # 1.原生js，移除属性
        # js = "$('input[id=txtBeginDate]').removeAttr('readonly')"  # 2.jQuery，移除属性
        # js = "$('input[id=txtBeginDate]').attr('readonly',false)"  # 3.jQuery，设置为false
        # js = "$('input[id=txtBeginDate]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
        js = "$('input[id=" + value + "]'.attr('readonly',''"
        self.driver.execute_script(js)
        # self.url_element(element_key, value).send_keys(send_time)
        self.driver.find_element_by_id(value).send_keys(send_time)

    # 句柄
    def handle_window(self):
        handles = self.driver.window_handles
        return handles

    # 退出，释放driver
    def driver_close(self):
        self.driver.close()

    # 获取元素的其他属性值
    def element_attru(self, element_key, vlaue, key):
        return self.url_element(element_key, vlaue).get_attribute(key)

