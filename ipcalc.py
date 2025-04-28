# Made with love by DarkShy
# Инструмент для рассчета подсетей
# Спасибо Владимиру Валентновичу Шальневу за обучение :3

def parse_ip(ip_str):
    octets = list(map(int, ip_str.split('.')))
    if len(octets) != 4 or any(o < 0 or o > 255 for o in octets):
        raise ValueError("Неверный IP-адрес")
    return octets

def is_valid_mask(mask):
    binary = ''.join(format(o, '08b') for o in mask)
    seen_zero = False
    for bit in binary:
        if bit == '0':
            seen_zero = True
        elif seen_zero and bit == '1':
            return False
    return True

def cidr_to_mask(cidr):
    if cidr < 0 or cidr > 32:
        raise ValueError("Неверный CIDR")
    mask = [0, 0, 0, 0]
    for i in range(cidr):
        mask[i//8] |= (1 << (7 - i % 8))
    return mask

def mask_to_cidr(mask):
    binary = ''.join(format(o, '08b') for o in mask)
    cidr = binary.count('1')
    if not is_valid_mask(mask):
        raise ValueError("Неверная маска подсети")
    return cidr

def ip_to_str(ip):
    return '.'.join(map(str, ip))

def calculate_network(ip, mask):
    return [ip[i] & mask[i] for i in range(4)]

def calculate_broadcast(network, mask):
    inverse_mask = [255 - mask[i] for i in range(4)]
    return [network[i] | inverse_mask[i] for i in range(4)]

def main():
    while True:
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("█ SysAdmin Toolkit v1.0 █")
        print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        try:
            user_input = input("\nВведите IP и маску (формат: IP/CIDR или IP маска): ").strip()
            if user_input.lower() in ('exit', 'quit'):
                print("Выход из программы")
                break
            
            if '/' in user_input:
                ip_part, cidr_part = user_input.split('/')
                cidr = int(cidr_part)
                mask = cidr_to_mask(cidr)
            else:
                parts = user_input.split()
                if len(parts) != 2:
                    raise ValueError("Неверный формат ввода")
                ip_part, mask_part = parts
                mask = parse_ip(mask_part)
                if not is_valid_mask(mask):
                    raise ValueError("Неверная маска подсети")
                cidr = mask_to_cidr(mask)
            
            ip = parse_ip(ip_part)
            network = calculate_network(ip, mask)
            broadcast = calculate_broadcast(network, mask)
            
            # Расчет количества хостов
            if cidr <= 30:
                host_count = (2 ** (32 - cidr)) - 2
            elif cidr == 31:
                host_count = 2
            elif cidr == 32:
                host_count = 1
            else:
                host_count = 0
            
            # Определение диапазона хостов
            if cidr < 31:
                first_host = network.copy()
                first_host[3] += 1
                last_host = broadcast.copy()
                last_host[3] -= 1
            elif cidr == 31:
                first_host = network
                last_host = broadcast
            else:
                first_host = network
                last_host = network

            print("\nРезультаты расчета:")
            print(f"IP-адрес: {ip_to_str(ip)}")
            print(f"Маска сети: {ip_to_str(mask)} (CIDR /{cidr})")
            print(f"Сетевой адрес: {ip_to_str(network)}")
            print(f"Широковещательный адрес: {ip_to_str(broadcast)}")
            print(f"Доступно хостов: {host_count}")
            print(f"Диапазон хостов: {ip_to_str(first_host)} - {ip_to_str(last_host)}")
        
        except ValueError as e:
            print(f"Ошибка: {e}")
        except KeyboardInterrupt:
            print("\nВыход из программы")
            break
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    main()