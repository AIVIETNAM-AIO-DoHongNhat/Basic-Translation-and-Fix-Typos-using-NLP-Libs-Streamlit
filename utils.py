import streamlit as st
import langcodes
from spellchecker import SpellChecker
from langdetect import detect, LangDetectException
from nltk.tokenize import TreebankWordDetokenizer, wordpunct_tokenize

# Tải từ điển của ngôn ngữ đó rồi lưu vào cache
@st.cache_resource(show_spinner=False)
def get_spellchecker(code):
  return SpellChecker(language=code)

# Trả về tên của ngôn ngữ viết tắt đó, ví dụ "en" --> English
def language_name(code):
  try:
    return langcodes.get(code).display_name()
  except Exception:
    return code or "Unknow"

# Từ dữ liệu đưa vô, phát hiện xem đó là ngôn ngữ gì
def detect_language(raw):
  try:
    return detect(raw)
  except LangDetectException:
    return None
  
# Hàm sửa lỗi chính tá
def fix_typos(text, code):
  spell = get_spellchecker(code)
  tokens = wordpunct_tokenize(text) # Tách các từ ra và trả về []
  fixed = []
  for token in tokens:
    if token.isalpha() and len(token) > 1:
      suggestion = spell.correction(token.lower()) or token
      suggestion = suggestion.title() if token.istitle() else suggestion
      suggestion = suggestion.upper() if token.isupper() else suggestion
      fixed.append(suggestion)
    else:
      fixed.append(token)
  # Hoàn nguyên văn bản (detokenization)
  return TreebankWordDetokenizer().detokenize(fixed), fixed != tokens