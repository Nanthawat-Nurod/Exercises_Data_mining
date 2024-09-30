import pandas as pd
import numpy as np

#1. จัดการกับค่า Missing Values ในคอลัมน์ children จากไฟล์ customers.csv
customers_df = pd.read_csv('customers.csv')
print("ข้อมูล Missing ในคอลัมน์ children ก่อนจัดการ(customers.csv):")
print(customers_df['children'].isnull().sum())
customers_df['children'] = customers_df['children'].fillna(customers_df['children'].mean())
print("ข้อมูล Missing ในคอลัมน์ children หลังจัดการ:(customers.csv)")
print(customers_df['children'].isnull().sum())

#คำอธิบาย:
#อ่านข้อมูลจากไฟล์ customers.csv และใช้ฟังก์ชัน isnull().sum() เพื่อตรวจสอบจำนวน Missing Values ในคอลัมน์ children
#ใช้ฟังก์ชัน fillna() แทนค่าที่ขาดหายด้วยค่าเฉลี่ยของคอลัมน์ children (mean())

#2. นำเข้าชุดข้อมูล sample_data.csv และตรวจสอบข้อมูลเบื้องต้น
sample_df = pd.read_csv('sample_data.csv')
print("5 แถวแรกของข้อมูล(sample_data.csv):")
print(sample_df.head())
print("ข้อมูลสถิติพื้นฐาน(sample_data.csv):")
print(sample_df.describe())

#3. จัดการกับค่า Missing Values ในคอลัมน์ Age และ Salary
print("จำนวน Missing Values ในแต่ละคอลัมน์(sample_data.csv):")
print(sample_df.isnull().sum())
sample_df['Age'] = sample_df['Age'].fillna(sample_df['Age'].mean())
sample_df['Salary'] = sample_df['Salary'].fillna(sample_df['Salary'].mean())
print("จำนวน Missing Values หลังจัดการ(sample_data.csv):")
print(sample_df.isnull().sum())

#4. แปลงข้อมูลและสร้างคอลัมน์ใหม่ Age_Group
sample_df['Salary'] = pd.to_numeric(sample_df['Salary'], errors='coerce')
bins = [0, 18, 35, 60, np.inf]
labels = ['Youth', 'Adult', 'Senior', 'Elder']
sample_df['Age_Group'] = pd.cut(sample_df['Age'], bins=bins, labels=labels)
print("ข้อมูลหลังการแปลงคอลัมน์ Age_Group(sample_data.csv):")
print(sample_df[['Age', 'Age_Group']].head())
