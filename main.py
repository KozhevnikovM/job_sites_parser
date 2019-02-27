from head_hunter import HeadHunter
from super_job import SuperJob
from draw import draw_table
from dotenv import load_dotenv

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
        hunter = HeadHunter(params)

        lang_statistic = {
                        language: {
                            'vacancies_found': hunter.found,
                            'vacancies_processed': hunter.get_average_salary()['vacancies_processed'],
                            'average_salary': hunter.get_average_salary()['average_salary']
                            }
                        }
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
        super_job = SuperJob(params)

        language_statistics = {language: {
                                    'vacancies_found': super_job.total,
                                    'vacancies_processed': super_job.get_average_salary()['vacancies_processed'],
                                    'average_salary': super_job.get_average_salary()['average_salary']
                                    }
                        }
        job_stats.append(language_statistics)
    print(draw_table(job_stats, title='SuperJob Statistic'))
