def send(obj, msg):
    obj.write(msg)


class Console:
    def write(self, msg):
        print(msg)


class Buffer:
    def __init__(self):
        self.data = []

    def write(self, msg):
        self.data.append(msg)


console_1 = Console()
console_2 = Console()
buffer = Buffer()
cache = Buffer()

send(console_1, 'Hello!')
send(console_2, 'Bye!')
send(buffer, 'Python')
send(cache, 'Java')
print(buffer.data)
print(cache.data)

print('-' * 100)

send(cache, "Java Script")
print(cache.data)
