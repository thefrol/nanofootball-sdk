# Библиотека для работы с nanofootball.com

## Установка

    pip install .
    pip install nanofoot

## Авторизация

### Через файл nanofootball-credentials.yaml(рекомендуется)
Создайте файл nanofootball-credentials.yaml следующего содержания
    username: my_name@yandex.ru
    password: qwerty111

и положите в домашнюю или локальную папку, тогда при вызову всех апишек можно будет пользоваться просто

    videos=VideoService()
    for video in videos:
        print(video)

### Через код

    from nanofoot import Api
    api=Api(username='my_name@yandex.ru', password='qwerty123.')

В такком случае все сервисы нужно будет создавать вручную указывая апи

    from nanofoot import Api, VideoService

    api=Api(username='my_name@yandex.ru', password='qwerty123.')

    videos=VideoService(api=api)

    for video in videos:
    print(video)

## Видео

    from nanofoot import VideoService
    videos=VideoService()
    print(videos[2554])
    # prints video with id 2554

## Упражнения

    from nanofoot import ExerciceService
    exercises=ExercisesService()
    print(exercises[122])
    # prints exercise with id 122

    for exercise in exercises['Z3']
        print(exercise)
    
    # will print all exercises in Z3 folder

## Командная строка

Позволяет выполнять простые фукции с сайтом, создавать, удалять, просматривать видео и упражнения

    nf video info 2334
    nf video delete 2334
    nf --help