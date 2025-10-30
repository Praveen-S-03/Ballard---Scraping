from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import string

start_time = time.perf_counter()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

people_data = []

for alpha in string.ascii_lowercase:

    url = f"https://www.ballardspahr.com/people?Alpha={alpha}"
    driver.get(url)
    time.sleep(3)

    # Close cookie popup if it appears
    try:
        close_button = driver.find_element(By.ID, "onetrust-close-btn-container")
        close_button.click()
        time.sleep(1)
    except:
        pass

    # Keep clicking Load More until it disappears
    while True:
        try:
            load_more_btn = driver.find_element(By.CLASS_NAME, "LoadMoreButton")
            driver.execute_script("arguments[0].scrollIntoView(true);", load_more_btn)
            time.sleep(1)
            load_more_btn.click()
            time.sleep(1)
        except:
            break

    # Scraping the data

    names_list = driver.find_elements(By.CLASS_NAME, "PeopleResultCard__name")
    role_list = driver.find_elements(By.CLASS_NAME, "PeopleResultCard__role")
    mail_list = driver.find_elements(By.CLASS_NAME,"EmailLink")
    contact_list = driver.find_elements(By.CLASS_NAME,"ContactNumbersWithLabel__number")
    location_list = driver.find_elements(By.CLASS_NAME,"PeopleResultCard__office")

    for person,role,mail,contact,location in zip(names_list,role_list,mail_list,contact_list,location_list):
        people_data.append({
            "Name":person.text,
            "Role":role.text,
            "Mail":mail.get_attribute("href").replace("mailto:",''),
            "Phone":contact.text,
            "Location":location.text
        })

driver.quit()

#Saving it as a JSON file

with open("data.json","w") as datafile:
    json.dump(people_data,datafile,indent=4)

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.6f} seconds")