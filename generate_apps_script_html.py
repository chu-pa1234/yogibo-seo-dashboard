"""
現在の index.html から埋め込みデータを除去し、
Apps Script テンプレート変数に置き換えてindex_apps_script.htmlを生成する
"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print(f'元ファイルサイズ: {len(html):,} bytes')

# ── GA4_DATA を テンプレート変数に置換 ──
html = re.sub(
    r'const GA4_DATA = \[.*?\];',
    'const GA4_DATA = <?!= ga4Data ?>;',
    html, flags=re.DOTALL
)
print('GA4_DATA 置換完了')

# ── ARTICLE_TRAFFIC_DATA を テンプレート変数に置換 ──
html = re.sub(
    r'const ARTICLE_TRAFFIC_DATA = \{.*?\};',
    'const ARTICLE_TRAFFIC_DATA = <?!= articleData ?>;',
    html, flags=re.DOTALL
)
print('ARTICLE_TRAFFIC_DATA 置換完了')

# ── SEO_DATA を テンプレート変数に置換 ──
html = re.sub(
    r'const SEO_DATA = \[.*?\];',
    'const SEO_DATA = <?!= seoData ?>;',
    html, flags=re.DOTALL
)
print('SEO_DATA 置換完了')

# ── Apps Script 用: <base> タグを追加（相対パス解決のため） ──
# Apps Script は独自URLで配信されるため不要な場合はスキップ

print(f'変換後サイズ: {len(html):,} bytes')
print(f'削減: {(1 - len(html)/700000)*100:.0f}% 程度')

with open('index_apps_script.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('保存: index_apps_script.html')
