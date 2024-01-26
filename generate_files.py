import os
import random
import string

def generate_random_text():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=100))

def create_files(directory, num_files):
    os.makedirs(directory, exist_ok=True)
    for i in range(1, num_files + 1):
        file_path = os.path.join(directory, f"{i}.txt")
        with open(file_path, 'w') as file:
            file.write(generate_random_text())

if __name__ == "__main__":
    create_files("tmp/data", 30)
