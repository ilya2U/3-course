def generate_keys(p, q):
    # Вычисление модуля n
    n = p * q
    # Вычисление функции Эйлера от n
    phi = (p - 1) * (q - 1)
    # Выбор открытой экспоненты e
    e = 17
    while phi % e == 0:
        e += 2
    # Вычисление закрытой экспоненты d
    d = pow(e, -1, phi)
    # Возвращение открытого и закрытого ключей
    return ((e, n), (d, n))

def encrypt_message(message, public_key):
    # Разбиение сообщения на символы
    message_symbols = list(message)
    # Кодирование символов в числовой эквивалент
    message_nums = [ord(symbol) - 64 for symbol in message_symbols]
    # Шифрование чисел с помощью открытого ключа
    encrypted_nums = [pow(num, public_key[0], public_key[1]) for num in message_nums]
    # Возвращение зашифрованного сообщения в виде чисел
    return encrypted_nums

def decrypt_message(encrypted_message, private_key):
    # Расшифрование чисел с помощью закрытого ключа
    decrypted_nums = [pow(num, private_key[0], private_key[1]) for num in encrypted_message]
    # Декодирование чисел в символьный эквивалент
    decrypted_symbols = [chr(num + 64) for num in decrypted_nums]
    # Объединение символов в сообщение
    decrypted_message = ''.join(decrypted_symbols)
    # Возвращение расшифрованного сообщения
    return decrypted_message

# Генерация ключей
p = 19
q = 73
public_key, private_key = generate_keys(p, q)

# Шифрование сообщения
message = "Астра"
encrypted_message = encrypt_message(message, public_key)

# Расшифрование сообщения
decrypted_message = decrypt_message(encrypted_message, private_key)

# Вывод результатов
print(f"Открытый ключ: {public_key}")
print(f"Закрытый ключ: {private_key}")
print(f"Зашифрованное сообщение: {encrypted_message}")
print(f"Расшифрованное сообщение: {decrypted_message}")
