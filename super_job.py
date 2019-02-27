import requests, os
from itertools import islice, count
from common import predict_rub_salary


API_KEY=os.getenv('API_KEY')


class SuperJob:
    def __init__(self, default_params={}):
        self.headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': API_KEY,
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.default_params = default_params
        self.data = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                headers=self.headers,
                                params=self.default_params).json()
        self.total = self.data['total']
        self.vacancies = self.data['objects']

    def fetch_all_pages(self):
        for page in count(0):
            params = {**self.default_params, count:100}
            total_pages = round(self.total / params['count'])
            page_data = self.data
            if page > total_pages:
                break
            yield from page_data['objects']


    def get_average_salary(self):
        vacancies = self.fetch_all_pages()
        salary_list = []
        for vacancy in vacancies:
            if self.predict_rub_salary(vacancy):
                salary_list.append(self.predict_rub_salary(vacancy))
        return {'average_salary': round(sum(salary_list) / len(salary_list), 2),
                'vacancies_processed': len(salary_list)}
