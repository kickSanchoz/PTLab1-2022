from Types import DataType
from Types import ExcellentRatingType


class CalcExcellentStudent:

    def __init__(self, data: DataType, maxAvailableRating: int = 100) -> None:
        self.data: DataType = data
        self.maxAvailableRating = maxAvailableRating
        self.excellentStudents: ExcellentRatingType = {}

    def find(self) -> ExcellentRatingType:
        # Флаг того, что какой-нибудь студент добавлен в список
        alreadyAdded = False

        for student in self.data:

            isExcellentStudent = True
            subjects = []

            # Пройтись по всем предметам студента
            for subj in self.data.get(student):
                subjects.append(subj[0])
                # Если хоть один предмет не равен максимально возможному баллу,
                # то студент не считается стобалльником
                if subj[1] != self.maxAvailableRating:
                    isExcellentStudent = False

            # Если студент стобалльник, то вывести все предметы, по которым он
            # имеет максимальный балл
            if isExcellentStudent:
                # Если студент уже был добавлен в список
                if not alreadyAdded:
                    self.excellentStudents[student] = subjects
                    alreadyAdded = True

        return self.excellentStudents
