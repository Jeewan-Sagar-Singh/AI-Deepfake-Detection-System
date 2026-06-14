import os

REAL_PATH = "datasets/real"
FAKE_PATH = "datasets/fake"

real_count = len(os.listdir(REAL_PATH))
fake_count = len(os.listdir(FAKE_PATH))

print("REAL IMAGES =", real_count)
print("FAKE IMAGES =", fake_count)