# This program will LEt you log_in to your google acount 
# 1/you have to Change your privacy settings in google acount
# 2/First by going through your Stack over flow acount 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

ok = webdriver.Chrome(r"C:\Users\HP\Downloads\Telegram Desktop\chromedriver_win32\chromedriver.exe")  # Path to the exe file of ChromeDrive (Find in the download folder)

ok.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
ok.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/button[1]").click()
ok.find_element_by_id("identifierId").send_keys("angsudas62@gmail.com") # put your email that u use in google acount
ok.find_element_by_class_name("VfPpkd-RLmnJb").click()
ok.maximize_window()
ok.implicitly_wait(4)
ok.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").send_keys("*******") # put your google password

ok.find_element_by_xpath("//*[@id='passwordNext']/div/button/div[2]").click()

ok.get("https://translate.google.co.in/#view=home")
ok.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div[1]/a").click()
ok.find_element_by_xpath("//*[@id='ft-icon-img-cmn']").click()
ok.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/div/div/div").click()


ok.switch_to.frame(ok.find_element_by_class_name("I0_1603209239122"))
ok.find_element_by_class_name("VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ INImOe clr7zd").click()
