# Made with love by DarkShy
# Инструмент для рассчета подсетей
# Спасибо Владимиру Валентновичу Шальневу за обучение :3

import os
import sys
import socket
import subprocess
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def ping_host(ip, count=2):
    param = '-n' if os.name == 'nt' else '-c'
    command = ['ping', param, str(count), ip]
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return True, output
    except subprocess.CalledProcessError:
        return False, ""

def port_scan(ip, ports, timeout=1):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                result = s.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except (socket.timeout, ConnectionRefusedError):
            continue
        except Exception as e:
            print(f"Ошибка при сканировании порта {port}: {str(e)}")
    return open_ports

def read_ips_from_file(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if validate_ip(line.strip())]
    except Exception as e:
        print(f"Ошибка чтения файла: {str(e)}")
        return []

def main_menu():
    clear_screen()
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("█ SysAdmin Toolkit v1.0 █")
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print("\n1. Проверка доступности хостов")
    print("2. Сканирование портов")
    print("3. Выход")
    choice = input("\nВыберите действие: ")
    return choice

def host_check_menu():
    clear_screen()
    print("=== Проверка доступности хостов ===")
    print("1. Ввести IP-адрес")
    print("2. Загрузить из файла")
    print("3. Назад")
    
    choice = input("\nВыберите источник IP-адресов: ")
    ips = []
    
    if choice == '1':
        ips = input("Введите IP-адрес(а) через пробел: ").split()
    elif choice == '2':
        filename = input("Введите имя файла: ")
        ips = read_ips_from_file(filename)
    else:
        return
    
    log = []
    for ip in ips:
        if validate_ip(ip):
            status, output = ping_host(ip)
            result = f"{ip} {'доступен' if status else 'недоступен'}"
            print(result)
            log.append(f"{datetime.now()} - {result}")
        else:
            error = f"Неверный IP: {ip}"
            print(error)
            log.append(error)
    
    if input("\nСохранить лог? (y/n): ").lower() == 'y':
        with open('ping_log.txt', 'a') as f:
            f.write('\n'.join(log) + '\n')

def port_scan_menu():
    clear_screen()
    print("=== Сканирование портов ===")
    ip = input("Введите IP-адрес: ")
    
    if not validate_ip(ip):
        print("Неверный IP-адрес!")
        return
    
    ports = input("Введите порты (через пробел или диапазон 1-100): ")
    port_list = []
    
    if '-' in ports:
        start, end = map(int, ports.split('-'))
        port_list = list(range(start, end+1))
    else:
        port_list = list(map(int, ports.split()))
    
    print(f"\nСканирование {ip}...")
    open_ports = port_scan(ip, port_list)
    
    if open_ports:
        print("\nОткрытые порты:")
        print(', '.join(map(str, sorted(open_ports))))
    else:
        print("\nОткрытых портов не найдено")
    
    if input("\nСохранить результат? (y/n): ").lower() == 'y':
        with open('port_scan.txt', 'a') as f:
            f.write(f"{datetime.now()} - {ip}\n")
            f.write("Открытые порты: " + ', '.join(map(str, sorted(open_ports))) + '\n\n')

def main():
    while True:
        try:
            choice = main_menu()
            
            if choice == '1':
                host_check_menu()
            elif choice == '2':
                port_scan_menu()
            elif choice == '3':
                print("\nДо свидания!")
                sys.exit(0)
            else:
                print("\nНеверный выбор!")
            
            input("\nНажмите Enter для продолжения...")
        
        except KeyboardInterrupt:
            print("\n\nПрервано пользователем")
            sys.exit(0)
        except Exception as e:
            print(f"\nОшибка: {str(e)}")
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()