'''

1 --- navigate to directory of this script then execute following sample command
$ python xml_to_csv.py -d fruitbasket

2 --- 
the d-flag specifies directory name where labeled images in xml and normal jpg and png images reside

3 -- this will a train csv fail in the train directory and a test csv file in the test directory
     each specifying images and labels for the training of our own model 

'''



import os, glob, argparse
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    parser = argparse.ArgumentParser(description='directory to find pictures in and size to make it')
    parser.add_argument('-d', '--directory', type=str, help='directory')
    args = parser.parse_args()
    os.chdir("../images/" + args.directory)
    for folder in ['train', 'test']:
      image_path = os.path.join(os.getcwd(), folder)
      xml_df = xml_to_csv(image_path)
      xml_df.to_csv(('{0}/{0}_labels.csv'.format(folder)), index=None)
    print('Successfully converted xml to csv.')


main()