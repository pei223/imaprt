from django.test import TestCase
from ..views import *
from rest_framework.test import APIRequestFactory


class FilterBatchTest(TestCase):
    def setUp(self):
        self.root_dir = "imaprt_api/tests/"
        self.view = filter_batch

    def test_no_file(self):
        with open(f"{self.root_dir}/test_json/success.json", "r") as file:
            test_params_str = file.read()
        test_data = json.loads(test_params_str)

        request = APIRequestFactory().post("/filter_batch", test_data, format="multipart")
        response = self.view(request)
        self.assertEqual(response.status_code, 400)

    def test_no_filter_params(self):
        test_data = {}
        file_name = f"{self.root_dir}/test.jpg"
        file = open(file_name, "rb")
        test_data["file"] = file

        request = APIRequestFactory().post("/filter_batch", test_data, format="multipart")
        response = self.view(request)
        self.assertEqual(response.status_code, 400)

    def test_invalid_method(self):
        response = self._access_filter_batch(f"{self.root_dir}/test_json/invalid_method.json")
        self.assertEqual(response.status_code, 400)

    def test_invalid_args(self):
        response = self._access_filter_batch(f"{self.root_dir}/test_json/invalid_args.json")
        self.assertEqual(response.status_code, 400)

    def test_valid_request(self):
        response = self._access_filter_batch(f"{self.root_dir}/test_json/success.json")
        self.assertEqual(response.status_code, 200)

    def _access_filter_batch(self, json_file_path: str):
        with open(json_file_path, "r") as file:
            test_params_str = file.read()
        test_data = json.loads(test_params_str)

        file_name = f"{self.root_dir}/test.jpg"
        file = open(file_name, "rb")
        test_data["file"] = file

        request = APIRequestFactory().post("/filter_batch", test_data, format="multipart")
        return self.view(request)
