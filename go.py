from selenium import webdriver
import os
import time
import zipfile
from fpdf import FPDF
from variables import chromedriver

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': os.getcwd()}
chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

name = input("Enter the name of Anime to search - ").lower()
name = name.split()
driver.get("http://www8.mangafreak.net/Search/" + '%20'.join(name))

while (1):
    try:
        done = driver.find_element_by_link_text("Home")
        break
    except Exception as e:
        time.sleep(1)
        continue

result = driver.find_elements_by_class_name("manga_search_item")
for r in result:
    print(r.text)

index = int(input("Enter Index of anime to proceed - "))
index-=1
interest = result[index]
link = interest.find_element_by_tag_name("a")
link.click()


lists = driver.find_element_by_class_name("manga_series_list")
rows = lists.find_elements_by_tag_name("tr")
for index, val in enumerate(rows):
    print(index, "\t=>\t", val.text)

i = int(input("Which index chapter do you want to download? (zero if a range is needed) "))
if i != 0:
    interest = rows[i]
    print("Now Downloading ", interest.find_elements_by_tag_name("td")[0].text)
    down = interest.find_element_by_link_text("Download").click()
else:
    print("Enter range of chapters to download (inclusive)")
    start = int(input("start = "))
    end = int(input("end = "))
    for i in range(start, end + 1):
        interest = rows[i]
        down = interest.find_element_by_link_text("Download").click()
        print("Now Downloading ", interest.find_elements_by_tag_name("td")[0].text)

time.sleep(1)

driver.get('chrome://downloads')
while True:
    for item in driver.find_elements_by_css_selector('body/deep/downloads-item'):
        if 'pause' in item.text.lower():
            time.sleep(2)
            break
    else:
        break

def natural_keys(text):
    c = text.split(".")[0].split('_')[-1]
    return int(c)

listFiles = []
cwd = os.getcwd()
for file in os.listdir(cwd):
    if file.endswith(".zip"):
        listFiles.insert(1, str(file))

listFiles.sort(key=natural_keys)
for file in listFiles:
    path = file.split('.')[0]
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        try:
            zip_ref = zipfile.ZipFile(os.path.join(cwd, file), 'r')
            zip_ref.extractall(path)
            zip_ref.close()

            mypath = os.path.join(cwd,path)
            onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

            def natural_keys_1(text):
                c = text.split(".")[0].split('_')[-1]
                return int(c)

            onlyfiles.sort(key=natural_keys_1)
            pdf = FPDF()
            for image in onlyfiles:
                pdf.add_page()
                pdf.image(mypath + '/' + image, 0, 0, w=210, h=297)
            pdf.output(file.split('.')[0] + ".pdf", "F")
        except:
            continue