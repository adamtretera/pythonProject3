from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "L2AGLb")))
    button.click()
    search_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "q")))
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.RETURN)


    assert "Selenium - Hledat Googlem" in driver.title
    driver.implicitly_wait(5)
    driver.quit()

if __name__ == "__main__":
    test_google_search()
