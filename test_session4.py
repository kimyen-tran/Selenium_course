
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Khởi tạo trình duyệt
# driver = webdriver.Chrome()
# driver.get("https://dev.sp.leadplus.net/")
# driver.maximize_window()
# time.sleep(2)

# EmailTextbox = driver.find_element(By.XPATH, "//input[contains(@name,'username')]")
# EmailTextbox.send_keys("admin")
# time.sleep(2)

# PassWordTextbox = driver.find_element(By.XPATH, "//input[contains(@name,'password')]")
# PassWordTextbox.send_keys("SP@123456")
# time.sleep(2)

# LoginButton = driver.find_element(By.XPATH, "//button[contains(@data-at_id, 'btn__login')]")
# LoginButton.click()
# time.sleep(3)

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test_lien_tiep():
  #LOGIN 
  driver = webdriver.Chrome()
  driver.get("https://dev.sp.leadplus.net/bundle/27/budget_group/214/portfolio/405?type=rsa_ads&status=Enabled")
  driver.maximize_window()

  wait = WebDriverWait(driver, 30)

  EmailTextbox = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
  EmailTextbox.send_keys("admin")

  PassWordTextbox = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
  PassWordTextbox.send_keys("SP@123456")

  LoginButton = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-at_id='btn__login']")))
  LoginButton.click()

  expected_url = "https://dev.sp.leadplus.net/bundle/27/budget_group/214/portfolio/405"
  wait.until(EC.url_to_be(expected_url))
  
BÀI 1
  TitleBanner = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='fw-semibold' and contains(text(), 'Failed to publish')]")))
  assert "Failed to publish" in TitleBanner.text 
  print("Banner text:", TitleBanner.text)

  CodeError = wait.until(EC.presence_of_element_located((By.XPATH,"//a[text()='15133_GGS2']")))
  assert "15133_GGS2" in CodeError.text
  print("Mã lỗi:", CodeError.text)

# Direct tới Tab RSA
  tabRSA= wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@data-at_lb='lb_rsa_ads']")))
  tabRSA.click()

# BÀI 2
  # DropdownBtn = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class, 'css-hlgwow')]")))
  # DropdownBtn.click()

  # OptContains = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'single-value') and text()='Contains']")))
  # OptContains.click()

  # TextSearchF1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='textSearch1']")))
  # TextSearchF1.send_keys("Adgr")

  # TextSearchF2 = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='textSearch2']")))
  # TextSearchF2.send_keys("1237")

  # ButtonApply = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-at_lb='btn_search_apply']")))
  # driver.execute_script("arguments[0].scrollIntoView(true);", ButtonApply)   # Cần scroll để tìm được button và click
  # driver.execute_script("arguments[0].click();", ButtonApply)    # Vì btn bị overlay nên cần JavaScript để click (vượt qua intercept)

  # TableRSA = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
  # driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
  # Records = TableRSA.find_elements(By.XPATH, ".//tbody/tr")   # Dùng .// để tìm phần từ tr từ TableRSA trở đi, chứ ko phải toàn bộ DOM
  # print ("số lượng records sau khi filter:", len(Records))
  # for row in Records:
  #       Noi_dung_row = row.text
  #       if "Adgr" in Noi_dung_row and "1237" in Noi_dung_row:
  #          print("Tìm thấy record:", Noi_dung_row)

# BÀI 3 
  # TableRSA=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
  # driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
  # Records = TableRSA.find_elements(By.XPATH, ".//tbody/tr")
  # Total_record_thoa_man = 0
  # for row in Records:
  #        Noi_dung_row = row.text
  #        PublishStt_Removed=row.find_elements(By.XPATH, ".//span[contains(@class, 'badge') and text()='Removed']")  #in ra list
  #        PublishStt_Added=row.find_elements(By.XPATH, ".//span[contains(@class, 'badge') and text()='Added']")
  #        UserStt_Enabled=row.find_elements(By.XPATH, ".//span[@data-at_lb='lb_enabled']")
  #        ApprovalStt_Not_Publish=row.find_elements(By.XPATH, ".//span[@data-at_lb='lb_not_published']")
  #        if UserStt_Enabled and PublishStt_Added:  #check điều kiện trong row 
  #         print("Record cần tìm 1:", Noi_dung_row)
  #        elif UserStt_Enabled and PublishStt_Removed:
  #         print("\nRecord cần tìm 2:", Noi_dung_row)

  #        if ApprovalStt_Not_Publish:
  #         Total_record_thoa_man +=1
  # print("\n Total record chưa được publish:", Total_record_thoa_man)

# BÀI 4
  # TableRSA=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
  # driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
  # Records = TableRSA.find_elements(By.XPATH, ".//tbody/tr")
  # for row in Records:
  #   campaign_links = row.find_elements(By.XPATH, ".//td[contains(@data-at_id,'td__table_rsa_campaign')]//a")
  #   adgroup_links  = row.find_elements(By.XPATH, ".//td[contains(@data-at_id,'td__table_rsa_ads_group')]//a")
  #   if campaign_links:
  #       campaign_href = campaign_links[0].get_attribute("href")
  #       print("Campaign là link:", campaign_href)

  #   if adgroup_links:
  #       adgroup_href = adgroup_links[0].get_attribute("href")
  #       print("Ad Group là link:", adgroup_href)
    
