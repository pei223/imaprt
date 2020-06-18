import requests
import json


class FilterChaint():
    def test_filter_batch(self):
        with open("test_json/success.json", "r") as file:
            test_params_str = file.read()
        test_data = json.loads(test_params_str)

        file_name = "test.jpg"
        file_data_binary = open(file_name, "rb")
        files = {"file": file_data_binary}

        header = {"Content-Type": "multipart/form-data"}

        url = "http://localhost:8000/imaprt_api/filter_batch"
        response = requests.post(url, files=files, data=test_data)
        print(response.content.decode())

FilterChaint().test_filter_batch()


