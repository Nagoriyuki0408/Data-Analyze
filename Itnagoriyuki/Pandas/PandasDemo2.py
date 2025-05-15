import pandas as pd

    # 从字典创建 DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']
    }
    df = pd.DataFrame(data)
    print(df)
    # 输出:
    #        Name  Age      City
    # 0     Alice   25  New York
    # 1       Bob   30    London
    # 2  Charlie   28     Paris

    # 从列表的列表创建 DataFrame
    data = [['Alice', 25, 'New York'], ['Bob', 30, 'London'], ['Charlie', 28, 'Paris']]
    df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
    print(df)
    # 输出:
    #        Name  Age      City
    # 0     Alice   25  New York
    # 1       Bob   30    London
    # 2  Charlie   28     Paris