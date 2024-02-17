import streamlit as st


# st.title("Streamlit")
# st.subheader("Main Page")

st.set_page_config(page_title='Monkeypox Information', page_icon=':microbe:')
st.title('Monkeypox Information')

# Add information on what monkeypox is
st.header('What is Monkeypox?')
st.write('Monkeypox is a rare viral disease that is similar to human smallpox. It is caused by the monkeypox virus, which is transmitted to people from animals, usually rodents and primates. The disease occurs primarily in remote parts of Central and West Africa, near tropical rainforests.')

# Add information on the symptoms of monkeypox
st.header('Symptoms of Monkeypox')
st.write('The symptoms of monkeypox include fever, headache, muscle aches, backache, swollen lymph nodes, chills, and exhaustion. A rash then develops, often beginning on the face then spreading to the trunk and limbs. The rash changes and goes through different stages before forming a scab, which later falls off.')

# Add information on the treatment and prevention of monkeypox
st.header('Treatment and Prevention of Monkeypox')
st.write('There is no specific treatment for monkeypox. However, the disease is self-limiting and resolves on its own in most cases. Treatment is supportive and includes rest, fluids, and fever control. Vaccination against smallpox has been used to prevent monkeypox, but its effectiveness against monkeypox is not well established. Prevention measures include avoiding contact with animals that may carry the virus, especially rodents and primates, and practicing good hand hygiene.')

# if __name__ == '__main__':
#     main()
