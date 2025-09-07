import streamlit as st

st.title("✅ Streamlit Test with Transformers")
st.write("If you see this, Streamlit is working correctly!")

user_input = st.text_input("Enter some text:")

if st.button("Submit"):
    st.success(f"You entered: {user_input}")

