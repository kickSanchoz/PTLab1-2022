from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XmlReader(DataReader):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()
        for student in root:
            self.students[student.tag] = []

            for subj in student:
                self.students[student.tag].append(
                    (subj.tag, int(subj.text))
                )

        return self.students
