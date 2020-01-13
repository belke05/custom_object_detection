from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
project_id = 'objectdetector-264912'
display_name = 'my_data'

client = automl.AutoMlClient()

# A resource that represents Google Cloud Platform location.
project_location = client.location_path(project_id, 'us-central1')
metadata = automl.types.ImageObjectDetectionDatasetMetadata()
dataset = automl.types.Dataset(
    display_name=display_name,
    image_object_detection_dataset_metadata=metadata)

# Create a dataset with the dataset metadata in the region.
response = client.create_dataset(project_location, dataset)

created_dataset = response.result()

# Display the dataset information
print(u'Dataset name: {}'.format(created_dataset.name))
print(u'Dataset id: {}'.format(created_dataset.name.split("/")[-1]))
# Dataset name: projects/709347852392/locations/us-central1/datasets/IOD4408903088916660224
# Dataset id: IOD4408903088916660224