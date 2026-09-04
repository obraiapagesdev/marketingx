@echo off
chcp 65001 > nul
echo ======================================================
echo    OBRA IA - Deploy Automatico para Cloudflare Pages
echo ======================================================
echo.

cd /d "%~dp0"

echo [1/3] Verificando arquivos alterados...
git status -s

echo.
echo [2/3] Adicionando e criando commit...
set /p MENSAGEM="Digite a mensagem do deploy (ou pressione ENTER para mensagem padrao): "
if "%MENSAGEM%"=="" set MENSAGEM=Atualizacao automatica Obra IA

git add .
git commit -m "%MENSAGEM%"

echo.
echo [3/3] Enviando para GitHub (Dispara deploy no Cloudflare Pages)...
git push origin main

echo.
echo ======================================================
echo  Deploy enviado com sucesso!
echo  O Cloudflare Pages atualizara em ~15 segundos em:
echo  https://obraia.pages.dev
echo ======================================================
pause
