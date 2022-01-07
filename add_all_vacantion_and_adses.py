from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver_path_location = "C:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path_location)
driver.maximize_window()

# ------------------------  IVANO-FRANKIVSK ------------------------------------------- #
driver.get("https://www.0342.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# --------------------------------- UZHGOROD -------------------------------------------#

driver.get("https://www.0312.ua/cabinet/vacancy/create")
email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ----------------------------------- LVIV ------------------------------------------- #

driver.get("https://www.032.ua/cabinet/vacancy/create")
email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ---------------------------------  LUTSK  --------------------------------------------- #
driver.get("https://www.0332.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# --------------------------- TERNOPIL  -------------------------------------------- #

driver.get("https://www.0352.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ---------------------------------------  YALTA ------------------------------------ #

driver.get("https://www.3654.ru/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# --------------------------------------- RIVNE  ------------------------------------------------ #

driver.get("https://www.0362.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# --------------------------------------- KHMELNYTSKYI ---------------------------------------- #

driver.get("https://www.0382.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------------------- CHERNIVTSI ----------------------------------- #
driver.get("https://www.0372.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# --------------------------------- VINNYTSIA -------------------------------------- #

driver.get("https://www.0432.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ----------------------------------------- KIEV ------------------------------------------- #

driver.get("https://www.44.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# --------------------------------------- BROVARY  ------------------------------------- #

driver.get("https://www.4594.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)
#??????????????????????????????????????????????????????#


# ---------------------------------------  WHITE CHURCH  ------------------------------------------------------ #

driver.get("https://www.04563.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()

# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)
#??????????????????????????????????????????????????????#

# ------------------------------------ ODESSA ----------------------------------------------- #

driver.get("https://www.048.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------------- CHERKASY  ------------------------------------------ #

driver.get("https://www.0472.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------------------ ZHYTOMYR ------------------------------------------ #

driver.get("https://www.0412.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------------------- SUMY ------------------------------------------- #

driver.get("https://www.0542.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -------------------------------------- KROPYVNYTSKYI  ----------------------------------------- #

driver.get("https://www.0522.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ----------------------------------------- KHARKIV --------------------------------------------- #

driver.get("https://www.057.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------------ POLTAVA  ----------------------------------------------- #

driver.get("https://www.0532.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------------ KRIVOY ROG --------------------------------------- #

driver.get("https://www.0564.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------------- KREMENCHUG -------------------------------------------- #

driver.get("https://www.05366.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -------------------------------------- NIKOLAEV  ----------------------------------------- #

driver.get("https://www.0512.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -------------------------------- POKROVSK AND MYRNOGRAD --------------------------------- #

driver.get("https://www.06239.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -------------------------------------- MELITOPOL -------------------------------------- #

driver.get("https://www.0619.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()

# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# --------------------------------- ZAPOROZHYE ----------------------------------------------- #

driver.get("https://www.061.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ----------------------------------- MARIUPOL  ------------------------------------------- #

driver.get("https://www.0629.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ----------------------------------------- BERDYANSK --------------------------------------- #

driver.get("https://www.06153.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------------- KONSTANTINOVKA ------------------------------------ #

driver.get("https://www.06272.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()

# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# --------------------------------------- TOKMAK ------------------------------------------- #

driver.get("https://www.06178.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------------------ KHERSON  ------------------------------------------- #

driver.get("https://www.0552.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -------------------------------- DONETSK --------------------------------------- #

driver.get("https://www.62.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -----------------------------------  KAMENSK --------------------------------------- #

driver.get("https://www.5692.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ---------------------- KAMIANETS-PODILSKYI ---------------------------------- #

driver.get("https://www.3849.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ---------------------------------------- KRAMATORSK --------------------------------- #

driver.get("https://www.6264.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------------- SEVERODONETSK ------------------------------ #

driver.get("https://www.06452.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -----------------------------  DOBROPOLYA ----------------------------- #

driver.get("https://www.06277.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -------------------------- PAVLOGRAD ---------------------------------------------- #

driver.get("https://www.5632.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -------------------------- BAKHMUT --------------------------------------- #

driver.get("https://www.06274.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ----------------------- KIRILLOVKA ---------------------------------- #

driver.get("https://www.6131.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ---------------------------- CHERNOMORSK ------------------------------- #

driver.get("https://www.04868.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -------------------------------- BORYSPIL --------------------------- #

driver.get("https://www.4595.com.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[10]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[22]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ---------------------------- CHERNIHIV ------------------------------------ #

driver.get("https://www.0462.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# ------------------------- GORLOVKA ------------------------------------- #

driver.get("https://www.06242.ua/cabinet/vacancy/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
send_keys_to_email = driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
# --------------------------------- -------------------------------------------#
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
send_keys_to_password = driver.find_element_by_xpath(password).send_keys('Privat24¿')
# --------------------------------- -------------------------------------------#
click_button_enter = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button_enter).click()
time.sleep(10)
# --------------------------------- -------------------------------------------#
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[9]"
driver.find_element_by_xpath(click_cat_one).click()
click_input = '/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/span[2]/span[1]/span/ul/li/input'
driver.find_element_by_xpath(click_input).click()
click_cat_one = "/html/body/span/span/span[2]/ul/li[23]"
driver.find_element_by_xpath(click_cat_one).click()
# --------------------------------- -------------------------------------------#
vacantion = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/input"
click_vacantion_input = driver.find_element_by_xpath(vacantion).click()
send_keys_to_vacantion = driver.find_element_by_xpath(vacantion).send_keys('Музикант в духовий військовий оркестр')
# ---------------------------------------------------------------------------------------- #
click_salary_from = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/input"
driver.find_element_by_xpath(click_salary_from).click()
driver.find_element_by_xpath(click_salary_from).send_keys('10500')
# ----------------------------------  ------------------------------------------ #
click_salary_to = "/html/body/div[2]/div/section/div/form/div/div/div[4]/div[2]/input"
driver.find_element_by_xpath(click_salary_to).click()
send_keys_salary_from = driver.find_element_by_xpath(click_salary_to).send_keys('18000')
# --------------------------------- -------------------------------------------#
click_carrency = "Ads[currency_id]"
driver.find_element_by_name(click_carrency).click()
Select(driver.find_element_by_name(click_carrency)).select_by_value('2')
# --------------------------------- -------------------------------------------#
click_employment = "Ads[graph_job]"
driver.find_element_by_name(click_employment).click()
Select(driver.find_element_by_name(click_employment)).select_by_value('17')
# --------------------------------- -------------------------------------------#
click_work_experience = "Ads[experience]"
driver.find_element_by_name(click_work_experience).click()
Select(driver.find_element_by_name(click_work_experience)).select_by_value('24')
# --------------------------------- -------------------------------------------#
click_education = "Ads[education]"
driver.find_element_by_name(click_education).click()
Select(driver.find_element_by_name(click_education)).select_by_value('31')
# --------------------------------- -------------------------------------------#
click_description = "Ads[txt]"
driver.find_element_by_name(click_description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
click_employer = "/html/body/div[2]/div/section/div/form/div/div/div[11]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(click_employer).click()
select_employer = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_employer).click()
# --------------------------------- -------------------------------------------#
click_phone = "/html/body/div[2]/div/section/div/form/div/div/div[13]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(click_phone).click()
select_phone = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_phone).click()
# --------------------------------- -------------------------------------------#
click_free_placement = "/html/body/div[2]/div/section/div/form/div/div/div[16]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(click_free_placement).click()
# --------------------------------- -------------------------------------------#
click_email = "/html/body/div[2]/div/section/div/form/div/div/div[14]/div[2]/span"
driver.find_element_by_xpath(click_email).click()
select_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(select_email).click()
time.sleep(5)
click_submit = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_submit).click()
time.sleep(5)

# -------------- ІВАНО-ФРАНКІВСЬК ----------------------- #

driver.get("https://www.0342.ua/cabinet/ads/create")
email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# ---------------------- ----------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# ----------------------      ----------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# ---------------------- ----------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# -------------------- УЖГОРОД -------------------- #

driver.get("https://www.0312.ua/cabinet/ads/create")
email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# --------------------- ЛЬВІВ ------------------------------- #

driver.get("https://www.032.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------------ ЛУЦЬК ------------------------------------ #

driver.get("https://www.0332.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------- ТЕРНОПІЛЬ --------------------------------- #

driver.get("https://www.0352.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# --------------------------------- ЯЛТА -------------------------------- #

driver.get("https://www.3654.ru/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# -------------------------- РІВНЕ ------------------------------------- #

driver.get("https://www.0362.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# -------------------------- ХМЕЛЬНИЦЬКИЙ ---------------------------------------- #

driver.get("https://www.0382.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------------- ЧЕРНІВЦІ --------------------------------------- #

driver.get("https://www.0372.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# -------------------------- ВІННИЦЯ ------------------------------------ #

driver.get("https://www.0432.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ---------------------------- КИЇВ ------------------------------------ #

driver.get("https://www.44.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------ БРОВАРИ ------------------------------ #

driver.get("https://www.4594.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ---------------------------- БІЛА - ЦЕРКВА -------------------------------- #

driver.get("https://www.04563.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ---------------------------- ОДЕСА ------------------------------------ #

driver.get("https://www.048.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------- ЧЕРКАСИ --------------------------- #

driver.get("https://www.0472.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------- ЖИТОМИР ------------------------------- #

driver.get("https://www.0412.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# -------------------------------- СУМИ ---------------------------- #

driver.get("https://www.0542.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# --------------------------  КРОПИВНИЦЬКИЙ -------------------------- #

driver.get("https://www.0522.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------- ХАРЬКОВ ------------------------------- #

driver.get("https://www.057.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ----------------------------- ПОЛТАВА --------------------------------- #

driver.get("https://www.0532.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ---------------------------------- КРИВИЙ РІГ ------------------------------------------ #

driver.get("https://www.0564.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# -------------------------------- КРЕМЕНЧУГ --------------------------- #

driver.get("https://www.05366.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------- НІКОЛАЄВ ------------------------------ #

driver.get("https://www.0512.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ----------------------- ПОКРОВСЬК ТА МИРНОГРАД ---------------------------------- #

driver.get("https://www.06239.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ----------------------------- МЕЛІТОПОЛЬ ------------------------------ #

driver.get("https://www.0619.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------------- ЗАПОРОЖЬЯ ----------------------------------------- #

driver.get("https://www.061.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# --------------------------- МАРІУПОЛЬ ----------------------------- #

driver.get("https://www.0629.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# --------------------------  БЕРДЯНСЬК ------------------------------------ #

driver.get("https://www.06153.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------- КОСТЯНТИНІВКА ---------------------------- #

driver.get("https://www.06272.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------------------- ТОКМАТ ----------------------------------- #

driver.get("https://www.06178.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# --------------------------------- ХЕРСОН ----------------------------------------- #

driver.get("https://www.0552.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# --------------------------------- ДОНЕЦЬК ------------------------------------- #

driver.get("https://www.62.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ----------------------------------- КАМЕНСЬК ----------------------------------- #

driver.get("https://www.5692.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ---------------------------- КАМЯНЕЦЬ-ПОДІЛЬСЬК ------------------------------ #

driver.get("https://www.3849.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------------- КРАМАТОРСЬК ----------------------------------- #

driver.get("https://www.6264.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ---------------------------- СЕВЕРОДОНЕЦК ------------------------------- #

driver.get("https://www.06452.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ----------------------------- ДОБРОПОЛЬЯ ------------------------------------- #

driver.get("https://www.06277.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ------------------------------- ПАВЛОГРАД --------------------------------- #

driver.get("https://www.5632.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ----------------------------- БАХМУТ ------------------------------------------------- #

driver.get("https://www.06274.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ----------------------------------- КИРИЛЛОВКА ------------------------------------------ #

driver.get("https://www.6131.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

# ---------------------------------------- ЧЕРНОМОРСК ---------------------------------------- #

driver.get("https://www.04868.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)
# ---------------------------------------- БОРИСПІЛЬ ---------------------------------------- #

driver.get("https://www.4595.com.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[5]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[14]/ul/li[4]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)
# ---------------------------------------- ЧЕРНІГОВ ---------------------------------------- #

driver.get("https://www.0462.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)
# ---------------------------------------- ГОРЛОВКА ---------------------------------------- #

driver.get("https://www.06242.ua/cabinet/ads/create")

email = "/html/body/main/div/div/div[3]/div/div/div/form/div[1]/input"
driver.find_element_by_xpath(email).send_keys('098320000w@gmail.com')
password = "/html/body/main/div/div/div[3]/div/div/div/form/div[2]/input"
driver.find_element_by_xpath(password).send_keys('Privat24¿')
click_button = "/html/body/main/div/div/div[3]/div/div/div/form/button"
driver.find_element_by_xpath(click_button).click()
time.sleep(10)
# --------------------------------------------- #
heading = "/html/body/div[2]/div/section/div/form/div/div/div[1]/div[2]/input"
driver.find_element_by_xpath(heading).click()
driver.find_element_by_xpath(heading).send_keys('Музиканти в військовий духовий оркестр')
# --------------------------------------------- #
description = "/html/body/div[2]/div/section/div/form/div/div/div[2]/div[2]/textarea"
driver.find_element_by_xpath(description).click()
driver.find_element_by_xpath(description).send_keys(
    "Проводиться набір музикантів в військовий духовий оркестр м. Маріуполь  до 50 років на контрактній основі")
# --------------------------------------------- #
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_one = "/html/body/span/span/span[2]/ul/li[4]/ul/li[1]"
driver.find_element_by_xpath(select_rubric_one).click()
rubric = "/html/body/div[2]/div/section/div/form/div/div/div[3]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(rubric).click()
select_rubric_two = "/html/body/span/span/span[2]/ul/li[20]/ul/li[3]"
driver.find_element_by_xpath(select_rubric_two).click()
# ---------------------------------------------------------------- #
name = '/html/body/div[2]/div/section/div/form/div/div/div[5]/div[2]/span/span[1]/span/span[1]/span'
driver.find_element_by_xpath(name).click()
name_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(name_click).click()
# ---------------------------------------------------------------- #
phone = "/html/body/div[2]/div/section/div/form/div/div/div[6]/div[2]/span[2]/span[1]/span/ul/li/input"
driver.find_element_by_xpath(phone).click()
phone_click = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(phone_click).click()
# ------------------------------------------------------------------ #
email = "/html/body/div[2]/div/section/div/form/div/div/div[7]/div[2]/span/span[1]/span/span[1]/span"
driver.find_element_by_xpath(email).click()
click_email = "/html/body/span/span/span[2]/ul/li"
driver.find_element_by_xpath(click_email).click()
# ------------------------------------------------------------------ #
free = "/html/body/div[2]/div/section/div/form/div/div/div[9]/div/div[2]/div[1]/div[7]/input[3]"
driver.find_element_by_xpath(free).click()
# ----------------------------------------------------------#
click_button_send = "/html/body/div[2]/div/section/div/form/div/div/button"
driver.find_element_by_xpath(click_button_send).click()
time.sleep(5)

driver.quit()