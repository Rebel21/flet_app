from clients.client import HttpClient


class TimeWebApiClient(HttpClient):
    def __init__(self):
        super().__init__(api_host='https://api.timeweb.cloud/api', api_version='v1', timeout=60)

    def get_servers(self):
        return self.get('/servers').json()

    def get_finance_info(self):
        return self.get('/account/finances').json()


