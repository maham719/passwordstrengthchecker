import streamlit as st
import random
import string
import re

def password_strength_checker(password):
    score = 0
    with open('common.txt', 'r') as f:
        common_passwords = f.read().splitlines()
        if password in common_passwords:
            return "❌Password is very common, choose a unique password.", "weak"

    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🔸 Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password): 
        score += 1
    else:
        feedback.append("🔸 Add at least one digit (0-9).")  
    
    if re.search(f"[{re.escape(string.punctuation)}]", password):
        score+=1
    else:
        feedback.append("🔸 include atleast one special character (!@#$%&)")

    if score == 4:
        return "✅strong password" , "strong"
    elif score==3:
        return "⚠ Moderate password ,consider adding more security features.","Moderate"
    else:
        return "\n".join(feedback) ,"weak"
    
check_password=st.text_input("Enter Your Password" , type="password")
if st.button("check strength"):
    if check_password:
      result , Strength = password_strength_checker(check_password)
      if Strength=="strong":
          st.success(result)
      elif Strength == "Moderate":
          st.warning(result)
      else:
          st.error("Weak password try using these tips to improve :")
          for tip in result.split("\n"):
              st.write(tip)

    else:
        st.warning("please enter a password")

def generate_password(Length,use_digits,use_special):
    characters= string.ascii_letters
    if use_digits:
        characters+=string.digits

    if use_special:
        characters+=string.punctuation

    return ' '.join(random.choice(characters) for _ in range(Length))

st.title("Password Generator")
Length= st.slider("Select Password Length" , min_value=6 , max_value=20, value=12)
use_digits=st.checkbox("Include Digits")
use_special=st.checkbox("Include special characters")

if st.button("Generate Password"):
    password=generate_password(Length,use_digits,use_special)
    st.write(f"Generated password {password}")
st.write("------------------")
st.write("Build with ❤ by syeda maham amjad")