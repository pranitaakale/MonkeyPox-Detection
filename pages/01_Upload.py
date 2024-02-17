import streamlit as st
from PIL import Image, ImageFilter
import numpy as np
import cv2
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from functions.functions import filter_records

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title("MonkeyPox Image Classification")
st.markdown("""---""")

with st.container():
    dropdown_col, checkbox_col = st.columns(2)
    with dropdown_col:
        options = ['None', 'Fever', 'Swollen Lymph Nodes', 'Muscle Aches and Pain']
        selected_option = st.selectbox("Select Systemic Illness", options)
    
    with checkbox_col:
        cbox_col1, cbox_col2 = st.columns(2)
        default_value = False

        with cbox_col1:
            Rectal_Pain = st.checkbox("Rectal Pain", value=default_value)
            Sore_Throat = st.checkbox("Sore Throat", value=default_value)
            Penile_Oedema = st.checkbox("Penile Oedema", value=default_value)
        
        with cbox_col2:
            Oral_Lesions = st.checkbox("Oral Lesions", value=default_value)
            Solitary_Lesion = st.checkbox("Solitary Lesion", value=default_value)
            Swollen_Tonsils = st.checkbox("Swollen Tonsils", value=default_value)
            Hiv_Infection = st.checkbox("HIV Infection", value=default_value)

    
    
st.markdown("""---""")

with st.container():
    st.subheader("Upload Image")
    uploaded_file = st.file_uploader("Choose a file",type=["jpg", "jpeg", "png"])
st.markdown("""---""")

if uploaded_file is not None:
    
    
    with st.container():
        st.subheader("Image Analysis")
        col1, col2, col3, col4 = st.columns(4)
    st.markdown("""---""")

    with st.container(): 
        pred_col1, pred_col2 = st.columns(2)
    st.markdown("""---""")
    
    # im= Image.open(uploaded_file)
    original_image = Image.open(uploaded_file)
    grayscale_image = original_image.convert('L')
    edge_image = original_image.filter(ImageFilter.FIND_EDGES)
    img_array = np.array(grayscale_image)
    edge_detection_image = cv2.Canny(img_array, 100, 200)


    with col1:
        st.markdown('<p class="image-font">Original</p>', unsafe_allow_html=True)
        st.image(original_image)
    
    with col2:
        st.markdown('<p class="image-font">GrayScale</p>', unsafe_allow_html=True)
        st.image(grayscale_image)
    
    with col3:
        st.markdown('<p class="image-font">Edge Analysis</p>', unsafe_allow_html=True)
        st.image(edge_image)
    
    with col4:
        st.markdown('<p class="image-font">Edge Detection</p>', unsafe_allow_html=True)
        st.image(edge_detection_image)
    
  
   

    img= np.asarray(original_image)
    image= cv2.resize(img,(224, 224))
    img= preprocess_input(image)
    img= np.expand_dims(img, 0)

    model = load_model('./model_building/saved_model', compile=False)

    predictions = model.predict(img)

    y_hat = model.predict(img)
    # print('pred', y_hat)
    m_labels = ['Monkey Pox Case','Others']
    pred_idx = np.argmax(y_hat[0])
    # print('y =', pred_idx)

    percent_of_pos_record = filter_records(selected_option, Rectal_Pain, Sore_Throat, Penile_Oedema, Oral_Lesions, Solitary_Lesion, Swollen_Tonsils, Hiv_Infection)

    predicted_class_index = np.argmax(predictions)
    predicted_class = m_labels[predicted_class_index]
    probability_scores = predictions[0]

    # pred_idx = (pred_idx+probability_scores)/2

    severityMPox='Nil'
    if probability_scores[0] > .8:
            severityMPox = 'Very High'
    elif probability_scores[0] > .6 and probability_scores[0] < .8:
        severityMPox = 'High'
    elif probability_scores[0] > .5 and probability_scores[0] < .6:
        severityMPox = 'Mild'
    elif probability_scores[0] > .4 and probability_scores[0] < .5:
        severityMPox = 'Low'
    else:
        severityMPox = 'Nil'

    with pred_col1:
        

        # if probability_scores[0] > .8:
        #     isMonkeypox = 'Highly Monkey Pox Case'
        # elif probability_scores[0] > .6 and probability_scores[0] < .8:
        #     isMonkeypox = 'Most Likely Monkey Pox Case'
        # elif probability_scores[0] > .5 and probability_scores[0] < .6:
        #     isMonkeypox = 'Likely Monkey Pox Case'
        # elif probability_scores[0] > .4 and probability_scores[0] < .5:
        #     isMonkeypox = 'Less Likely Monkey Pox Case'
        # else:
        #     isMonkeypox = 'Not a Monkey Pox Case'



        st.subheader("Prediction")
        st.markdown(
             f"""
            <div class="prediction">
                <div class="prediction_title">Detected Class:
                </div>
                <br>
                <div class="prediction_value">{m_labels[pred_idx]}</div>
            </div>
            """
            , unsafe_allow_html=True)
    

    with pred_col2:
        
        st.subheader("Severity") 
        st.markdown(
             f"""
            <div class="prediction">
                <div class="prediction_title">Case Severrity:
                </div>
                <br>
                <div class="prediction_value">{severityMPox}</div>
            </div>
            """
            , unsafe_allow_html=True)

    # with pred_col2:
    #     st.subheader("Probability Scores")
    #     predicted_class_index = np.argmax(predictions)
    #     predicted_class = m_labels[predicted_class_index]
    #     probability_scores = predictions[0]
    #     st.markdown(
    #         f"""
    #         <div class="prediction">
    #             {m_labels[0]} : <label> {format(probability_scores[0]*100, ".5f")} %</label>
    #             <br/>
    #             {m_labels[1]} : <label> {format(probability_scores[1]*100, ".5f")} %</label>
    #         </div>
    #         """
    #         , unsafe_allow_html=True)



