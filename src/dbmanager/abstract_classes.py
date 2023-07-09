from abc import ABC, abstractmethod


class DataBase(ABC):

    @abstractmethod
    def __init__(self):
        """Инициализация"""
        pass

    @abstractmethod
    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        pass

    @abstractmethod
    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""
        pass

    @abstractmethod
    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        pass

    @abstractmethod
    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    @abstractmethod
    def get_vacancies_with_keyword(self):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова, например Python"""
        pass
