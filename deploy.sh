#!/bin/bash

echo "🚀 AI Manual 배포 스크립트"
echo "=========================="

# 현재 디렉토리 확인
if [ ! -f "AI manual.html" ]; then
    echo "❌ AI manual.html 파일을 찾을 수 없습니다."
    exit 1
fi

echo "✅ 프로젝트 파일 확인 완료"

# GitHub Pages 배포
echo ""
echo "📦 GitHub Pages 배포 방법:"
echo "1. GitHub에서 새 저장소 생성"
echo "2. 파일들을 업로드"
echo "3. Settings > Pages에서 배포 설정"
echo "4. 브랜치: gh-pages 또는 main/docs"

# Vercel 배포
echo ""
echo "⚡ Vercel 배포 방법:"
echo "1. vercel.com 가입"
echo "2. GitHub 연동"
echo "3. 프로젝트 import"
echo "4. 환경변수 설정: GEMINI_API_KEY"

# Netlify 배포
echo ""
echo "🌐 Netlify 배포 방법:"
echo "1. netlify.com 가입"
echo "2. 드래그 앤 드롭으로 폴더 업로드"
echo "3. 환경변수 설정: GEMINI_API_KEY"

echo ""
echo "🎉 배포 완료 후 다음 URL로 접속 가능:"
echo "- GitHub Pages: https://yourusername.github.io/cursorstudy"
echo "- Vercel: https://ai-manual.vercel.app"
echo "- Netlify: https://ai-manual.netlify.app"

echo ""
echo "📋 배포 체크리스트:"
echo "✅ HTML 파일 확인"
echo "✅ CSS/JS 파일 확인"
echo "✅ API 키 설정"
echo "✅ 환경변수 설정"
echo "✅ 도메인 연결 (선택사항)"
