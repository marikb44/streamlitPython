import streamlit as st

st.set_page_config(page_title="Meu Site")

with st.container():
    st.title("Verdades serão ditas:")
    st.subheader("Mariana é FODA!!")
    st.write("Nada além do que todos já sabiam")

with st.container():
    st.write("---")
    st.image('foto.jpg', caption='No tunel do tempo')

with st.container():
    st.write("---")
    uploaded_file = st.file_uploader("Escolha uma imagem", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Exibindo a imagem carregada
        st.image(uploaded_file, caption="Imagem carregada", use_column_width=True)