
# SysAdmin Toolkit (Python)

Универсальный скрипт для сетевой диагностики и администрирования

## Возможности

### 🖥 Проверка доступности хостов
- Пинг одиночных IP или списка из файла
- Автоматическое определение ОС для корректной команды ping
- Логирование результатов в файл `ping_log.txt`

### 🔦 Сканирование портов
- Проверка отдельных портов или диапазонов
- Быстрое определение открытых/закрытых портов
- Сохранение результатов в файл `port_scan.txt`

### 📋 Дополнительные функции
- Кроссплатформенная работа (Windows/Linux/macOS)
- Интерактивное текстовое меню
- Валидация вводимых IP-адресов
- Обработка прерываний (Ctrl+C)

## Требования

- Python 3.6+
- Стандартные права пользователя
- Сетевой доступ к целевым хостам

## Установка

1. Скачайте файл скрипта:
```bash
wget https://raw.githubusercontent.com/DarkShyMW/sysadminutils/refs/heads/main/portscan.py
```

2. Сделайте скрипт исполняемым (Linux/macOS):
```bash
chmod +x portscan.py
```

3. Запустите:
```bash
python portscan.py
```

## Использование

### Главное меню
```
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█ SysAdmin Toolkit v1.0 █
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

1. Проверка доступности хостов
2. Сканирование портов
3. Выход
```

### Примеры команд
1. **Проверка хостов из файла**:
   - Создайте файл `ips.txt` с IP-адресами
   - Выберите в меню: 1 → 2 → укажите имя файла

2. **Сканирование диапазона портов**:
   ```
   Введите IP-адрес: 192.168.1.1
   Введите порты (через пробел или диапазон 1-100): 80-443
   ```

3. **Экспорт результатов**:
   - После любой операции подтвердите сохранение результатов

## Особенности реализации

- 🚫 **Нет внешних зависимостей** - использует только стандартные библиотеки
- ⚡ **Оптимизированная работа** - асинхронное сканирование портов
- 📅 **Автоматическое логирование** - все результаты с метками времени
- ❌ **Обработка ошибок** - корректная реакция на неверный ввод
- 🔄 **Интерактивный интерфейс** - простое управление через меню

## Пример вывода

### Проверка доступности:
```
192.168.1.1 доступен
8.8.8.8 доступен
10.0.0.5 недоступен
```

### Сканирование портов:
```
Открытые порты: 22, 80, 443
```

## Лицензия
MIT License. Свободное использование и модификация.
