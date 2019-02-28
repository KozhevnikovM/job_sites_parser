import head_hunter
import super_job
from draw import draw_table
from dotenv import load_dotenv


def get_language_statistics(language, vacancies_found, average_salary):
    if not average_salary:
        return {language: {'vacancies_found': vacancies_found,
                           'vacancies_processed': average_salary,
                           'average_salary': average_salary}}

    return {language: {
        'vacancies_found': vacancies_found,
        'vacancies_processed': average_salary['vacancies_processed'],
        'average_salary': average_salary['average_salary']
    }}


if __name__ == '__main__':
    load_dotenv()
    hh_stats = []
    job_stats = []
    search_template = 'программист'
    languages = ['python', 'java', 'ruby', 'javascript']
    moscow = 1
    one_month = 30

    for language in languages:
        params = {'text': f'{search_template} {language}', 'area': moscow, 'period': one_month}
        lang_statistic = get_language_statistics(language,
                                                 head_hunter.request_hh(params)['found'],
                                                 head_hunter.get_average_salary(params)
                                                 )
        hh_stats.append(lang_statistic)

    print(draw_table(hh_stats, title="HeadHunter Statistic"))

    print()

    moscow = 4
    programming_directory_section = 48

    for language in languages:
        params = {'t': moscow,
                  'catalogues': programming_directory_section,
                  'keyword': f'{search_template} {language}',
                  }
        language_statistics = get_language_statistics(language,
                                                      super_job.request_super_job(params)['total'],
                                                      super_job.get_average_salary(params)
                                                      )
        job_stats.append(language_statistics)

    print(draw_table(job_stats, title='SuperJob Statistic'))
