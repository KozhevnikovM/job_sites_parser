import requests, os
from itertools import islice, count
from pprint import pprint


API_KEY=os.getenv('API_KEY')


class SuperJob:
    def __init__(self, params={}):
        self.headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': API_KEY,
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.params = params
        self.data = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                headers=self.headers,
                                params=self.params).json()
        self.total = self.data['total']
        self.vacancies = self.data['objects']

    def fetch_all_pages(self):
        for page in count(0):
            params = self.params
            params['count'] = 100
            total_pages = round(self.total / params['count'])
            page_data = self.data
            if page > total_pages:
                break
            yield from page_data['objects']

    @staticmethod
    def predict_rub_salary(vacancy):
        if not vacancy['currency'] == 'rub':
            return None
        if vacancy['payment_from'] and vacancy['payment_to']:
            return (vacancy['payment_from'] + vacancy['payment_to']) / 2
        if vacancy['payment_from']:
            return vacancy['payment_from'] * 1.2
        if vacancy['payment_to']:
            return vacancy['payment_to'] * 0.8

    def get_average_salary(self):
        vacancies = self.fetch_all_pages()
        salary_list = []
        for vacancy in vacancies:
            if self.predict_rub_salary(vacancy):
                salary_list.append(self.predict_rub_salary(vacancy))
        return {'average_salary': round(sum(salary_list) / len(salary_list), 2),
                'vacancies_processed': len(salary_list)}
