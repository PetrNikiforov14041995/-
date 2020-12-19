import json
import hashlib

# чтение и запись в файл страна - ссылка
class MyIterator:
    with open("websites.txt", "w") as file:
        with open('countries.json', 'r') as load:
            text = json.load(load)
            for key in text:
                file.write(f"{key['name']['common']} - https://ru.wikipedia.org/wiki/{key['name']['common']}\n")


# возврат md5 hash
def MD5_hash(string, encoding='utf-8'):
    md5_hasher = hashlib.md5()
    md5_hasher.update(string.encode(encoding))
    return md5_hasher.hexdigest()


with open("websites.txt", "r") as f:
    for line in f:
        print(MD5_hash(line))
