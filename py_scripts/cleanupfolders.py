import os, glob, shutil, time, argparse, pathlib


def openImages(imgDirectory):
  print(pathlib.Path.cwd())
  os.chdir("../images/" + imgDirectory)
  print(pathlib.Path.cwd())
  os.mkdir('./pictures')
  print(pathlib.Path.cwd())
  files = os.listdir(pathlib.Path.cwd())
  print(files)
  for f in files:
    if not (f.endswith(".pbtxt")) \
       and not (f.startswith("train")) \
       and not (f.startswith("test")):
      print('moving one image')
      shutil.move(f,'./pictures')
  for train_label_csv in glob.glob('./train/*.csv'):
        shutil.move(train_label_csv, './')
  for test_label_csv in glob.glob('./test/*.csv'):
        shutil.move(test_label_csv, './')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='main directort')
  parser.add_argument('-d', '--directory', type=str, help='directory')
  args = parser.parse_args()
  openImages(args.directory)