import requests
from pprint import pprint
from itertools import count, islice

BASE_URL = 'https://api.hh.ru'


class HeadHunter:
    def __init__(self, params={}):
        self.params = params
        self.data = requests.get(f'{BASE_URL}/vacancies', params=self.params).json()
        self.found = self.data['found']
        self.pages = self.data['pages']

    def fetch_all_pages_items(self):
        for page in count(0):
            params = self.params
            params['page'] = page
            page_data = self.data
            if page >= self.pages:
                break
            yield from page_data['items']

    @staticmethod
    def __predict_rub_salary(vacancy):
        salary = vacancy['salary']
        if not salary or salary['currency'] != 'RUR':
            return None
        if salary['from'] and salary['to']:
            return (salary['from'] + salary['to']) / 2
        if salary['from']:
            return salary['from'] * 1.2
        if salary['to']:
            return salary['to'] / 0.8

    def get_average_salary(self, nums=None):
        if not nums:
            nums = self.found
        vacancies = self.fetch_all_pages_items()
        salary_list = []
        for vacancy in islice(vacancies, nums):
            if self.__predict_rub_salary(vacancy):
                salary_list.append(self.__predict_rub_salary(vacancy))
        return {'average_salary': round(sum(salary_list) / len(salary_list), 2),
                'vacancies_processed': len(salary_list)}