#BÀI 5
  # BtnEditPortfoilo = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-at_lb='lb_edit_portfolio']")))
  # BtnEditPortfoilo.click()
  # try: 
  #     Popup_Edit=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-at_id='modal__create_new_portfolio']")))
  #     print("Popup đã xuất hiện.")
  # except:
  #     print("không có popup nào hết")

  # Port_Name = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@data-at_id='input__create_portfolio_name']")))
  # Port_Name.send_keys("yen_test")
  # Btn_Close= wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-at_lb='btn_close']")))
  # Btn_Close.click()

#BÀI 6:
  # TableRSA=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
  # driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
  # Records = TableRSA.find_elements(By.XPATH, ".//tbody/tr")
  # so_record_thieu_heading_preview = 0
  # for row in Records: 
  #       Preview =row.find_elements(By.XPATH, ".//td[contains(@data-at_id, 'td__table_rsa_preview')]//span[contains(@class, '_preview-text-title')]")
  #       Tieu_de = Preview[0].text()
  #       List_tieu_de = Tieu_de.split("|")   #Tách chuỗi thành danh sách theo dấu "|"
  #       print("tieu de:", List_tieu_de)
  #       if len(List_tieu_de) < 3:
  #            so_record_thieu_heading_preview += 1  
  # print("số record thiếu heading trong preview:", so_record_thieu_heading_preview)

#BÀI 7:
  # TableRSA=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
  # driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
  # # Records = TableRSA.find_elements(By.XPATH, ".//tbody/tr")
  # btn_url = driver.find_elements(By.XPATH, "//tbody/tr/td[contains(@data-at_lb,'td__table_rsa_url')]/button[@data-at_lb='lb_url_with_platform_query']")
  # # btn_url = driver.find_elements(By.XPATH, "//p[@class='container-url-btn-text]")
  # if btn_url:
  #   actions = ActionChains(driver)
  #   actions.move_to_element(btn_url[0]).pause(2).perform()
    
  #   tooltip = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'navigate-url')]")))
  #   tooltip_text = tooltip.text

  #   print("Tooltip hiển thị:", tooltip_text)
  # else:
  #   print("❌ Không tìm thấy bất kỳ phần tử nào phù hợp với XPath.")
  # actions = ActionChains(driver)
  # actions.move_to_element(btn_url).pause(2).perform()
  # tooltip = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'navigate-url')]")))
  # tooltip_text = tooltip.text()
  # print("Tooltip hiển thị:", tooltip_text)
  # if tooltip_text.startswith("https://dev.sp.leadplus.net/"):
  #   print("✅ Tooltip hiển thị URL đúng")
  # else:
  #   print("❌ Tooltip không đúng")

#BÀI 8:
  # TableRSA=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
  # driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
  # Records = TableRSA.find_elements(By.XPATH, ".//tbody/tr")
  # for row in Records:
  #     checkbox = row.find_elements(By.XPATH, ".//td[contains(@data-at_id,'td__table_rsa_select')]//input[@type='checkbox']")
  #     for i in range(2):
  #         driver.execute_script("arguments[0].click();", checkbox[i])
  #     # print(" Đã click vào checkbox", [i])

# #BÀI 9:
  # TableRSA=wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
  # driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
  # first_item_page1 = wait.until(EC.presence_of_element_located((By.XPATH, "//table//tbody/tr[1]"))).text
  # print("Trang 1 - Item đầu tiên:\n", first_item_page1)

  # page_2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='page-link' and text()='2']")))
  # # page_2.click()
  # driver.execute_script("arguments[0].click();", page_2)  #element bị che phủ không thể dùng action click 
  # wait.until(EC.presence_of_element_located((By.XPATH, "//table//tbody/tr[1]")))

  # first_item_page2 = driver.find_element(By.XPATH, "//table//tbody/tr[1]").text
  # print("Trang 2 - Item đầu tiên:\n", first_item_page2)

  # if first_item_page1 != first_item_page2:
  #       print("Item đầu tiên ở hai trang khác nhau.")
  # else:
  #       print("Item đầu tiên ở hai trang giống nhau.")


 #BÀI 10:
#   Filter_Approval_Status = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='approvalStatus']")))
#   Filter_Approval_Status.click()
# # đang không get được element này, cần can thiệp manual tại step này 
#   Opt_Disapproved = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'_select_19ily_1')]//div[contains(@class,'single-value') and text()='Disapproved']")))
#   driver.execute_script("arguments[0].scrollIntoView(true);", Opt_Disapproved)
#   driver.execute_script("arguments[0].click();", Opt_Disapproved) 

#   ButtonApply = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@data-at_lb='btn_search_apply']")))
#   driver.execute_script("arguments[0].scrollIntoView(true);", ButtonApply)   # Cần scroll để tìm được button và click
#   driver.execute_script("arguments[0].click();", ButtonApply) 

#   TableRSA = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_table-rsa-campaign_8o8n8_128']")))
#   driver.execute_script("arguments[0].scrollIntoView(true);", TableRSA)
#   Records = TableRSA.find_elements(By.XPATH, ".//tbody/tr")
#   print ("số lượng records sau khi filter:", len(Records))
#   Total_record_match_filter = 0
#   for row in Records:
#         Nd_Approval_Status = row.find_elements(By.XPATH,"//span[contains(@class,'badge')]")
#         for badge in Nd_Approval_Status:
#            if "Disapproved" in badge.text:
#                Total_record_match_filter += 1
#                break
#   if Total_record_match_filter == len(Records):
#      print(f"Tổng số record thỏa filter 'Disapproved': {Total_record_match_filter} / {len(Records)}")
