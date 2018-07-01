from selenium import webdriver
import time

chromedriver = "/home/yagyansh/Desktop/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chromedriver)

driver.get("http://www8.mangafreak.net/")
name = input("Enter the name of Anime to search - ").lower()
name = name.split()
driver.get("http://www8.mangafreak.net/Search/" + '%20'.join(name))
result = driver.find_elements_by_class_name("manga_search_item")
for r in result:
	print(r.text)

index = int(input("Enter Index of anime to proceed - "))
index-=1
interest = result[index]
link = interest.find_element_by_tag_name("a")
link.click()
