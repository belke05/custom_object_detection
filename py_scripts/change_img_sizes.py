'''

1 --- navigate to directory of this script then execute following sample command
$ python change_img_size.py -d fruitbasket -s 600 600

2 --- 
the d-flag specifies directory name where labeled images in xml and normal jpg and png images reside
the s-flag specifies the size we want ot rescale our image to 

3 -- this will save the specified image in the new size 

'''


from PIL import Image,UnidentifiedImageError
import sys
import os, argparse

def rescale_img(directory, size):
  print(directory)
  for i, img in enumerate(os.listdir(directory)):
    try:
      image = Image.open(directory + img)
      im_resized = image.resize(size, Image.ANTIALIAS)
      im_resized.save(directory + img)
    except UnidentifiedImageError as error:
      print(error, '---')
    except:
      if image:
        image.close()
        del image
        os.remove(directory + img)
        print('deleted', i)

    
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='directory to find pictures in and size to make it')
  parser.add_argument('-d', '--directory', type=str, help='directory')
  parser.add_argument('-s', '--size', type=int, nargs=2, required=True, metavar=('width', 'height'), help='Image size')
  args = parser.parse_args()
  print(args.directory, args.size)
  os.chdir("../images/" + args.directory)
  size=args.size
  rescale_img(str(os.getcwd()), size)