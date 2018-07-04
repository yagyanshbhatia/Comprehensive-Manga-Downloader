# Comprehensive-Manga-Downloader
This is a python based crawler that allows you to search and download manga of any anime (any chapter). This crawls http://www8.mangafreak.net
## Install Dependencies
`pip3 install selenium fpdf`

Download chomedriver : https://chromedriver.storage.googleapis.com/index.html?path=2.40/
unzip and copy the location of chromedriver in it and assign it to `chromedriver` in `variable.py`

Execute the script by using `python3 go.py`

## Here is an example of the workflow :
Execute the script:

![screenshot from 2018-07-04 10-17-25](https://user-images.githubusercontent.com/26413062/42257652-1ff311b6-7f75-11e8-9ed2-a4a3723834f6.png)

Enter Anime name to be searched , and choose the index from the results:

![screenshot from 2018-07-04 10-18-04](https://user-images.githubusercontent.com/26413062/42257658-220e73be-7f75-11e8-96f2-35bc1cf5250c.png)

Select the chapter or press zero for a range of chapters. 

![screenshot from 2018-07-04 10-19-06](https://user-images.githubusercontent.com/26413062/42257659-23f384a8-7f75-11e8-9762-801934d185ed.png)

Script will download the zips, extract them, convert them to PDFs ready for you to get going :)

![screenshot from 2018-07-04 10-19-51](https://user-images.githubusercontent.com/26413062/42257662-28fe1080-7f75-11e8-99a1-2ecf1bb37199.png)
