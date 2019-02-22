from terminaltables import AsciiTable


def draw_table(stats_list, title=None):
    table_data = [('Язык программирования',
                   'Вакансий найдено',
                   'Вакансий обработано',
                   'Средняя зарплата')]
    for stat in stats_list:
        language = list(stat.keys())[0]
        vacancies_found = stat[language]['vacancies_found']
        vacancies_processed = stat[language]['vacancies_processed']
        average_salary = stat[language]['average_salary']
        table_data.append(tuple([
            language,
            vacancies_found,
            vacancies_processed,
            average_salary
        ]))
    table = AsciiTable(table_data, title=title)
    return table.table
