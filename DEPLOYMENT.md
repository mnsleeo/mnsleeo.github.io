# AI Manual 배포 가이드

## GitHub Pages 배포

### 1. GitHub 저장소 생성
1. GitHub에서 새 저장소 생성
2. 파일들을 업로드
3. Settings > Pages에서 배포 설정

### 2. 자동 배포 설정
- `gh-pages` 브랜치 사용
- 또는 `main` 브랜치의 `/docs` 폴더 사용

### 3. 도메인 설정
- 커스텀 도메인 연결 가능
- HTTPS 자동 적용

## Vercel 배포 (추천)

### 1. Vercel 계정 생성
- [vercel.com](https://vercel.com) 가입
- GitHub 연동

### 2. 프로젝트 배포
```bash
# Vercel CLI 설치
npm i -g vercel

# 배포
vercel --prod
```

### 3. 환경변수 설정
- Vercel 대시보드에서 `GEMINI_API_KEY` 설정
- 자동 HTTPS 적용

## Netlify 배포

### 1. Netlify 계정 생성
- [netlify.com](https://netlify.com) 가입
- GitHub 연동

### 2. 드래그 앤 드롭 배포
- 폴더를 Netlify에 드래그
- 자동 배포 완료

### 3. 환경변수 설정
- Site settings > Environment variables
- `GEMINI_API_KEY` 추가

## Firebase Hosting

### 1. Firebase 프로젝트 생성
- [firebase.google.com](https://firebase.google.com) 가입

### 2. Firebase CLI 설치
```bash
npm install -g firebase-tools
firebase login
firebase init hosting
```

### 3. 배포
```bash
firebase deploy
```

## 무료 호스팅 옵션 비교

| 서비스 | 무료 한도 | 도메인 | HTTPS | 자동 배포 |
|--------|-----------|--------|-------|-----------|
| GitHub Pages | 무제한 | 커스텀 가능 | ✅ | ✅ |
| Vercel | 100GB/월 | 커스텀 가능 | ✅ | ✅ |
| Netlify | 100GB/월 | 커스텀 가능 | ✅ | ✅ |
| Firebase | 10GB/월 | 커스텀 가능 | ✅ | ✅ |
