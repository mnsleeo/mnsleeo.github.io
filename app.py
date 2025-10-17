from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# 환경변수에서 API 키 가져오기
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

def call_gemini(model, prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 1000
        }
    }
    
    response = requests.post(url, json=payload)
    response.raise_for_status()
    
    data = response.json()
    return data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')

@app.route('/')
def serve_index():
    return send_from_directory('.', 'AI manual.html')

@app.route('/api/generate', methods=['POST'])
def generate_text():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        model = data.get('model', 'gemini-1.5-flash')
        
        reply = call_gemini(model, prompt)
        return jsonify({'success': True, 'reply': reply})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/recommend', methods=['POST'])
def recommend_tools():
    try:
        data = request.json
        query = data.get('query', {})
        model = data.get('model', 'gemini-1.5-flash')
        
        prompt = f"""다음 요구사항을 분석해서 가장 적합한 AI 도구 3-5개를 추천해주세요. 각 도구마다 구체적인 사용법과 프롬프트 예시를 포함해서 JSON 형태로 답변해주세요.

요구사항: {query.get('text', '')}
분야: {query.get('domain', '미지정')}
제약사항: {', '.join([k for k, v in query.get('prefs', {}).items() if v]) or '없음'}

응답 형식:
[
  {{
    "tool": "도구명",
    "reason": "추천 이유", 
    "prompt": "구체적인 프롬프트 예시",
    "tips": "사용 팁"
  }}
]"""
        
        reply = call_gemini(model, prompt)
        return jsonify({'success': True, 'reply': reply})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
