from selenium import webdriver
import time

chromedriver = "/home/yagyansh/Desktop/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("http://www8.mangafreak.net/Manga/Boruto")

# I have to wait now untill page loads. this can be done by
while(1):
	try:
		done = driver.find_element_by_link_text("Home")
		break;
	except Exception as e:
		time.sleep(1)
		continue

lists = driver.find_element_by_class_name("manga_series_list")
rows = lists.find_elements_by_tag_name("tr")
for index, val in enumerate(rows):
    print(index,"\t=>\t" , val.text )


i = int(input("Which index chapter do you want to download? (zero if a range is needed) "))
if i!=0 :
	interest = rows[i]
	print("Now Downloading " , interest.find_elements_by_tag_name("td")[0].text)
	down = interest.find_element_by_link_text("Download").click()
else:
	print("Enter range of chapters to download (inclusive)")
	start = int(input("start = "))
	end = int(input("end = "))
	for i in range(start,end+1):
		interest = rows[i]
		print("Now Downloading " , interest.find_elements_by_tag_name("td")[0].text)
		down = interest.find_element_by_link_text("Download").click()