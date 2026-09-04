# Obra IA — Cloudflare Pages & GitHub Deploy Automático

Projeto da plataforma **Obra IA** (`https://obraia.pages.dev`), conectado ao repositório GitHub e integrado em tempo real com a API do backend VPS (`https://consultoriasoft.com.br/api/...`).

---

## 🌐 Links Principais
- **Site no Ar**: [https://obraia.pages.dev](https://obraia.pages.dev)
- **Vitrine de Prestadores**: [https://obraia.pages.dev](https://obraia.pages.dev)
- **Cadastro de Novos Prestadores**: [https://obraia.pages.dev/cadastro-prestador.html](https://obraia.pages.dev/cadastro-prestador.html)
- **Repositório GitHub**: [https://github.com/obraiapagesdev/marketingx](https://github.com/obraiapagesdev/marketingx)
- **Painel Cloudflare Pages**: [https://dash.cloudflare.com/960a35848d3c753d88910be60f947d11/pages/view/obraia](https://dash.cloudflare.com/960a35848d3c753d88910be60f947d11/pages/view/obraia)

---

## 🔐 Credenciais & Acessos
- **Email Proton / GitHub / Cloudflare**: `obraia.pages.dev@proton.me`
- **Usuário GitHub**: `obraiapagesdev`
- **GitHub Personal Access Token (PAT)**: *(Configurado e salvo localmente no arquivo `.env`)*
- **Cloudflare Account ID**: `960a35848d3c753d88910be60f947d11`
- **Cloudflare Pages Project**: `obraia`

---

## 🏗️ Arquitetura & Fluxo de Atualização com IA

```
[Você / IA no Editor]
         │
         ▼
[Edita os arquivos nesta pasta (index.html, etc.)]
         │
         ▼ (Roda deploy.bat ou git push)
[GitHub: obraiapagesdev/marketingx]
         │
         ▼ (Webhook Cloudflare automático em ~15s)
[Cloudflare Pages: obraia.pages.dev]
         │
         ▼ (Requisições /api/ com CORS liberado)
[VPS Backend: https://consultoriasoft.com.br/api/prestadores]
```

---

## 📁 Estrutura de Arquivos desta Pasta
- **`index.html`**: Vitrine principal de prestadores avaliados, busca, filtros de categoria e modo totem.
- **`cadastro-prestador.html`**: Formulário de auto-cadastro com aprimoramento de bio via IA (DeepSeek).
- **`_redirects`**: Regras de redirecionamento e rotas do Cloudflare Pages.
- **`_headers`**: Permissões de CORS (`Access-Control-Allow-Origin: *`) e segurança HTTP.
- **`deploy.bat`**: Script de 1 clique para salvar tudo e enviar pro GitHub / Cloudflare.
- **`deploy.py`**: Script Python para automação programática via IA.
- **`test_site.py`**: Testador automático de integridade do site e das APIs online.

---

## 🚀 Como Fazer Atualizações no Site

### Opção 1: Pedir para a IA
Basta dizer no chat:
> *"Altere a cor do cabeçalho para preto e publique no obraia.pages.dev"*  
A IA edita os arquivos e envia o commit automaticamente.

### Opção 2: Manual pelo Windows
1. Edite o arquivo `index.html`.
2. Dê dois cliques no arquivo `deploy.bat`.
3. Em 15 segundos o Cloudflare Pages publica a versão nova no ar!
