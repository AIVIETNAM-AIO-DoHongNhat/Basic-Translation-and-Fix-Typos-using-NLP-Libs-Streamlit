import streamlit as st
from data import EXAMPLES_T, EXAMPLES_S, TARGET_LANGS, SPELL_LANGS
from logic import run_translation, run_spellcheck

st.set_page_config(page_title="NLP Pipeline", layout="centered")
st.title("Streamlit NLP Pipeline")
st.caption("Hai ứng dụng: Dịch văn bản - Sửa lỗi chính tả")
tab_t, tab_s = st.tabs(["Dịch văn bản", "Sửa lỗi chính tả"])

# Dịch văn bản
with tab_t:
    st.session_state.setdefault("res_t", None)
    with st.expander("Ví dụ"):
        for ex in EXAMPLES_T:
            st.markdown(f"- {ex}")

    with st.form("form_translate"):
        text_t = st.text_area(
            "Câu cần dịch",
            height=90,
            placeholder="Nhập câu ở bất kỳ ngôn ngữ nào..."
        )
        target = st.selectbox("Dịch sang", list(TARGET_LANGS.keys()))
        submitted_t = st.form_submit_button("Dịch", type="primary")

    if submitted_t:
        st.session_state.res_t = run_translation(text_t, TARGET_LANGS[target])

    res = st.session_state.res_t

    if res:
        if res["ok"]:
            st.caption(f"Nguồn: {res["source"]} -> Đích: {res["target"]}")
            st.text(res["translated"])
            if res.get("note"):
                st.info(res["note"])
    else:
        st.warning(res["error"])


# Sửa lỗi chính tả
with tab_s:
    st.session_state.setdefault("res_s", None)
    with st.expander("Ví dụ"):
        for ex in EXAMPLES_S:
            st.markdown(f"- {ex}")

    st.caption(f"Hỗ trợ: {', '.join(sorted(SPELL_LANGS))}")
    
    with st.form("form-spell"):
        text_s = st.text_area(
            "Câu cần kiểm tra",
            height=90,
            placeholder="Nhập câu để kiểm tra chính tả...",
        )
        submitted_t = st.form_submit_button("Kiểm tra", type="primary")
    
    if submitted_t:
        st.session_state.res_s = run_spellcheck(text_s)

    res = st.session_state.res_s

    if res:
        if res["ok"]:
            st.caption(f"Ngôn ngữ: {res["language"]}")
            st.text(res["fixed"])
            st.caption("Có sửa lỗi chính tả" if res["changed"] else "Không phát hiện lỗi")
        else:
            st.warning(res["error"])