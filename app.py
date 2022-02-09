import streamlit as st 
import joblib 
st.title("SPAM HAM CLASSIFICATION")

#load the joblib model 
model = joblib.load('spam-ham')

#ask user input to enter a sentence to check if it is spam or ham 
ip = st.text_input('Enter your message:')

# predict if the entered message is spam or ham 
op = model.predict([ip])
if st.button('PREDICT'):    #create a button called predict, if we click on this button, display if the entered message was spam or ham 
  st.title(op[0])
