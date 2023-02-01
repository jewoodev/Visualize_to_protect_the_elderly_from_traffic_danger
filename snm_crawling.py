#Step 1. 필요한 모듈을 로딩합니다
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time          


driver = webdriver.Edge('C:/develop_dir/playdata_project/data_visualization/edgedriver_win64/msedgedriver.exe')
# Options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver.get(url='https://tmacs.kotsa.or.kr/web/TG/TG300/TG3200/Tg3200_34.jsp?mid=S1812#')
select = Select(driver.find_element(By.XPATH, '//*[@id="sido"]'))
select.select_by_visible_text('서울')
driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[1]/div[2]/a').click()
time.sleep(1)
view_branch_details = driver.find_elements(By.XPATH,'//*[@id="rMateH5__Content57"]/div')
print(view_branch_details)
for vbd in view_branch_details:
    try:
        vbd.click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        driver.get_window_position(driver.window_handles[1])
        local = driver.find_element(By.XPATH, '//*[@id="new_popup"]/div[2]/table[1]/tbody/tr/td/dl[1]/dd')
        local_info = local.text
        place = driver.find_element(By.XPATH, '//*[@id="new_popup"]/div[2]/table[1]/tbody/tr/td/dl[2]/dd')
        place_info = place.text
        table = driver.find_element(By.XPATH, '//*[@id="new_popup"]/div[2]/table[2]')
        table_info = table.text
        print(local_info, place_info, table_info)
        driver.switch_to.window(driver.window_handles[0])
        driver.get_window_position(driver.window_handles[0])
        itemlist = driver.find_element(By.CLASS_NAME, "rMateH5__VBrowserScrollBar")
        driver.execute_script("arguments[0].scrollBy(0, 20)", itemlist)
    except:
        pass
driver.close()

# //*[@id="rMateH5__Content57"]/div[6]
# //*[@id="rMateH5__Content57"]/div[17]
# //*[@id="rMateH5__Content57"]/div[19]
# //*[@id="rMateH5__Content57"]/div[10]