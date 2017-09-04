import os

model_path = os.environ.get('MODEL_PATH')


def train():
  if not os.path.exists(model_path):
    open(model_path, 'a')


def test():
  pass