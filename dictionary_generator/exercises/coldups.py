import random

from dictionary_generator.exercises.exercises_abs import ExerciseAbstract


class ColdUp1(ExerciseAbstract):
    _description = '''Заминка1: статические наклоны в стороны
                    растяжка ног в наклоне
                    наклоны с перекрещением ног
                    растяжка рук
                    руки в замок с наклоном
                    наклон вперед с касанием пола
                    стретчинг бицепсов бедер
                    растяжка квадрицепсов
                    стретчинг ягодичных мыщц
                    низкий выпад
                    растяжка в низком выпаде
                    растяжка в боковом выпаде \n'''

    _pulse = [75, 115]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "Легкая одышка",
                        "Немного устал",
                        "Усталость",
                        ]

    def description(self):
        return str(self._description) + "\n"


class ColdUp2(ExerciseAbstract):
    _description = '''Заминка2: наклоны вперед с подъемом рук
                    растяжка ног в полувыпаде
                    наклоны с перекрещением ног
                    растяжка c руками в замок
                    руки в замок с наклоном
                    наклон вперед с касанием пола
                    стретчинг бицепсов бедер
                    статическая растяжка позвоночника
                    растяжка приводящих мышц
                    растяжка в сумо
                    низкий выпад
                    растяжка в позе гирлянды
                    поза собаки мордой вниз \n'''

    _pulse = [75, 125]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "Легкая одышка",
                        "Немного устал",
                        "Усталость",
                        ]

    def description(self):
        return str(self._description) + "\n"