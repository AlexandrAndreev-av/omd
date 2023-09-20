import requests
city_code = 524901
appid = "c92c4c562b53abd196e2c8a20bf2ea48"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={
    'id': city_code,
    'lang': 'ru',
    'APPID': appid
})

data = res.json()


def step2_umbrella():
    print(
        "На улице", data['weather'][0]['description']
    )


def step2_no_umbrella():
    print(
        'Попасть под дождь не самое страшное в жизни'
    )


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар.'
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
