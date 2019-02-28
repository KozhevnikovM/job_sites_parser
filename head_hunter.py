import requests
from pprint import pprint
from itertools import count, islice
from common import predict_rub_salary

BASE_URL = 'https://api.hh.ru'


def request_hh(params={}):
    params = params
    data = requests.get(f'{BASE_URL}/vacancies', params=params).json()
    return data


def fetch_all_pages_items(default_params={}):
    pages = request_hh(default_params)['pages']
    for page in count(0):
        params = {**default_params, 'page': page}
        page_data = request_hh(params)
        if page >= pages:
            break
        yield from page_data['items']


def get_average_salary(params, nums=None):
    response = request_hh(params)
    if not nums:
        nums = response['found']
    vacancies = fetch_all_pages_items(params)
    salary_list = [vacancy['salary'] for vacancy in islice(vacancies, nums)]
    args = ['currency', 'RUR', 'from', 'to']
    predicted_salary_list = [predict_rub_salary(salary, *args) for salary in salary_list
              if salary and predict_rub_salary(salary, *args)]
    return {'average_salary': round(sum(predicted_salary_list) / len(predicted_salary_list), 2),
            'vacancies_processed': len(predicted_salary_list)}

if __name__ == '__main__':
    print(request_hh()['pages'])