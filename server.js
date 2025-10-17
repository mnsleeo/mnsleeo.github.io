const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// 미들웨어
app.use(cors());
app.use(express.json());
app.use(express.static('.')); // 정적 파일 서빙

// Gemini API 호출 함수
async function callGemini(model, prompt) {
    const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${process.env.GEMINI_API_KEY}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            contents: [{
                parts: [{ text: prompt }]
            }],
            generationConfig: {
                temperature: 0.3,
                maxOutputTokens: 1000
            }
        })
    });
    
    if (!response.ok) throw new Error('Gemini API 오류: ' + response.status);
    const data = await response.json();
    return data.candidates?.[0]?.content?.parts?.[0]?.text || '';
}

// API 라우트들
app.post('/api/generate', async (req, res) => {
    try {
        const { prompt, model = 'gemini-1.5-flash' } = req.body;
        const reply = await callGemini(model, prompt);
        res.json({ success: true, reply });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

app.post('/api/recommend', async (req, res) => {
    try {
        const { query, model = 'gemini-1.5-flash' } = req.body;
        const prompt = `다음 요구사항을 분석해서 가장 적합한 AI 도구 3-5개를 추천해주세요. 각 도구마다 구체적인 사용법과 프롬프트 예시를 포함해서 JSON 형태로 답변해주세요.

요구사항: ${query.text}
분야: ${query.domain || '미지정'}
제약사항: ${Object.entries(query.prefs).filter(([k,v]) => v).map(([k]) => k).join(', ') || '없음'}

응답 형식:
[
  {
    "tool": "도구명",
    "reason": "추천 이유",
    "prompt": "구체적인 프롬프트 예시",
    "tips": "사용 팁"
  }
]`;
        
        const reply = await callGemini(model, prompt);
        res.json({ success: true, reply });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

app.listen(PORT, () => {
    console.log(`🚀 서버가 http://localhost:${PORT}에서 실행 중입니다`);
});
