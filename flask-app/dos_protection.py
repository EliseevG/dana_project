import time
from collections import defaultdict


class DOSProtection:
    def __init__(self, max_requests=5, window_seconds=1):
        self.max_requests = max_requests  # Максимум запросов
        self.window_seconds = window_seconds  # Временное окно
        self.requests_log = defaultdict(list)  # Хранение временных меток

    def is_allowed(self, client_ip):
        """Проверяет, разрешен ли запрос от client_ip"""
        current_time = time.time()

        # Удаляем старые записи вне временного окна
        self.requests_log[client_ip] = [
            timestamp for timestamp in self.requests_log[client_ip]
            if current_time - timestamp < self.window_seconds
        ]

        # Проверяем количество запросов
        if len(self.requests_log[client_ip]) < self.max_requests:
            self.requests_log[client_ip].append(current_time)
            return True
        return False
