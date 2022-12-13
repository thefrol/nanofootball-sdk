# Библиотека для работы с nanofootball.com

Для работы администраторов на Нанофутболе. Позволяет читать и редактировать упражнения и видео из папок. Легко заскриптовать любые рутинные задачи, такие как удалить все видео из папки, найти двойники видео, переименовать кучку видео и прочее. 

## Установка

    pip install nanofootball-sdk

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

В таком случае все сервисы нужно будет создавать вручную указывая апи

    from nanofoot import Api, VideoService

    api=Api(username='my_name@yandex.ru', password='qwerty123.')

    videos=VideoService(api=api)

    for video in videos:
    print(video)
## Как пользоваться

### Видео

    from nanofoot import VideoService

    videos=VideoService()
    print(videos[2554])  # получить видео с id 2554
    videos.patch(2554,name='Новое имя')  # поменять название у того же видео
    videos.delete(2554) # удалить это видео
    

### Упражнения

    from nanofoot import ExerciceService

    exercises=ExercisesService()
    print(exercises[122]) # напечатает упражнение с id 122

    # prints exercise with id 122

    for exercise in exercises['Z3']
        print(exercise) # напечатает все видео из папки Z3
    
    exercises.patch(exs_id=122, title='Новое название')  # поменяет название видео в упражнении 122

### Командная строка

Позволяет выполнять простые фукции с сайтом, создавать, удалять, просматривать видео и упражнения в командной строке

    nf video info 2334
    nf video delete 2334
    nf --help
