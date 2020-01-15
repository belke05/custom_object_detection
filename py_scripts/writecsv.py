# Program to show various ways to read and 
# write data in a file. 
file1 = open("dataset.csv", "w")
L=[]
for x in range(300):
  L.append('UNASSIGNED,gs://object_detector_bucket/elon musk/elon musk_{}.jpeg\n'.format(x))

# \n is placed to indicate EOL (End of Line) 
file1.writelines(L)
file1.close()


