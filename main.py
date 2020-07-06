import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def get_friends(name):
    options = Options()
    options.headless = True
    options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options, executable_path=r'D:\files\chromedriver\bin\chromedriver.exe')
    driver.get(f'https://www.faceit.com/en/players/{name}/friends')
    length = 0
    while True:
        driver.execute_script('window.scrollTo(0,1000)')

        ActionChains(driver).key_down(Keys.PAGE_DOWN)

        time.sleep(0.5)
        tags = driver.find_elements_by_tag_name('avatar')
        new_length = len(tags)
        if length == new_length:
            break
        length = new_length
        tag = driver.find_element_by_css_selector('body')
        tag.click()
        tag.send_keys(Keys.END)

    names = [i.get_attribute('img-alt') for i in tags]
    names.remove(name)
    driver.quit()
    return names


def similar_friends2(name1, name2):
    friends1 = get_friends(name1)
    friends2 = get_friends(name2)
    return set(friends1) & set(friends2)


def similar_friends(*args):
    all_friends = []
    print('Working...')
    if len(args) == 1:
        name = args[0]
        friends = get_friends(name)
        print(f'{len(friends)} of {name}\'s friends found.')
        for n, friend in enumerate(friends, start=1):
            friends_friends = get_friends(friend)
            all_friends.append(friends_friends)
            print(f'{n} of {len(friends)} checked. {len(friends_friends)} friend\'s friends added.')

    elif len(args) > 1:
        print(f'Got {len(args)} names for check.')
        for n, friend in enumerate(args, start=1):
            friends_friends = get_friends(friend)
            all_friends.append(friends_friends)
            print(f'{n} of {len(args)} checked. {len(friends_friends)} friend\'s friends added.')
    else:
        return
    number_of_friends_friends = [item for sublist in all_friends for item in sublist]
    print(f'{len(number_of_friends_friends)} friend\'s friends collected.')
    time.sleep(1)
    if all_friends:
        result = set(all_friends[0])
        for friends in all_friends:
            result = result & set(friends)
        if result:
            print('\n', f'Found {len(result)} similar friends: {result}')
        else:
            print('No similar friends found.')
        return result


similar_friends('Toivu')
