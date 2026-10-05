from abc import ABC, abstractmethod
import requests as _http_requests


class requests(ABC):
    @staticmethod
    @abstractmethod
    def get(url, params=None, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def post(url, data=None, json=None, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def put(url, data=None, json=None, **kwargs):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def delete(url, **kwargs):
        raise NotImplementedError


class HTTPRequests(requests):
    @staticmethod
    def get(url, params=None, **kwargs):
        response = _http_requests.get(url, params=params, **kwargs)
        response.raise_for_status()
        return response

    @staticmethod
    def post(url, data=None, json=None, **kwargs):
        response = _http_requests.post(url, data=data, json=json, **kwargs)
        response.raise_for_status()
        return response

    @staticmethod
    def put(url, data=None, json=None, **kwargs):
        response = _http_requests.put(url, data=data, json=json, **kwargs)
        response.raise_for_status()
        return response

    @staticmethod
    def delete(url, **kwargs):
        response = _http_requests.delete(url, **kwargs)
        response.raise_for_status()
        return response


requests = HTTPRequests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data["results"]
