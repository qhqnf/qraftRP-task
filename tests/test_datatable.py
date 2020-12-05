import unittest


class TestDatatable(unittest.TestCase):
    def test_1_init(self):
        from datatable import DataTable

        DataTable("data.csv")

        self.assertTrue(True)

    def test_2_wrong_source(self):
        from datatable import DataTable

        with self.assertRaises(FileNotFoundError):
            DataTable("wrong_source.csv")

    def test_3_wrong_field_name(self):
        from datatable import DataTable

        data = DataTable("data.csv")

        with self.assertRaises(KeyError):
            next(data.find_n(3, where={"Year": "2017", "Variable_cod": "H01",}))

    def test_4_find_correct_value(self):
        import pandas as pd
        from datatable import DataTable

        my_data = DataTable("data.csv")
        my_result = []
        for match in my_data.find_n(3, where={"Year": "2017", "Variable_code": "H01"}):
            my_result.append(match[8])

        real_data = pd.read_csv("data.csv")
        real_find = real_data[
            (real_data["Year"] == 2017) & (real_data["Variable_code"] == "H01")
        ]
        real_result = list(real_find.iloc[:3]["Value"])

        self.assertEqual(my_result, real_result)

