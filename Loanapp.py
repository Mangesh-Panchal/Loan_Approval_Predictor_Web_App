import pickle
with open("Loan_Approval_Prediction_Model","rb") as f:
  model= pickle.load(f)


import streamlit as st
st.title("Loan Approval Predictor")
a=st.number_input("ApplicantIncome")
b=st.number_input("CoapplicantIncome")
c=st.number_input("LoanAmount")
d=st.number_input("Loan_Amount_Term")
e=st.number_input("Credit_History")

f = st.selectbox("Select Gender", ["Male","Female"])
g=1
if f=="Female":
    g=0

    
i = st.selectbox("Are you married?", ["No","Yes"])
j=1
k=0
if i=="No":
    j=0

    
l = st.selectbox("Select Education", ["Graduated","Not Graduated"])
m=1
if f=="Graduated":
    m=0


o = st.selectbox("Select No. of dependants", ["0","1","2","3+"])
p=q=r=0

if o=="1":
    p=1
elif o=="2":
    q=1
elif o=="3":
    r=1

t=st.selectbox("Are you Self-Employed", ["No","Yes"])
u=1
if t=="No":
    u=0


w= st.selectbox("Select property", ["Rural","SemiUrban","Urban"])
x=y=0

if w=="SemiUrban":
    x=1
else :
    y=1
    
prediction=model.predict([[a,b,c,d,e,g,j,m,p,q,r,u,x,y]])
button_pressed=st.button("Predict")

if button_pressed:
    if prediction[0]==0:

        st.write("Not Eligible (Loan Not Approved)")
    else:
        st.write("Eligible (Loan Approved)")