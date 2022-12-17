def button():
    import random
    import requests
    import os
    
    def Generate_Code():
        # Creation of the Code
        code = ''
        for i in range(6):
            code += str(random.randint(0, 9))
        # Creation of the link
        url = 'https://nhentai.to/g/'+ code +'/'
        return url
    Generate_Code()

    url=Generate_Code()

    # Receive the status code
    r = requests.get(url)

    # Check if the status code is not 404
    if r.status_code != 404:
        os.system('start chrome --incognito '+'"'+url+'"')
    else:
        print("Restart")
button()
