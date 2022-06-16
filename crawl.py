# //*[@id="XKiOfPaBg"]/div[2]/div/div/div/div[1]/div[3]/div/div/div/div/div/div[5]/div/div[11]/div/div/div/div/div/div/div/div/div[1]/div/div[7]/div/table/tbody/tr[2]/td[2]/div
# //*[@id="XKiOfPaBg"]/div[2]/div/div/div/div[1]/div[3]/div/div/div/div/div/div[5]/div/div[11]/div/div/div/div/div/div/div/div/div[1]/div/div[8]/div/table/tbody/tr[2]/td[1]/div
import selenium.webdriver as webdriver
from webdriver_manager.chrome import ChromeDriverManager
import csv

f1 = open('data.csv', 'w')
writer = csv.writer(f1)
writer.writerow(['id', 'name'])
url = 'https://namu.wiki/w/%EB%8F%99%EB%AC%BC%EC%9D%98%20%EC%88%B2%20%EC%8B%9C%EB%A6%AC%EC%A6%88/%EC%95%84%EB%AF%B8%EB%B3%B4%20%EC%B9%B4%EB%93%9C'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

for i in range(0, 448):
    id = driver.find_element_by_xpath(
        '//*[@id="XKiOfPaBg"]/div[2]/div/div/div/div[1]/div[3]/div/div/div/div/div/div[5]/div/div[11]/div/div/div/div/div/div/div/div/div[1]/div/div[' + str(
            7 + i // 100) + ']/div/table/tbody/tr[' + str(
            i % 100 + 2) + ']/td[1]/div').text
    name = driver.find_element_by_xpath(
        '//*[@id="XKiOfPaBg"]/div[2]/div/div/div/div[1]/div[3]/div/div/div/div/div/div[5]/div/div[11]/div/div/div/div/div/div/div/div/div[1]/div/div[' + str(
            7 + i // 100) + ']/div/table/tbody/tr[' + str(
            i % 100 + 2) + ']/td[2]/div').text
    print(id, name)
    writer.writerow([id, name])
for i in range(0, 56):
    id = driver.find_element_by_xpath(
        '//*[@id="XKiOfPaBg"]/div[2]/div/div/div/div[1]/div[3]/div/div/div/div/div/div[5]/div/div[11]/div/div/div/div/div/div/div/div/div[1]/div/div[' + str(
            12 + i // 50) + ']/div/table/tbody/tr[' + str(
            i % 50 + 2) + ']/td[1]/div').text
    name = driver.find_element_by_xpath(
        '//*[@id="XKiOfPaBg"]/div[2]/div/div/div/div[1]/div[3]/div/div/div/div/div/div[5]/div/div[11]/div/div/div/div/div/div/div/div/div[1]/div/div[' + str(
            12 + i // 50) + ']/div/table/tbody/tr[' + str(
            i % 50 + 2) + ']/td[2]/div').text
    print(id, name)
    writer.writerow([id, name])

f1.close()
