# Creare un Generatore Random di Codici Nucleari

# The fucking libreries
import random
import webbrowser

# random integer from 0 to 1 000 000
num1 = random.randint(0, 1000000)
# transform num1 from integer to string
nuclear = str(num1)
# blend the nuclear stonk to the nuclear code
bomb = str("https://nhentai.net/g/" + nuclear)
# open tha' bomb on chrome
webbrowser.open(bomb)  # Go to example.com
