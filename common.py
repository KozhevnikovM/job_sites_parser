def predict_rub_salary(vacancy):
    if not vacancy['currency'] == 'rub':
        return None
    if vacancy['payment_from'] and vacancy['payment_to']:
        return (vacancy['payment_from'] + vacancy['payment_to']) / 2
    if vacancy['payment_from']:
        return vacancy['payment_from'] * 1.2
    if vacancy['payment_to']:
        return vacancy['payment_to'] * 0.8