import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV files
khach_hang_df = pd.read_csv('CustomerData.txt')
marketing_trend_df = pd.read_csv('MarketTrend.txt')
truy_cap_web_df = pd.read_csv('WebsiteData.txt')
san_pham_va_gia_df = pd.read_csv('ProductData.txt')
transaction_df = pd.read_csv('Transaction.txt')
category_df = pd.read_csv('Category.txt')


# 1 Line Chart: Average of EconomicIndicator by Year and Quarter
marketing_trend_df['Date'] = pd.to_datetime(marketing_trend_df['Date'])
marketing_trend_df['Year'] = marketing_trend_df['Date'].dt.year
marketing_trend_df['Quarter'] = marketing_trend_df['Date'].dt.quarter


# Create a line chart
plt.figure(figsize=(12, 6))
plt.plot(marketing_trend_df['Date'], marketing_trend_df['Value'], marker='o')
plt.title('Average of Value by Year, and Quarter')
plt.xlabel('Date')
plt.ylabel('Average of Value')
plt.grid()
plt.show()





# 2. Customer Distribution by Country
plt.figure(figsize=(10, 6))
customer_country_counts = khach_hang_df['Country'].value_counts()
customer_country_counts.plot(kind='bar', color='skyblue')
plt.title('Customer Distribution by Country')
plt.xlabel('Country')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('customer_distribution_by_country.png')
plt.show()



# 3. Website Access by Page()
plt.figure(figsize=(10, 6))
page_access_counts = truy_cap_web_df.groupby('Page')['AccessCount'].sum()
page_access_counts.plot(kind='bar', color='lightgreen')
plt.title('Website Access by Page')
plt.xlabel('Page')
plt.ylabel('Access Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('website_access_by_page.png')
plt.show()



# Tải dữ liệu từ file Category.txt
category_df = pd.read_csv('Category.txt')

# In tên cột và một vài dòng đầu tiên để kiểm tra cấu trúc dữ liệu
print(category_df.columns)
print(category_df.head())

# Đếm số lượng sản phẩm cho mỗi danh mục
category_counts = category_df['CategoryName'].value_counts()

# Vẽ biểu đồ hình tròn
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(category_counts))))
plt.title('Phân phối sản phẩm theo danh mục')
plt.tight_layout()
plt.savefig('category_distribution_pie.png')
plt.show()



marketing_trend_df = pd.read_csv('Dữ liệu market trend.txt')

# In tên cột và một vài dòng đầu tiên để kiểm tra cấu trúc dữ liệu
print(marketing_trend_df.columns)
print(marketing_trend_df.head())

# Đếm số lượng các loại xu hướng (TrendType) cho mỗi loại sản phẩm (ProductID)
# Nếu bạn muốn phân phối theo các loại xu hướng, bạn có thể sử dụng TrendType
trend_counts = marketing_trend_df['TrendType'].value_counts()

# Vẽ biểu đồ hình tròn
plt.figure(figsize=(8, 8))
plt.pie(trend_counts, labels=trend_counts.index, autopct='%1.1f%%', colors=plt.cm.Paired(range(len(trend_counts))))
plt.title('Phân phối các loại xu hướng marketing')
plt.tight_layout()
plt.savefig('marketing_trend_distribution_pie.png')
plt.show()








