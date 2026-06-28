# Basic Translation and Fix Typos using NLP Libs (Streamlit)

> Module 1 - Project 1.1. Web and Streamlit for Simple Deployment (Using NLP Libs)

Ứng dụng web đơn giản xây dựng bằng **Streamlit**, tích hợp hai pipeline NLP cơ bản:

1. **Dịch văn bản** – tự động nhận diện ngôn ngữ nguồn và dịch sang ngôn ngữ đích do người dùng chọn.
2. **Sửa lỗi chính tả** – phát hiện ngôn ngữ và sửa các lỗi chính tả trong câu.

## Tính năng

### Dịch văn bản
- Tự động nhận diện ngôn ngữ nguồn bằng `langdetect`.
- Dịch sang 8 ngôn ngữ đích: Vietnamese, English, French, Japanese, Chinese, Korean, Spanish, German.
- Sử dụng `deep-translator` (Google Translator) để dịch.
- Nếu câu đã ở ngôn ngữ đích thì giữ nguyên, không dịch lại.

### Sửa lỗi chính tả
- Tự động nhận diện ngôn ngữ của câu.
- Sửa lỗi chính tả bằng `pyspellchecker`, giữ nguyên kiểu chữ hoa/thường/viết hoa đầu từ.
- Hỗ trợ 10 ngôn ngữ: `en`, `es`, `fr`, `pt`, `de`, `ru`, `ar`, `eu`, `lv`, `nl`.
- Thông báo rõ khi không phát hiện lỗi hoặc khi ngôn ngữ chưa được hỗ trợ.

## Công nghệ sử dụng

| Thư viện | Vai trò |
|----------|---------|
| [streamlit](https://streamlit.io/) | Xây dựng giao diện web |
| [deep-translator](https://pypi.org/project/deep-translator/) | Dịch văn bản (Google Translator) |
| [langdetect](https://pypi.org/project/langdetect/) | Nhận diện ngôn ngữ |
| [pyspellchecker](https://pypi.org/project/pyspellchecker/) | Sửa lỗi chính tả |
| [nltk](https://www.nltk.org/) | Tách từ / ghép từ (tokenize / detokenize) |
| [langcodes](https://pypi.org/project/langcodes/) + language_data | Hiển thị tên ngôn ngữ đầy đủ |

## Cấu trúc project

```
.
├── app.py            # Giao diện Streamlit (2 tab: Dịch & Sửa lỗi chính tả)
├── logic.py          # Pipeline xử lý: run_translation, run_spellcheck
├── utils.py          # Hàm tiện ích: nhận diện ngôn ngữ, sửa lỗi, tên ngôn ngữ
├── data.py           # Dữ liệu cấu hình ngôn ngữ & ví dụ mẫu
├── config.py         # Hằng số cấu hình (độ dài input tối thiểu)
└── requirement.txt   # Danh sách thư viện cần cài
```

## Cài đặt

### 1. Clone project
```bash
git clone https://github.com/<your-username>/Basic-Translation-and-Fix-Typos-using-NLP-Libs-Streamlit.git
cd Basic-Translation-and-Fix-Typos-using-NLP-Libs-Streamlit
```

### 2. Tạo môi trường ảo (khuyến khích)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 3. Cài đặt thư viện
```bash
pip install -r requirement.txt
```

### 4. Tải dữ liệu NLTK
Ứng dụng dùng `nltk` để tách từ nên cần tải dữ liệu hỗ trợ:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
```

## Chạy ứng dụng

```bash
streamlit run app.py
```

Sau đó mở trình duyệt tại địa chỉ hiển thị trong terminal (mặc định http://localhost:8501).

## Cách sử dụng

**Tab Dịch văn bản**
1. Nhập câu cần dịch (tối thiểu 3 ký tự).
2. Chọn ngôn ngữ đích.
3. Nhấn **Dịch** để xem kết quả cùng ngôn ngữ nguồn được nhận diện.

**Tab Sửa lỗi chính tả**
1. Nhập câu cần kiểm tra (tối thiểu 3 ký tự).
2. Nhấn **Kiểm tra** để xem câu đã được sửa và ngôn ngữ phát hiện.

> Mỗi tab đều có mục **Ví dụ** để bạn thử nhanh.

## Lưu ý
- Tính năng dịch yêu cầu **kết nối Internet** (gọi tới Google Translator).
- Độ chính xác phụ thuộc vào chất lượng nhận diện ngôn ngữ và từ điển của các thư viện.
- Sửa lỗi chính tả chỉ áp dụng cho các ngôn ngữ trong danh sách hỗ trợ.
