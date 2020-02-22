import time
from selenium import webdriver

# driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
# options.add_argument("--window-size=1366,768")
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome('C:/web/driver/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()