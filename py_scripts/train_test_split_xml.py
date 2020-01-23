'''

1 --- navigate to directory of this script then execute following sample command
$ python train_test_split_xml.py -d fruitbasket -s 0.7

2 --- 
the d-flag specifies directory name where labeled images in xml and normal jpg and png images reside
the s-flag specifies the size on ratio of 1 which we want our train set to have 

3 -- these sets will be saved in the image directory under the directories train and test 

'''

import os, glob, shutil, time, argparse, math

def createDirectories(imgDirectory):
  test_path = imgDirectory + '/test'
  train_path = imgDirectory + '/train'
  os.mkdir(test_path)
  os.mkdir(train_path)
  return(test_path,train_path)

def openImages(imgDirectory, trainSize):
  os.chdir("../images/" + imgDirectory)
  test_path, train_path = createDirectories(str(os.getcwd()))
  while not os.path.exists(train_path) or not os.path.exists(test_path):
    # wait till directories are created 
    time.sleep(1)
  xml_paths = [xml for xml in glob.glob("*.xml")]
  # find all the xmls 
  xml_path_end_count = int(math.floor(len(xml_paths)*trainSize))
  for xml_train in xml_paths[:xml_path_end_count]:
    try:
      shutil.move(xml_train, train_path)
    except:
      print('failed to move in train')
  for xml_test in xml_paths[xml_path_end_count:-1]:
    try:
      shutil.move(xml_test, test_path)
    except:
      print('failed to move in test')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='directory to find pictures in and size to make it')
  parser.add_argument('-d', '--directory', type=str, help='directory')
  parser.add_argument('-s', '--trainSize', type=float, help='train size')
  args = parser.parse_args()
  openImages(args.directory, args.trainSize)