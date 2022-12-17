def button():
    # from selenium import webdriver
    import random
    import requests
    # import webbrowser
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
        """TODO: Open link in incognito mode"""
        # Opens Chrome in Incognito
        """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        """
        """
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.close()

        while True:
            pass
        """
        # Opens the link
        # webbrowser.open_new_tab(url)

        os.system('start chrome --incognito '+'"'+url+'"')
    else:
        print("Restart")
button()
