import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def test_url(name, url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = urllib.request.urlopen(req, context=ctx, timeout=10)
        print(f"[OK] {name}: Status {res.status} ({url})")
        return res
    except Exception as e:
        print(f"[ERRO] {name}: {e} ({url})")
        return None

print("=== TESTANDO SERVIÇOS OBRA IA ===")
test_url("Cloudflare Pages (Home)", "https://obraia.pages.dev")
test_url("Cloudflare Pages (Cadastro)", "https://obraia.pages.dev/cadastro-prestador.html")

res_api = test_url("VPS Backend API Prestadores", "https://consultoriasoft.com.br/api/prestadores")
if res_api:
    try:
        data = json.loads(res_api.read().decode('utf-8'))
        total = len(data.get('prestadores', []))
        print(f"  -> Total de prestadores carregados da API: {total}")
        for p in data.get('prestadores', [])[:3]:
            print(f"     - {p.get('nome_comercial') or p.get('nome_completo')} ({p.get('bairro')})")
    except Exception as e:
        print(f"  -> Erro ao parsear JSON da API: {e}")

print("=== FIM DOS TESTES ===")
