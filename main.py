import requests
from bs4 import BeautifulSoup



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def get_html(url):
    response = requests.get(url, headers=headers)
    return response.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    page = soup.find('div', class_='pgn').find('table', class_='table__nums table__wrap table_top_border pgn__additional pgn__table').find('tr').find('td',class_='table__cell_last').text.strip()
    return int(page)


def download(url='', name=''):
    try:
        response = requests.get(url=url)

        with open(f'{name}.mp3', 'wb') as file:
            file.write(response.content)
        return f'{name} successfully downloaded! '

    except Exception as _ex:
        return'ups'


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    bloks = soup.find('div', id='main_content').find_all('div', class_= '__adv_list_track')

    for kart in bloks:
        name = kart.find('div', class_='oh').find('a').find('b', class_='m darkblue break-word').text
        url_mp3 =kart.find('div', class_='js-off_hide player_item player_item_old p_i_tools oh').get('data-src').strip()
        print(download(url_mp3,name))
       
  

def main():
    url = 'https://spcs.me/sz/audio/dlja-sms/now/'
    # get_data(get_html(url))
    total_page = get_page_data(get_html(url))
    for page in range(83, total_page+1):
        total_url = url + 'p' + str(page)
        print(f'Обрабатывается {page} страница из {total_page} страниц')
        get_data(get_html(total_url))
        

    

if __name__ == "__main__":
    main()