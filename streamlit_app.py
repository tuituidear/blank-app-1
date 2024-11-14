import streamlit as st
import joblib


# โหลดโมเดลจากไฟล์ในโฟลเดอร์ models
@st.cache_resource
def load_model():
    model = joblib.load(ru"/workspaces/blank-app-1/models/model.joblib")
    return model

model = load_model()

# ตัวอย่าง input และการทำนายผล
input_data = st.text_input("กรอกข้อมูลที่ต้องการทำนาย:")

if input_data:
    # ปรับ input_data ตามรูปแบบข้อมูลที่โมเดลต้องการ
    prediction = model.predict([input_data])
    st.write(f"ผลการทำนาย: {prediction}")
