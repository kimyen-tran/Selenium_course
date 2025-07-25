from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()
driver.get("https://dev.sp.leadplus.net/bundle/27/budget_group/214/portfolio/405?type=rsa_ads&status=Enabled")
driver.maximize_window()

wait = WebDriverWait(driver,20)

Username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
Username.send_keys("admin")

Password = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
Password.send_keys("SP@123456")

BtnLogin = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-at_lb='btn_login']")))
BtnLogin.click()

#BAI 01
Section_error= wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-at_id='msg__publish_status_alert']")))
try: 
    # Section_error= wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-at_id='msg__publish_status_alert']")))
    Title_error= Section_error.find_element(By.XPATH, ".//span[@class='fw-semibold' and contains(text(),'Failed to publish')]")
    print(f"Banner màu vàng có nội dung: {Title_error.text}")
except:
    print(f"Không có title như yêu cầu")

try: 
    Ma_loi = wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='15113_GGS (can create RSA/ KW/ Negative KW)']")))
    print(f"mã lỗi: {Ma_loi.text}")
except:
    print(f"khong co ma loi")

# Ma_loi = wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='15133_GGS2']")))
# assert "15133_GGS2" in Ma_loi.text
# print("Mã lỗi:", Ma_loi.text)
   
#BAI02
tabRSA= wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@data-at_lb='lb_rsa_ads']")))
tabRSA.click()

DropFilter= driver.find_elements(By.XPATH, "//div[contains(@class,'_select_19ily_1')]")
DropFilter1= wait.until(EC.element_to_be_clickable(DropFilter[0]))
DropFilter1.click()

SelectOption=DropFilter1.find_element(By.XPATH,".//div[@class=' css-hlgwow']/span[contains(@class,'d-flex')]/div[text()='Contains']")
time.sleep(5)
SelectOption.click()

SearchF1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='textSearch1']")))
SearchF1.send_keys("Adgr")

SearchF2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='textSearch2']")))
SearchF2.send_keys("1237")

ButtonApply = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-at_lb='btn_search_apply']")))
driver.execute_script("arguments[0].scrollIntoView(true);", ButtonApply)  
driver.execute_script("arguments[0].click();", ButtonApply)   

TableRSA = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
time.sleep(3)
Records = TableRSA.find_elements(By.XPATH, ".//tbody/tr")  
print ("số lượng records sau khi filter:", len(Records))
for row in Records:
        Noi_dung_row = row.text
        if "Adgr" in Noi_dung_row and "1237" in Noi_dung_row:
           print("Tìm thấy record:", Noi_dung_row)
  

#BAI03
TableRSA=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
Records = TableRSA.find_elements(By.XPATH, ".//tbody/tr")
Total_record_thoa_man = 0
for row in Records:
    Noi_dung_row = row.text
    PublishStt_Removed=row.find_elements(By.XPATH, ".//span[contains(@class, 'badge') and text()='Removed']")  #in ra list
    PublishStt_Added=row.find_elements(By.XPATH, ".//span[contains(@class, 'badge') and text()='Added']")
    UserStt_Enabled=row.find_elements(By.XPATH, ".//span[@data-at_lb='lb_enabled']")
    ApprovalStt_Not_Publish=row.find_elements(By.XPATH, ".//span[@data-at_lb='lb_not_published']")
    if UserStt_Enabled and PublishStt_Added:  #check điều kiện trong row 
      print("Record cần tìm 1:", Noi_dung_row)
    elif UserStt_Enabled and PublishStt_Removed:
      print("\nRecord cần tìm 2:", Noi_dung_row)

    if ApprovalStt_Not_Publish:
        Total_record_thoa_man +=1
print("\n Total record chưa được publish:", Total_record_thoa_man)






