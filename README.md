
# Сетевые инструменты для администрирования

Два Python-скрипта для работы с сетевыми ресурсами:

## 1. 📐 IP Calculator (`ipcalc.py`)
**Основное назначение:** Расчет параметров IPv4-сетей  
**Возможности:**
- Определение сетевого адреса и широковещательного адреса
- Конвертация CIDR ↔ маска подсети
- Расчет количества доступных хостов
- Поддержка специальных сетей (/31, /32)

[Подробная документация](readme-ip.md)

## 2. 🛠️ SysAdmin Toolkit (`portscan.py`)
**Основное назначение:** Диагностика сетевой инфраструктуры  
**Возможности:**
- Массовая проверка доступности хостов (ping)
- Сканирование портов (одиночных/диапазонов)
- Автоматическое логирование результатов
- Кроссплатформенная работа

[Подробная документация](readme-ps.md)

## 🚀 Быстрый старт
**Требования:** Python 3.6+  
**Запуск:**
```bash
# Для калькулятора сетей
python ipcalc.py

# Для набора инструментов
python portscan.py
```

## 🪲 При найденных багах
**Если вы нашли баг - пожалуйста напишите о нем в Issues!**

## 📄 Лицензия
Оба проекта распространяются под лицензией MIT.  
Используйте, модифицируйте и распространяйте свободно.


