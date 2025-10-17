# 🔒 API 키 보안 설정 가이드

## ✅ 해결된 문제
- ❌ GitHub에서 API 키 노출 경고
- ✅ API 키를 환경변수로 안전하게 관리
- ✅ 백엔드 API를 통한 안전한 호출

## 🚀 Vercel 배포 시 환경변수 설정

### 1. Vercel 대시보드에서 설정
1. **Vercel 프로젝트** → **Settings** → **Environment Variables**
2. **Name**: `GEMINI_API_KEY`
3. **Value**: `YOUR_GEMINI_API_KEY` (실제 API 키 입력)
4. **Environment**: `Production`, `Preview`, `Development` 모두 선택
5. **Save** 클릭

### 2. CLI로 설정 (선택사항)
```bash
vercel env add GEMINI_API_KEY
# 프롬프트에 API 키 입력
```

## 🔧 프로젝트 구조
```
cursorstudy/
├── AI manual.html          # 프론트엔드 (API 키 없음)
├── pages/
│   └── api/
│       └── generate.js     # 백엔드 API (환경변수 사용)
├── vercel.json            # Vercel 설정
└── package.json           # 프로젝트 설정
```

## 🛡️ 보안 개선사항
- ✅ API 키가 코드에서 완전히 제거됨
- ✅ 환경변수를 통한 안전한 관리
- ✅ GitHub에서 보안 경고 해결
- ✅ 백엔드 API를 통한 프록시 호출

## 📋 배포 체크리스트
- [ ] GitHub에 파일 업로드 (API 키 없음)
- [ ] Vercel 프로젝트 생성
- [ ] 환경변수 `GEMINI_API_KEY` 설정
- [ ] 배포 완료 후 기능 테스트

## 🔍 테스트 방법
1. 배포된 사이트 접속
2. "AI 체험하기" 섹션에서 텍스트 생성 테스트
3. "상황별 AI 추천" 기능 테스트
4. 브라우저 개발자 도구에서 네트워크 탭 확인 (API 키 노출 없음)
