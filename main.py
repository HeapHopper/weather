import streamlit as st
import seaborn as sns
import  matplotlib.pyplot as plt

# Title for the app
st.title("Streamlit Radio Button Example")


st.markdown("""
# Title
## Subtitle

- bullet1
- bullet2
- bullet3

> Amazong quote
""")


# Radio button options
options = ["Option 1", "Option 2", "Option 3"]

# Adding the radio button
choice = st.radio("Choose an option:", options)

# Displaying the result based on user choice
if choice == "Option 1":
    st.write("You selected Option 1! 🎉")
elif choice == "Option 2":
    st.write("You selected Option 2! 🚀")
elif choice == "Option 3":
    st.write("You selected Option 3! 🌟")

# Add any additional content or functionality here
st.write("Feel free to make another selection above!")

df = sns.load_dataset('penguins')
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='flipper_length_mm', y='bill_length_mm', hue='species', ax=ax)
st.pyplot(fig)