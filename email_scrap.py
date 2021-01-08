from google_play_scraper import app

file1 = open('urls.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    try:
        result = app(
            line.strip()[46:],
            country='us'
        )

        print(result['developerEmail'])
        f = open("emails.txt", "a")
        f.write(result['developerEmail'] + '\n')
        f.close()
    except:
        ''
