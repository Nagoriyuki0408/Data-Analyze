import pandas as pd
import os

# 定义文件路径，使用原始字符串避免转义问题
file_path = r'F:\PythonProject2\numpy\youtube_video_data\GB_video_data_numbers.csv'

# 检查文件是否存在
if os.path.exists(file_path):
    try:
        # 尝试使用 UTF-8 编码读取 CSV 文件
        df = pd.read_csv(file_path, encoding='utf-8')
        # 打印 DataFrame 的前几行，用于预览数据
        print(df.head())
    except UnicodeDecodeError:
        # 如果 UTF-8 解码失败，则尝试使用 GBK 编码
        print("UTF-8 decoding failed, trying GBK...")
        try:
            # 尝试使用 GBK 编码读取 CSV 文件
            df = pd.read_csv(file_path, encoding='gbk')
            # 打印 DataFrame 的前几行，用于预览数据
            print(df.head())
        except UnicodeDecodeError:
            # 如果 GBK 解码失败，则尝试使用 Latin-1 编码
            print("GBK decoding failed, trying latin1...")
            try:
                # 尝试使用 Latin-1 编码读取 CSV 文件
                df = pd.read_csv(file_path, encoding='latin1')
                # 打印 DataFrame 的前几行，用于预览数据
                print(df.head())
            except UnicodeDecodeError:
                # 如果所有解码尝试都失败，则提示用户检查文件编码
                print("All decoding attempts failed.  Please check the file encoding.")
    except Exception as e:
        # 捕获其他可能发生的异常，并打印错误信息
        print(f"An error occurred: {e}")
else:
    # 如果文件不存在，则打印错误信息
    print(f"Error: File not found at {file_path}")