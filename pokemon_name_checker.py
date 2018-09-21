from bs4 import BeautifulSoup
import urllib, urllib2, os

file = open('pokemon.txt', 'r') #This text document has the list of Pokemon names with spaces and special characters if they have any
out = open('times.txt', 'w') #Output file
for line in file:
    try:
        page = urllib2.urlopen('https://lolnames.gg/en/na/' + line)
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find('h4', attrs={'class': 'text-center'}) #This line approximates the number of days to wait unless avaliable
        name = name_box.text.strip()
        out.write(name + '\n') #Writes to output file
    except:
        out.write(line + 'has an error. Try again!\n')

file.close()
out.close()

os.system('quit')
