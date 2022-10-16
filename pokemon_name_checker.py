from bs4 import BeautifulSoup
import os, requests

headers =  {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.42 Safari/537.36 Edg/77.0.235.17"}
file = open('pokemon.txt', 'r') #This text document has the list of Pokemon names with spaces and special characters if they have any
out = open('times.txt', 'w') #Output file
for line in file:
    try:
        line = line.replace('\n', '')
        print(line)
        page = requests.get('https://lols.gg/en/name/checker/na/' + line, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        name_box = soup.find('h4', attrs={'class': 'text-center'}) #This line approximates the number of days to wait unless avaliable
        name = name_box.text
        out.write(name + '\n') #Writes to output file
    except:
        out.write(line + 'has an error. Try again!\n')

file.close()
out.close()
