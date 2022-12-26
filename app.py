import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import pickle
from sklearn.preprocessing import OrdinalEncoder
encoder=OrdinalEncoder()
        
from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report


data=pd.read_csv("bank-marketing.csv")
def main():
    
    

    st.title("      Bank Marketing Prediction     ")
    


    htk=  """
    <div style="background-color:crimson;padding:0px">
    <h3 style="color:white;text-align:center;">Customer Response Prediction App </h3>
    </div>
    """
   
    model=st.sidebar.selectbox(
    " ML Model",
    ("nothing","Logistic Regression")
    )
    if model=="Logistic Regression":
        if st.checkbox("Modeling"):
        
            klm= """
    
    <h4 style="color:red;text-align:center;"> Top 3 feature columns are taken here to prophesy final output ,after performing EDA and Feature Engineering. </h4>
    
    """
            st.markdown(klm,unsafe_allow_html=True)
        
        housing=st.sidebar.selectbox("apakah customer punya kpr?", ("select",'yes' , 'no'))
        loan=st.sidebar.selectbox("apakah customer punya pinjaman bank?",("select",'yes', 'no'))
        contact=st.sidebar.selectbox("bagaimana cara menghubungi customer",("select","unknown",'Telephone', 'Cellular'))
        if housing!="select" and  loan!="select" and contact!="select":
        
            dict={"yes":'1',"no":'0'}
            for  i, j in dict.items():
                housing=housing.replace(i,j)
                loan=loan.replace(i,j)

            contact_dict={"unknown":'2',"Cellular":'0',"Telephone":'1'}
            for  i, j in contact_dict.items():
                contact=contact.replace(i,j)
        
        
            with open("lr.pkl",'rb') as f:
                lr=pickle.load(f)
        
            res=str(lr.predict([[int(housing),int(loan),int(contact)]]))
            dict={"yes":'1',"no":'0'}    
            for i,j in dict.items():
                res=res.replace(j,i)
        else:
            res="None"
    

          
      
       
        
        

    else:
        res="None"
           
    return res

    

if __name__=='__main__':
    Res=main()
    # Res=str(int(result))
    # dict={"yes":'1',"no":'0'}    
    # for i,j in dict.items():
    #     Res=Res.replace(j,i)
    
            
    if st.sidebar.button("Show Prediction"):
        st.sidebar.subheader("prediksi pelanggan akan deposit")
        st.sidebar.success(Res)
    
    
    
    
    if st.button("Thanks") :
        st.text("Thank you for visiting  and happy learning :)")
        st.balloons()
    
   