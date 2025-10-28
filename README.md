# dana_project
dos attack protection
для испытаний требуется:
1) создать docker образ web-приложения  командой: docker build -t app . (нужно находит ьв директории app)
2) создать docker образ приложения Dos- атаки командой: docker build -t attack .  (нужно находит ьв директории attack)
3) создать docker-сеть  командой: docker --network my-network
4) запустить контейнеры приложений командами:
    docker run -d -p 5000:5000 --name app-container --network my-network app
    docker run -d --name attack-container --network my-network attack
5) Проверить логи контейнера атаки командой: docker logs attack-container

Дополнительные команды:
Оставноить контейнер - docker stop <имя контейнра>
Удалить контейнер - docker rm <имя контейнера>
Просмотреть запущенные контейнеры - docker ps (docker ps -a (если хотим посмотреть все существующие контейнеры))