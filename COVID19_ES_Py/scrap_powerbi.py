import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By


def take_screenshot_element():
    """Take screenshot of the alerts map and store it in the tmp folder."""

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    chrome_driver = os.path.join(os.getcwd(), "chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options,
                              executable_path=chrome_driver)

    driver.get(
        "https://publico.bi.es.gov.br/Reports/powerbi/PUBLICOS/SESA/eSUS%20VS-COVID%20PUBLICO")
    print(f"PowerBI acessado.\n\n")

    screenshotPath = os.path.join("tmp", f"ss_.png")
    # teste = driver.find_element_by_xpath("//div[@class='region region-content']")
    # img_url = ob.full_Screenshot(driver, save_path=r'.', image_name='ss.png')
    # print(img_url)
    # print(driver.screenshot(screenshotPath))

    driver.close()
    driver.quit()

    return screenshotPath


take_screenshot_element()
