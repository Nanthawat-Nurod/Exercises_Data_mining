
####ผมหาไฟล์ csv ตามโจทย์ไม่เจอครับ เลยหาในเน็ตเอา 555

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. สร้าง DataFrame จากข้อมูลนักเรียน
data = {
    'Name': ['สมศรี', 'นันทเวด', 'เกมซ่า', 'ม้าเม็ด', 'น้องแดงดำ'],
    'Age': [18, 22, 20, 19, 21],
    'Grade': ['A', 'B', 'A', 'C', 'B']
}
df = pd.DataFrame(data)
print("1. DataFrame ที่สร้างขึ้น:")
print(df)
print()

# 2. กรองข้อมูลนักเรียนที่มีอายุเกิน 20 ปี
older_students = df[df['Age'] > 20]
print("2. นักเรียนที่มีอายุเกิน 20 ปี:")
print(older_students)
print()

# 3. จัดกลุ่มตามเกรดและคำนวณอายุเฉลี่ย
avg_age_by_grade = df.groupby('Grade')['Age'].mean()
print("3. อายุเฉลี่ยตามเกรด:")
print(avg_age_by_grade)
print()

# 4. สร้าง DataFrame ใหม่ที่มีคะแนนสอบและรวมกับ DataFrame เดิม
new_data = {
    'Name': ['สมศรี', 'นันทเวด', 'เกมซ่า', 'ม้าเม็ด', 'น้องแดงดำ'],
    'Score': [85, 72, 90, 68, 78]
}
df2 = pd.DataFrame(new_data)
merged_df = pd.merge(df, df2, on='Name')
print("4. DataFrame ที่รวมกัน:")
print(merged_df)
print()

# 5. สร้างอาเรย์ NumPy และคำนวณผลรวมและค่าเฉลี่ย
arr = np.arange(1, 11)
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
print("5. อาเรย์ NumPy:")
print(arr)
print('ผลรวม :' + str(np.sum(arr)))  # ผลรวม
print('ค่าเฉลี่ย :' + str(np.mean(arr)))  # ค่าเฉลี่ย

# 6. อ่านข้อมูลจากไฟล์ CSV และแสดง 5 แถวแรก
print("6. ข้อมูล 5 แถวแรกจากไฟล์ CSV:")
df_csv = pd.read_csv('students.csv')
print(df_csv.head())

# 7. บันทึก DataFrame ที่รวมข้อมูลลงในไฟล์ CSV
merged_df.to_csv('students_scores.csv', index=False)
print("7. บันทึกข้อมูลลงในไฟล์ students_scores.csv เรียบร้อยแล้ว")

# 8. สร้างกราฟแสดงคะแนนสอบของนักเรียน
print("8. กำลังสร้างกราฟ...")

# สร้างข้อมูลตัวอย่าง
data = {
    'Name': ['John', 'Emma', 'Alex', 'Sarah', 'Mike'],
    'Score': [85, 92, 78, 95, 88]
}
df_plot = pd.DataFrame(data)

# กราฟเส้น
plt.figure(figsize=(10, 4))
plt.subplot(131)
plt.plot(df_plot['Name'], df_plot['Score'], marker='o')
plt.title('Test Scores (Line Graph)')
plt.xlabel('Student Name')
plt.ylabel('Score')

# กราฟแท่ง
plt.subplot(132)
plt.bar(df_plot['Name'], df_plot['Score'])
plt.title('Test Scores (Bar Graph)')
plt.xlabel('Student Name')
plt.ylabel('Score')

# กราฟวงกลม
plt.subplot(133)
plt.pie(df_plot['Score'], labels=df_plot['Name'], autopct='%1.1f%%')
plt.title('Test Score Distribution (Pie Chart)')


# แสดงกราฟ
plt.show()

