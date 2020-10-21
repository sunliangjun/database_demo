from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://download.csdn.net/download/guoshuoda/4978042?utm_medium=distribute.pc_feed_download.none-task-download-hot-1.nonecase&depth_1-utm_source=distribute.pc_feed_download.none-task-download-hot-1.nonecase"
# driver.get("https://detail.tmall.com/item.htm?spm=a222t.8063993.1387691862.11.73757f57pP7JRX&acm=lb-zebra-164656-989409.1003.4.859249&id=608384662277&scm=1003.4.lb-zebra-164656-989409.ITEM_608384662277_859249&sku_properties=10004:1617715035;5919063:6536025")
driver.get(url)
driver.implicitly_wait(2)
driver.find_element_by_partial_link_text("立即下载").click()
driver.implicitly_wait(2)
iframe_element = driver.find_element_by_name("passport_iframe")
driver.switch_to.frame(iframe_element)
driver.find_element_by_partial_link_text("账号密码登录").click()
driver.implicitly_wait(2)
driver.find_element_by_id("all").send_keys("123")
driver.find_element_by_id("password-number").send_keys("123")
driver.find_element_by_partial_link_text("登录").click()
driver.get_screenshot_as_file("a.png")


# driver.switch_to.frame("sufei-dialog-content")
# login_frame
# driver.find_element_by_id("fm-login-id").send_keys("123")
# sufei-dialog-content