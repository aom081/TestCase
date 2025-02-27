import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# โหลด Test Data จาก CSV
def load_test_data():
    with open("../data/test_data.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)[0]  # ใช้แค่แถวแรก

test_data = load_test_data()

# ตั้งค่า ChromeDriver (แก้ให้ชี้ไปที่ไฟล์ที่โหลดมา)
chrome_driver_path = os.path.abspath("../drivers/chromedriver-win64/chromedriver.exe")  # แก้ path ตามเครื่องของคุณ
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# เปิดหน้าเว็บสมัครสมาชิก
driver.get("https://sc.npru.ac.th/sc_shortcourses/signup")
driver.maximize_window()

# กรอกข้อมูลจาก CSV
driver.find_element(By.NAME, "prefix").send_keys(test_data["prefix"])
driver.find_element(By.NAME, "first_name_th").send_keys(test_data["first_name_th"])
driver.find_element(By.NAME, "last_name_th").send_keys(test_data["last_name_th"])
driver.find_element(By.NAME, "prefix_en").send_keys(test_data["prefix_en"])
driver.find_element(By.NAME, "first_name_en").send_keys(test_data["first_name_en"])
driver.find_element(By.NAME, "last_name_en").send_keys(test_data["last_name_en"])
driver.find_element(By.NAME, "dob_day").send_keys(test_data["dob_day"])
driver.find_element(By.NAME, "dob_month").send_keys(test_data["dob_month"])
driver.find_element(By.NAME, "dob_year").send_keys(test_data["dob_year"])
driver.find_element(By.NAME, "id_card").send_keys(test_data["id_card"])
driver.find_element(By.NAME, "password").send_keys(test_data["password"])
driver.find_element(By.NAME, "phone").send_keys(test_data["phone"])
driver.find_element(By.NAME, "email").send_keys(test_data["email"])
driver.find_element(By.NAME, "address").send_keys(test_data["address"])
driver.find_element(By.NAME, "province").send_keys(test_data["province"])
driver.find_element(By.NAME, "district").send_keys(test_data["district"])
driver.find_element(By.NAME, "subdistrict").send_keys(test_data["subdistrict"])
driver.find_element(By.NAME, "zipcode").send_keys(test_data["zipcode"])

# คลิกยอมรับข้อมูลจริง
driver.find_element(By.NAME, "confirm_checkbox").click()

# คลิกปุ่มลงทะเบียน
driver.find_element(By.ID, "register_btn").click()

# รอโหลดหน้า
time.sleep(3)

# ตรวจสอบข้อความ "ลงทะเบียนสำเร็จ"
success_message = driver.find_element(By.CLASS_NAME, "swal-title").text
assert success_message == "ลงทะเบียนสำเร็จ", "Test Failed!"

print("✅ Test Case Passed: ลงทะเบียนสำเร็จ!")

# ปิดเบราว์เซอร์
driver.quit()
