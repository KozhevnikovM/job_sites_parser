import requests, os, pprint
from itertools import islice, count
from common import predict_rub_salary


def request_super_job(params={}):
    headers = {
        'Host': 'api.superjob.ru',
        'X-Api-App-Id': os.getenv('API_KEY'),
        'Authorization': 'Bearer r.000000010000001.example.access_token',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers).json()
    return data


def fetch_all_pages(default_params={}):
    response = request_super_job()
    for page in count(0):
        params = {'count': 100}
        total_pages = round(response['total'] / params['count'])
        page_data = response
        if page > total_pages:
            break
        yield from page_data['objects']


def get_average_salary(params={}):
    vacancies = fetch_all_pages(params)
    salary_list = [predict_rub_salary(vacancy) for vacancy in vacancies
                   if predict_rub_salary(vacancy)]
    return {'average_salary': round(sum(salary_list) / len(salary_list), 2),
            'vacancies_processed': len(salary_list)}


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    languages = ['python', 'java', 'ruby', 'javascript']
    search_template = 'программист'
    moscow = 4
    programming_directory_section = 48
    job_stats = []

    for language in languages:
        params = {'t': moscow,
                  'catalogues': programming_directory_section,
                  'keyword': f'{search_template} {language}',
                  }
        super_job = request_super_job()
        pprint.pprint(super_job)

        language_statistics = {language: {
                                    'vacancies_found': super_job['total'],
                                    'vacancies_processed': get_average_salary()['vacancies_processed'],
                                    'average_salary': get_average_salary()['average_salary']
                                    }
                        }
        job_stats.append(language_statistics)
        pprint.pprint(job_stats)


# class SuperJob:
    # def __init__(self, default_params={}):
    #     self.headers = {
    #         'Host': 'api.superjob.ru',
    #         'X-Api-App-Id': API_KEY,
    #         'Authorization': 'Bearer r.000000010000001.example.access_token',
    #         'Content-Type': 'application/x-www-form-urlencoded'
    #     }
    #     self.default_params = default_params
    #     self.data = requests.get('https://api.superjob.ru/2.0/vacancies/',
    #                             headers=self.headers,
    #                             params=self.default_params).json()
    #     self.total = self.data['total']
    #     self.vacancies = self.data['objects']

    # def fetch_all_pages(self):
    #     for page in count(0):
    #         params = {**self.default_params, count:100}
    #         total_pages = round(self.total / params['count'])
    #         page_data = self.data
    #         if page > total_pages:
    #             break
    #         yield from page_data['objects']

    # def get_average_salary(self):
    #     vacancies = self.fetch_all_pages()
    #     salary_list = [predict_rub_salary(vacancy)
    #                    for vacancy in vacancies
    #                    if predict_rub_salary(vacancy)]
    #     return {'average_salary': round(sum(salary_list) / len(salary_list), 2),
    #             'vacancies_processed': len(salary_list)}
