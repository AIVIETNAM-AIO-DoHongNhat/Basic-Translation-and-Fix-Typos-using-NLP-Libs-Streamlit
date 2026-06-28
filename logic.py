import langcodes
import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import DetectorFactory, LangDetectException, detect
from nltk.tokenize import TreebankWordDetokenizer, wordpunct_tokenize
from spellchecker import SpellChecker
from config import MIN_INPUT_LENGTH
from data import SPELL_LANGS
from utils import detect_language, language_name, fix_typos

DetectorFactory.seed = 0

# Pipeline dịch văn bản: Pipeline nhận câu đầu vào, nhận diện ngôn ngữ nguồn 
# và dịch sang ngôn ngữ đích do người dùng chọn
def run_translation(text, target_code):
  raw = text.strip()
  if(len(raw) < MIN_INPUT_LENGTH):
    return {
        "ok": False,
        "error": f"Nhập tối thiểu {MIN_INPUT_LENGTH} ký tự."
    }
    
  source_code = detect_language(raw)
  if source_code is None:
    return {
        "ok": False,
        "error": "Không nhận diện được ngôn ngữ."
    }

  if source_code == target_code:
    return {
        "ok": True,
        "source": language_name(source_code),
        "target": language_name(target_code),
        "translated": raw,
        "note": "Câu đã ở ngôn ngữ đích, không cần dịch."
    }

  try: 
    translated = GoogleTranslator(source=source_code, target=target_code).translate(raw)
  except Exception as e:
    return {
        "ok": False,
        "error": f"Lỗi dịch: {e}"
    }

  return {
      "ok": True,
      "source": language_name(source_code),
      "target": language_name(target_code),
      "translated": translated,
  } 

def run_spellcheck(text):
  raw = text.strip()
  if(len(raw) < MIN_INPUT_LENGTH):
    return {
        "ok": False,
        "error": f"Nhập tối thiểu {MIN_INPUT_LENGTH} ký tự."
    }
  
  code = detect_language(raw)
  if code is None:
    return {
        "ok": False,
        "error": "Không nhận diện được ngôn ngữ."
    }
  
  if code not in SPELL_LANGS:
    return {
        "ok": False,
        "error": f"pyspellchecker chưa hỗ trợ {language_name(code)} ({code})."
    }

  fixed, changed = fix_typos(raw, code)

  return {
      "ok": True,
      "language": language_name(code),
      "fixed": fixed,
      "changed": changed,
  }
