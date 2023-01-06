import urllib.request as urllib

def main(url):
    if 'https://' in url or 'http://' in url:
        pass
    else:
        url = 'https://' + url

    try:
        response = urllib.urlopen(url)
        print('The response code is ', response.getcode())
    except urllib.HTTPError as e:
        print(e)
    except urllib.URLError as e:
        print('Incorrect url')


link = input('Please enter the url to check: ')

main(link)