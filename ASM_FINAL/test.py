import pandas as pd

# Tải dữ liệu từ file CSV vào DataFrame
df = pd.read_csv('file_name.csv')

# Hiển thị vài dòng đầu tiên để kiểm tra dữ liệu
print(df.head())


# Kiểm tra giá trị thiếu trong từng cột
missing_values = df.isnull().sum()

# Hiển thị các cột có giá trị thiếu
print(missing_values[missing_values > 0])


# Điền giá trị thiếu trong cột "Name" bằng "Unknown"
df['Name'].fillna('Unknown', inplace=True)

# Kiểm tra lại dữ liệu để đảm bảo giá trị thiếu đã được xử lý
print(df['Name'].isnull().sum())

import re

# Định nghĩa một hàm để kiểm tra định dạng email hợp lệ
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# Kiểm tra và sửa lỗi các email không hợp lệ
df['Email'] = df['Email'].apply(lambda x: x if is_valid_email(x) else 'invalid@example.com')

# Hiển thị các email sau khi đã được xử lý
print(df['Email'].value_counts())
