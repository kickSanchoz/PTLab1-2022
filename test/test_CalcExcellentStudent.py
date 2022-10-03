from src.Types import DataType
from src.Types import ExcellentRatingType
from src.CalcExcellentStudent import CalcExcellentStudent
import pytest


class TestCalcExcellentStudent:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, ExcellentRatingType]:
        data: DataType = {
            "Абрамов.Петр.Сергеевич":
                [
                    ("математика", 100),
                    ("программирование", 100),
                    ("физкультура", 100)
                ],

            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }

        excellent_students: ExcellentRatingType = {
            "Абрамов.Петр.Сергеевич": ["математика",
                                       "программирование",
                                       "физкультура"]
        }

        return data, excellent_students

    def test_init_calc_rating(
            self,
            input_data: tuple[DataType, ExcellentRatingType]) -> None:
        # Студенты экземпляра класса CalcExcellentStudent
        excellentStudents = CalcExcellentStudent(input_data[0])
        # Равны ли тестовые данные и данные в экземпляре класса
        assert input_data[0] == excellentStudents.data

    def test_find(self,
                  input_data: tuple[DataType, ExcellentRatingType]) -> None:
        # Все найденные стобалльники
        excellentStudents = CalcExcellentStudent(input_data[0]).find()
        # Равны ли тестовые данные и вычисленные данные
        assert excellentStudents == input_data[1]
