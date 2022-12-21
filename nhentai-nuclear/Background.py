def button():
    import random
    import requests
    import os

    while True:

        # Creation of the code
        code = ''
        for i in range(6):
            code += str(random.randint(0, 9))
        
        # Creation of the link
        url = 'https://nhentai.to/g/'+ code +'/'
        r = requests.get(url)

        # Launching Chrome if there is a real hentai
        if r.status_code != 404:
            os.system('start chrome --incognito '+'"'+ url +'"')
            break
