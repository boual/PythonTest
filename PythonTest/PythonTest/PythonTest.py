import os

import cloudstorage as gcs

bucket_name = "python_test_app"
bucket = '/' + bucket_name
filename = bucket + '/FichierTestApp'

try:
   create_file(filename)

      
   read_file(filename)

except Exception as e:
   logging.exception(e)


def create_file(filename):

  gcs_file = gcs.open(filename,
                      'w',
                      content_type='text/plain')
  gcs_file.write('Succès\n')
  gcs_file.close()


def read_file(filename):

    gcs_file = gcs.open(filename)
    contents = gcs_file.read()
    gcs_file.close()
    print(contents)
