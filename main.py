from bs4 import BeautifulSoup
import shutil
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import requests

def createBrowser(url) :

    options = Options()
    options.headless = True

    browser = webdriver.Firefox(options=options)
    browser.get(url)

    return browser

def createSoup(url) :
    browser = createBrowser(url)
    return BeautifulSoup(createBrowser(url).page_source, 'html.parser')

def getImages(url):
    soup = createSoup(url)
    divImages = soup.find(id='divImage')
    return divImages.find_all('img')

def getImagesFromURL():
    url = input("URL de la bande dessinée : ")
    url += "?quality=hq&readType=1"
    return getImages(url)

def getComicsPage():
    comicsName = input("Nom du comic : ")
    return "https://readcomiconline.li/Comic/" + comicsName

def getImagesFromComicsName():
    
    url = getComicsPage()
    soup = createSoup(url)

    

    

def downloadImages(images, chemin=""):
    i = 0

    for img in images:
        i +=1

        response = requests.get(img['src'],stream=True)
        with open(chemin+ "/"+ str(i) + '.png', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response    

def main():

    print("1. Télécharger le comic à partir de l'url")
    print("2. Recherche avec le nom précis")

    choix = input("\nQuelle méthode voulez vos utilisé ?")

    match choix:

        case "1":
            images = getImagesFromURL()
            downloadImages(images, "test2")

        case 2:
            images = getImagesFromComicsName()


    

# options = Options()
# options.headless = True

# browser = webdriver.Firefox(options=options)
# browser.get(url)

# soup = BeautifulSoup(browser.page_source, 'html.parser')
# divImages = soup.find(id='divImage')
# images = divImages.find_all('img')

# i = 0

# for img in images:
#     i +=1

#     response = requests.get(img['src'],stream=True)
#     with open('test/' + str(i) + '.png', 'wb') as out_file:
#         shutil.copyfileobj(response.raw, out_file)
#     del response

# browser.quit()

main()