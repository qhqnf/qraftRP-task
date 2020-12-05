from timer import log_elapsed_time
import pandas as pd


@log_elapsed_time
def data_query_pandas():
    """
      csv 파일을 읽어오는 데이터는 처리하고자 합니다. 가장 쉽고 빠르게 해볼 수 있는 방법은 pandas 라이브러리를 이용해서 읽어오는 것입니다.
      data.csv 파일 데이터를 읽은 다음, 2017년도, Total Income 중 첫 3개의 산업군에 해당되는 정보를 가져옵니다.

      Task 1. data_query_pandas 함수에 처리 시간을 측정해서 로그파일에 기록하는 decorator 함수, log_elapsed_time 을 완성해 주세요.

    :return:
    """
    data = pd.read_csv("data.csv")
    find = data[(data["Year"] == 2017) & (data["Variable_code"] == "H01")]

    return list(find.iloc[:3]["Value"])


@log_elapsed_time
def custom_datatable():
    """
      data_query_pandas 와 동일한 내용을, pandas같은 라이브러리를 사용하지 않고 직접 class 로 구현하려고 합니다.

      Task 2. DataTable 객체는 find_n 이라는 함수를 완성해 같은 결과가 나오도록 구현해 주세요.
              구현이 완성된 DataTable 은 tests 에 명시된 단위테스트를 통과해야 합니다.
              (평가요소 : 가독성 + 메소드 성능 + 메모리 효율 )

    :return:
    """
    from datatable import DataTable

    data_table = DataTable("data.csv")

    res = []
    for match in data_table.find_n(3, where={"Year": "2017", "Variable_code": "H01",}):
        res.append(match[8])

    return res


if __name__ == "__main__":
    print(data_query_pandas())
    print(custom_datatable())
