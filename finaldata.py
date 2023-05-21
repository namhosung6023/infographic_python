import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm

font_location = "C:/13151B114AE7E3A025/malgun.ttf"
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

df = pd.read_csv('C:\data.csv',header=None)

column_sums = df.iloc[:, 2:10].sum()

x_labels = ['검경 사칭', '공공기관 사칭', '가족지인 사칭 ', '금융기관 사칭 ',
            '가족 상해 사칭 ', '허위 문자 ', '몸캠 피싱 ', '피싱 의심 ']
y_values = column_sums.tolist()

plt.bar(x_labels, y_values)
plt.xlabel('사칭 종류')
plt.ylabel('발생 빈도')
plt.title('2021년 ')
plt.xticks(rotation=45)  # x축 레이블 회전
plt.show()




