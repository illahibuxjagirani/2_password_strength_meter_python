import re
import streamlit as st
import time
st.markdown("""
<style>
.stApp {
    background-color: black17b !important;  /* Light gray */
    background-image: linear-gradient(white,  aqua, white, aqua);
    min-height: 100vh;  /* Ensure full page coverage */
}
</style>
""", unsafe_allow_html=True)



st.markdown("<h1 style='text-align: center; color: blue;'>Password Strength Meter</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'> <span style='background: red; padding: 5px; color: white; '>Very Weak </span> &nbsp; | &nbsp; <span style=' background: pink; padding: 5px; color: black;'>Weak </span> &nbsp; | &nbsp; <span style='padding: 5px; background: yellow; color: black'>Good </span> &nbsp; | &nbsp; <span style='background: lightgreen; padding: 5px; color: black'>Strong </span> &nbsp; | &nbsp; <span style='padding: 5px;color: white; background: green;'>Very Strong </span></p>", unsafe_allow_html=True)

st.markdown("<p style='text-align: right; font-size: 12px; color: black'><strong>ILLAHI BUX (Roll No.249403)</strong></p>", unsafe_allow_html=True)

# st.markdown("<h5>Enter Password to Check the Strength</h5>", unsafe_allow_html=True)
value = 5

password = st.text_input("Enter Password to Check the Strength:", placeholder="Enter Your Password here")

st.markdown(f"<p style='text-align: right; color: black'><span>Length: &nbsp; {len(password)}</p>", unsafe_allow_html=True)


def check_password_strength(password):
    lower_icon = "❌"
    upper_icon = "❌"
    digit_icon = "❌"
    special_icon = "❌"
    length_icon = "❌"
    
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
           
    score = 0
    if re.search(r"[a-z]", password):
        lower_icon = "✅"
        score += 1  
    
    with col2:
        st.markdown(f"<span style='font-size: 15px; color: black;'><strong >{lower_icon} Lower Case</strong></span>", unsafe_allow_html=True)   
    
    if re.search(r"[A-Z]", password):
        score += 1
        upper_icon = "✅"
        
    with col3:
        st.markdown(f"<span style='font-size: 15px; color: black;'><strong >{upper_icon} Upper Case</strong></span>", unsafe_allow_html=True)  
               
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
        digit_icon = "✅"
        
    with col4:
        st.markdown(f"<span style='font-size: 15px;color: black;'><strong >{digit_icon} Digits</strong></span>", unsafe_allow_html=True) 
        
        
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
        special_icon = "✅"

    with col5:
        st.markdown(f"<span style='font-size: 13px; color: black;'><strong >{special_icon} Special Characters </strong></span>", unsafe_allow_html=True) 
    
    
    if len(password) >= 8:
        score += 1  
        length_icon = "✅" 
        
    with col1:
       st.markdown(f"<span style='font-size: 15px; color: black;'><strong >{length_icon} length </strong></span>", unsafe_allow_html=True) 
           
    position = ""
    bcolor = "gray"
    color = "black"
    # Strength Rating
    if score == 5:
        position = "Very Strong"
        bcolor = "green" 
        color = "white" 
        
    if score == 4:
        position = "Strong"
        bcolor = "lightgreen" 
       
       
    elif score == 3:
        position = "Good"
        bcolor = "yellow" 
        
    elif score == 2:
        position = "Weak" 
        bcolor = "pink"  
        
    elif score == 1:
        position = "Very Weak"
        bcolor = "red" 
        color = "white" 
       

    st.markdown(f"<h5 style='background: {bcolor}; color: {color}; margin-bottom: 10px; text-align: center; border-radius: 10px'>{position}</h5>", unsafe_allow_html=True)
    
    
    

    if st.button("Check Password's Strength", use_container_width=True):
        if score == 1:
            st.markdown(f"<p style='background: {bcolor}; color: {color}; margin-bottom: 10px; text-align: center; border-radius: 10px'>Your Password's strength is very Weak, try Strong password and check again</p>", unsafe_allow_html=True)
            
        elif score == 2:
            st.markdown(f"<p style='background: {bcolor}; color: {color}; margin-bottom: 10px; text-align: center; border-radius: 10px'>Your Password's strength is Weak try Strong password and check again</p>", unsafe_allow_html=True)
            
        if score == 3:
            st.markdown(f"<p style='background: {bcolor}; color: {color}; margin-bottom: 10px; text-align: center; border-radius: 10px'>Your Password's strength is Good but i recommend try more Strong password and check again</p>", unsafe_allow_html=True)
    
    if st.button("Save Password", use_container_width=True):
        if score >= 4:
            st.write("Password is being saved please wait.......")
            time.sleep(1)
            st.markdown(f"<p style='background: green; color: white;  text-align: center; border-radius: 50px'>Password Successfully Saved ✅</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='background: {bcolor}; color: {color}; margin-bottom: 10px; text-align: center; border-radius: 10px'>Your Password is Weak try Strong password and Save i</p>", unsafe_allow_html=True)
            
            
    
    
# Get user input



check_password_strength(password)
