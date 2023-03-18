from enum import Enum
from django.utils.translation import gettext_lazy as _


class FileType(Enum):
    PDF = 1
    excel = 2
    word = 3
    other = 4

    @classmethod
    def choices(cls):
        return [(cls.PDF.value, "PDF"),
                (cls.excel.value, "excel"),
                (cls.word.value, "word"),
                (cls.other.value, "другое")
        ]


class PostCategories(Enum):
    news = 1
    seminar = 2
    speech = 3

    @classmethod
    def choices(cls):
        return [
            (cls.news.value, "Новости"),
            (cls.seminar.value, "Семинары"),
            (cls.speech.value, "Выступления"),
        ]


class DocumentCategories(Enum):
    state_reports = 1
    work_plan = 2
    civil_service = 3
    public_procurement = 4
    relationship_information = 5
    control_measures = 6
    appeal_procedure = 7
    information_about_accepted = 8
    information_about_contributions = 9
    execution_reports = 10
    methodological_support = 11
    regulations = 12
    normative_acts = 13
    corruption = 14
    commission = 15
    anti_corruption_expertise = 16
    income_information = 17
    annual_reports = 18
    agreements = 19


    @classmethod
    def choices(cls):
        return [
            (cls.state_reports.value, "Гос отчеты"),
            (cls.work_plan.value, "План работ"),
            (cls.civil_service.value, "Госслужба"),
            (cls.public_procurement.value, "Госзакупки"),
            (cls.relationship_information.value, "Информация о взаимоотношениях"),
            (cls.control_measures.value, "Контрольные и экспертно-аналитические мероприятия"),
            (cls.appeal_procedure.value, "Порядок обжалования КСО"),
            (cls.information_about_accepted.value, "Информация о принятых по внесённым представлениям и предписаниям решениях и мерах"),
            (cls.information_about_contributions.value, "Информация о внесённых по итогам проведения контрольных и экспертно-аналитических мероприятий представлениях и предписаниях"),
            (cls.execution_reports.value, "Отчеты о исполнений бюджета"),
            (cls.methodological_support.value, "Документы по методологическому обеспечению"),
            (cls.regulations.value, "Нормативные документы"),
            (cls.normative_acts.value, "Нормативные акты"),
            (cls.corruption.value, "Коррупция"),
            (cls.commission.value, "Комиссия (коррупций)"),
            (cls.anti_corruption_expertise.value, "Антикоррупционная экспертиза"),
            (cls.income_information.value, "Сведения о доходах"),
            (cls.annual_reports.value, "Годовые отчеты"),
            (cls.agreements.value, "Соглашения"),
        ]

