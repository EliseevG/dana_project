# dana_project
dos attack protection

Для испытаний требуется:
1) в терминале в директории dana_project командой "docker-compose --build -d" запустить приложение и мониторинг
2) зайти в контейнер attack командой "docker-compose exec attack bash"
3) выполнить команду "python attack.py" (остановить атаку Ctrl+C)
4) посмотреть метрики -  http://localhost:3000

Дополнительные команды:
Остановить контейнер - docker stop <имя контейнера>
Удалить контейнер - docker rm <имя контейнера>
Просмотреть запущенные контейнеры - docker ps (docker ps -a (если хотим посмотреть все существующие контейнеры))
Посмотреть существующие сети docker - docker network ls
Посмотреть логи контейнера - docker logs <имя контейнера>