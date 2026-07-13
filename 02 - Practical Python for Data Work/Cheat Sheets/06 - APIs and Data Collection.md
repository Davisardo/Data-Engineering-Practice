# Cheat Sheet: APIs and Data Collection

Referensi cepat requests, BeautifulSoup, dan file formats. Pelengkap dari lab [5.1](../5.1%20-%20Introduction%20to%20API/README.md), [5.2](../5.2%20-%20HTTP%20and%20Requests/README.md), [5.3](../5.3%20-%20API%20Examples/README.md), [5.4](../5.4%20-%20Web%20Scraping%20Lab/README.md), [5.5](../5.5%20-%20Working%20with%20Different%20File%20Formats/README.md), dan [5.6](../5.6%20-%20Practice%20Project%20GDP%20Data/README.md).

## Requests — HTTP Methods

**GET — ambil data**
```python
response = requests.get(url)
```

**POST — kirim data baru (BELUM dipraktikkan)**
```python
response = requests.post(url, data={"key": "value"})
```

**PUT — update data yang sudah ada (BELUM dipraktikkan)**
```python
response = requests.put(url, data={"key": "value"})
```

**DELETE — hapus resource (BELUM dipraktikkan)**
```python
response = requests.delete(url)
```

**Query Parameters**
```python
params = {"page": 1, "per_page": 10}
response = requests.get(url, params=params)
```

**Custom Headers (BELUM dipraktikkan) — untuk autentikasi API**
```python
headers = {"Authorization": "Bearer YOUR_TOKEN"}
response = requests.get(url, headers=headers)
```

**Response Handling**
```python
response.status_code   # cek hasil request (200 = sukses, 404 = tidak ditemukan, dst)
response.json()        # parse response JSON jadi dict/list Python
response.text           # response sebagai string mentah
```

---

## BeautifulSoup

**Parsing HTML**
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
```

**find() — elemen PERTAMA yang cocok**
```python
first_link = soup.find('a', {'class': 'link'})
```

**find_all() — SEMUA elemen yang cocok**
```python
all_links = soup.find_all('a', {'class': 'link'})
```

**select() — cari pakai CSS selector (BELUM dipraktikkan)**
```python
titles = soup.select('h1')
```

**findChildren() — semua child element (BELUM dipraktikkan)**
```python
child_elements = parent_div.findChildren()
```

**Navigasi Tree**
```python
element.parent              # elemen parent
element.find_next_sibling() # sibling berikutnya (lebih aman dari next_sibling manual)
```

**Attribute & Text**
```python
href = link_element['href']
text = title_element.text
```

**Tag yang Sering Dicari**
| Tag | Fungsi |
|---|---|
| `a` | Anchor/link |
| `p` | Paragraf |
| `h1`-`h6` | Heading |
| `table`, `tr`, `td`, `th` | Tabel & isinya |
| `img` | Gambar |
| `form`, `button` | Form input |

---

## File Formats

| Format | Baca dengan Pandas |
|---|---|
| CSV | `pd.read_csv()` |
| JSON | `pd.read_json()` |
| Excel | `pd.read_excel()` |
| XML | `pd.read_xml()` |
| HTML Table | `pd.read_html()` |

---

## Method Baru yang Belum Dipraktikkan — Perlu Dieksplor Lebih Lanjut

`POST`, `PUT`, `DELETE`, custom `Headers` (autentikasi), `select()` (CSS selector), `findChildren()`. Ini semua penting untuk interaksi API yang lebih kompleks (modifikasi data di server, bukan cuma baca), dan navigasi HTML yang lebih fleksibel dari `find`/`find_all`.