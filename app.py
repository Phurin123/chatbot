from flask import Flask, render_template, request, jsonify
from backend import response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])  # เปลี่ยนจาก GET, POST เป็น POST เฉพาะ
def chat():
    # รับข้อความจากฟอร์มในรูปแบบ JSON
    message = request.json.get('msg')  # ใช้ .get() เพื่อดึงข้อมูลจาก JSON
    result = response(message)
    return jsonify({'response': result})  # ส่งคืนคำตอบเป็น JSON

if __name__ == '__main__':
    app.run(debug=True)
