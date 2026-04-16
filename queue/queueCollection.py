from collections import deque

custom_queue = deque(maxlen=10)

custom_queue.append(1)
custom_queue.append(2)
custom_queue.append(3)
custom_queue.append(4)
custom_queue.append(5)
custom_queue.append(6)
custom_queue.append(7)
custom_queue.append(8)

print(custom_queue)

print(custom_queue.popleft())

print(custom_queue)