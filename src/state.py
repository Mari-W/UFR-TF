import json
from multiprocessing import Manager


state = Manager().dict()

with open("data/mapping.json") as f:
  mapping = json.load(f)