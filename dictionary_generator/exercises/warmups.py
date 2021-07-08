import random

from dictionary_generator.exercises.exercises_abs import ExerciseAbstract


class WarmUp1(ExerciseAbstract):
    _description = '''Разминка1: Повороты головы
                    Вращение руками
                    Разведение рук для плеч, спины и груди
                    Вращение коленями
                    Вращение тазом
                    Выгибания для спины и позвоночника
                    Наклон в приседе для спины и плеч
                    Наклоны в сторону для пресса и косых мышц
                    Наклоны к полу с разворотом
                    Выпады для разминки ног
                    Вращение ногами
                    Подъемы ног вперед для растяжки ягодиц \n'''

    _pulse = [95, 145]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "Легкая одышка",
                        "Немного устал",
                        "Усталость",
                        ]

    def description(self):
        return str(self._description) + "\n"


class WarmUp2(ExerciseAbstract):
    _description = '''Разминка2: Повороты головы
                    Вращение локтями
                    Сгибание рук для бицепсов и трицепса
                    Разведение локтей для дельт и плечевых суставов
                    Вращение запястьями
                    Вращение плечами
                    Вращения стопой
                    Повороты для пресса и косых мышц
                    Наклоны для задней поверхности бедра
                    Ходьба с подъемом колен
                    Бег на месте с захлестом голени
                    Боковые выпады для разминки ног
                    Подъемы ног для растяжки квадрицепса \n'''

    _pulse = [95, 145]
    _state_of_health = ["Хорошее",
                        "Нормальное",
                        "Легкая одышка",
                        "Немного устал",
                        "Усталость",
                        ]

    def description(self):
        return str(self._description) + "\n"