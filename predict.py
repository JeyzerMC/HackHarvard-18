import sys

from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2


def get_prediction(content, project_id, model_id):
    prediction_client = automl_v1beta1.PredictionServiceClient()
        
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content }}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request  # waits till request is returned
#sees whether prediction mmatches the tag
if __name__ == '__main__':
    file_path = sys.argv[1]
    file_path = "/Users/alaashamandy/Desktop/Work/Development/hackharvard/HackHarvard-18/cropped.jpg"
    project_id = "storied-port-220005"
    model_id = "ICN6771425939369298234"
    
    with open(file_path, 'rb') as ff:
        content = ff.read()

    print(get_prediction(content, project_id,  model_id))
    
