# Preparing a custom object detector

<ol>
<li> build small web interface to scroll in google images and download the JPG images</li>
<li> use labelimg to label downloaded images</li>
<li> use train test split pyscript to split xml data in
train and test</li>
<li> use xml to csv to get csvs</li>
<li> use generate TF record to get tf_record files on which you can train a model</li>
<ol>

## 1 download images

- `$ npm run start` will open up the app on localhost 4000
- insert the search term and directory to download to

## 2 label via labelimg / resize if necessary

- less than 200KB each
- resolution < 720x1280.
- use change_img_sizes in this repo if necessary
- `$ python change_img_size.py -d fruitbasket -s 600 600`

## 3 train test split

- `$ python train_test_split_xml.py -d directorWithImages -s 0.8`
- the xml will be split in two folders train (80%) and test

## 4 XML to CSV to generate train and test csv

- `$python xml_to_csv.py -d directorWithImages`
- inside train and test a test_labels.csv and train_labels.csv is made
- inside directorWithImages label_map.pbtxt is auto generated

## 5 move in a clean folder structure

`$ python cleanupfolders.py -d cards`

- images
- - imgdir
- - - train
- - - test
- - - images
- - - label_map.pbtxt

## 5 TF_records

move over all the created files of your image directory to drive
