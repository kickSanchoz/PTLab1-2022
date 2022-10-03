import pytest
from src.Types import DataType
from src.XmlReader import XmlReader


class TestXmlReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "<root>" \
               "<Иванов.Константин.Дмитриевич>" \
               "<математика>91</математика>" \
               "<химия>100</химия>" \
               "</Иванов.Константин.Дмитриевич>" \
               "<Петров.Петр.Семенович>" \
               "<программирование>87</программирование>" \
               "<литература>78</литература>" \
               "</Петров.Петр.Семенович>" \
               "</root>"

        data = {
            "Иванов.Константин.Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров.Петр.Семенович": [
                ("программирование", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        # Создаёт xml файл
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        # Записывает туда данные "text" из file_and_data_content
        p.write_text(file_and_data_content[0], encoding='utf-8')
        # Возвращает xml файл и "data" из file_and_data_content
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        # Парсит контент из файла
        file_content = XmlReader().read(filepath_and_data[0])
        # Сравнивает контент из файла и "data" из file_and_data_content
        assert file_content == filepath_and_data[1]
