from threading import Thread
from time import sleep, time

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


start_time = time()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

sequential_duration = time() - start_time
print(f"Время выполнения последовательных вызовов: {sequential_duration:.2f} секунд")


start_time = time()

threads = [
    Thread(target=write_words, args=(10, "example5.txt")),
    Thread(target=write_words, args=(30, "example6.txt")),
    Thread(target=write_words, args=(200, "example7.txt")),
    Thread(target=write_words, args=(100, "example8.txt")),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

parallel_duration = time() - start_time
print(f"Время выполнения потоков: {parallel_duration:.2f} секунд")