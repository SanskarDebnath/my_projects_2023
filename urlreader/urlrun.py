import webbrowser as wb
def fileOpen(fileVal):
    try:
            myFile = open(fileVal,"r")
            fileRead(myFile)
    except:
            print("file not found!") 

def fileRead(fileContent):    
    openfile = fileContent.read()
    urlList = openfile.split("\n")
    while True:
        if '' in urlList:
            urlList.remove('')
        else:
            break
    urlRun(urlList)        

def urlRun(urlCount):            
    for url in urlCount:
        try:
           wb.open_new_tab(url)
        except:
            print(f"the url {url} is broke!")
    
def main():
    fileName = "C:\\Users\\adity\\OneDrive\\Documents\\programming\\python\\myProjects\\urlreader\\myurl.txt"
    fileOpen(fileName)

if __name__ == '__main__':
     main()    


