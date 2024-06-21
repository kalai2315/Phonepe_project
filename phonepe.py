#Once created the clone of GIT-HUB repository then,
#Required libraries for the program

import pandas as pd
import json
import os
import streamlit as st
from streamlit_option_menu import option_menu
import pymysql
import plotly.express as px
import requests


#This is to direct the path to get the data as states

path = "C:\\Users\\Kalaiselvi\\OneDrive\\Desktop\\Phonepe\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\"

Agg_state_list=os.listdir(path)
Agg_state_list
#Agg_state_list--> to get the list of states in India
#This is to extract the data's to create a dataframe

clm={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for i in Agg_state_list:
    p_i=path+i+"/"
    Agg_yr  =os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
              Name=z['name']
              count=z['paymentInstruments'][0]['count']
              amount=z['paymentInstruments'][0]['amount']
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              
#Succesfully created a dataframe
Agg_Trans=pd.DataFrame(clm)

Agg_Trans["State"] = Agg_Trans["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_Trans["State"] = Agg_Trans["State"].str.replace("-"," ")
Agg_Trans["State"] = Agg_Trans["State"].str.title()
Agg_Trans['State'] = Agg_Trans['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman andDiu")



path_user=path = "C:\\Users\\Kalaiselvi\\OneDrive\\Desktop\\Phonepe\\pulse\\data\\aggregated\\user\\country\\india\\state\\"

Agg_user_list=os.listdir(path_user)
clm_user={'State':[], 'Year':[],'Quarter':[],'Brand':[], 'Transaction_count':[], 'Percentage':[]}

for i in Agg_user_list:
    p_i=path_user+i+"/"
    Agg_yr  =os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D1=json.load(Data)
            try:
              for z in D1["data"]["usersByDevice"]:
                brand=z['brand']
                count=z['count']
                percentage=z['percentage']
                clm_user['State'].append(i)
                clm_user['Year'].append(j)
                clm_user['Quarter'].append(int(k.strip('.json')))
                clm_user['Brand'].append(brand)
                clm_user['Transaction_count'].append(count)
                clm_user['Percentage'].append(percentage)
            except:
                pass
Agg_user=pd.DataFrame(clm_user)


Agg_user["State"] = Agg_user["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_user["State"] = Agg_user["State"].str.replace("-"," ")
Agg_user["State"] = Agg_user["State"].str.title()
Agg_user['State'] = Agg_user['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman andDiu")


path_map = "C:\\Users\\Kalaiselvi\\OneDrive\\Desktop\\Phonepe\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\"

#path_map="/content/pulse/data/map/transaction/hover/country/india/state/"
map_state_list=os.listdir(path_map)
clm_map={'State':[], 'Year':[],'Quarter':[],'T_Amount':[], 'D_Name':[], 'T_Count':[]}

for i in map_state_list:
    p_i=path_map+i+"/"
    Agg_yr  =os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            m_d=json.load(Data)
            #print(m_d)
            #print(m_d["data"]["hoverDataList"][0]["name"])
            #print(m_d["data"]["hoverDataList"][0]["metric"][0]["count"])
            #print(m_d["data"]["hoverDataList"][0]["metric"][0]["amount"])
            for z in m_d["data"]["hoverDataList"]:
                Name=z['name']
                Count=z["metric"][0]["count"]
                Amount=z["metric"][0]["amount"]
                clm_map['State'].append(i)
                clm_map['Year'].append(j)
                clm_map['Quarter'].append(int(k.strip('.json')))
                clm_map['D_Name'].append(Name)
                clm_map['T_Count'].append(Count)
                clm_map['T_Amount'].append(Amount)
Agg_map=pd.DataFrame(clm_map)

Agg_map["State"] = Agg_map["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
Agg_map["State"] = Agg_map["State"].str.replace("-"," ")
Agg_map["State"] = Agg_map["State"].str.title()
Agg_map['State'] = Agg_map['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman andDiu")


map_user="C:\\Users\\Kalaiselvi\\OneDrive\\Desktop\\Phonepe\\pulse\\data\\map\\user\\hover\\country\\india\\state\\"
map_user_list=os.listdir(map_user)
clm_map_user={'State':[], 'Year':[],'Quarter':[],'A_opens':[], 'D_Name':[], 'R_users':[]}

for i in map_user_list:
    p_i=map_user+i+"/"
    Agg_yr  =os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            m_user_d=json.load(Data)
            #print(m_user_d)
            for i in m_user_d["data"]["hoverData"].items():
              #print(i[0])
              #print(i[1]["registeredUsers"])
              #print(i[1]["appOpens"])
              Name=i[0]
              registeredUsers=i[1]["registeredUsers"]
              appOpens=i[1]["appOpens"]
              clm_map_user['State'].append(i)
              clm_map_user['Year'].append(j)
              clm_map_user['Quarter'].append(int(k.strip('.json')))
              clm_map_user['D_Name'].append(Name)
              clm_map_user['R_users'].append(registeredUsers)
              clm_map_user['A_opens'].append(appOpens)
user_map=pd.DataFrame(clm_map_user)


user_map["State"] = user_map["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
user_map["State"] = user_map["State"].astype(str).str.replace("-", " ")
user_map["State"] = user_map["State"].str.title()
user_map['State'] = user_map['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman andDiu")


top_transaction = r"C:\\Users\\Kalaiselvi\\OneDrive\\Desktop\\Phonepe\\pulse\data\\top\\transaction\\country\\india\\state\\"
top_transaction_list = os.listdir(top_transaction)
clm_top_trans={'State':[], 'Year':[],'Quarter':[],'Pincodes':[], 't_count':[], 't_amount':[]}


for i in top_transaction_list:
     p_i=top_transaction+i+"/"
     Agg_yr  =os.listdir(p_i)
     for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            t_trans=json.load(Data) 

            for pincode_data in t_trans["data"]["pincodes"]:
              entityName = pincode_data["entityName"]
              count=pincode_data["metric"]["count"]
              amount=pincode_data["metric"]["amount"]
              clm_top_trans['State'].append(i)
              clm_top_trans['Year'].append(j)
              clm_top_trans['Quarter'].append(int(k.strip('.json')))
              clm_top_trans['Pincodes'].append(entityName)
              clm_top_trans['t_count'].append(count)
              clm_top_trans['t_amount'].append(amount)

trans_top=pd.DataFrame(clm_top_trans)  


trans_top["State"] = trans_top["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
trans_top["State"] = trans_top["State"].str.replace("-"," ")
trans_top["State"] = trans_top["State"].str.title()
trans_top['State'] = trans_top['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman andDiu")
            

top_user="C:\\Users\\Kalaiselvi\\OneDrive\\Desktop\\Phonepe\\pulse\\data\\top\\user\\country\\india\\state\\"
top_user_list = os.listdir(top_user)
clm_top_user={'State':[], 'Year':[],'Quarter':[],'Pincodes':[], 'RegisteredUser':[]}

for i in top_user_list:
     p_i=top_user+i+"/"
     Agg_yr  =os.listdir(p_i)
     for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            t_user=json.load(Data) 

            for pincode_data in t_user["data"]["pincodes"]:
              Name = pincode_data["name"]
              registeredusers = pincode_data["registeredUsers"]
              clm_top_user['State'].append(i)
              clm_top_user['Year'].append(j)
              clm_top_user['Quarter'].append(int(k.strip('.json')))
              clm_top_user['Pincodes'].append(Name)
              clm_top_user['RegisteredUser'].append(registeredusers)
user_top=pd.DataFrame(clm_top_user)               


user_top["State"] = user_top["State"].str.replace("andaman-&-nicobar-islands","Andaman & Nicobar")
user_top["State"] = user_top["State"].str.replace("-"," ")
user_top["State"] = user_top["State"].str.title()
user_top['State'] = user_top['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman andDiu")


mydb = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "Phonepe_pulse",
        autocommit = True
    )
mycursor = mydb.cursor()

mydb.commit()

# Set up database connection parameters
from sqlalchemy import create_engine


user = 'root'
password = 'root'
host = 'localhost'
port = 3306
database = 'Phonepe_pulse'


engine = create_engine(url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        ), echo=False)

# Insert data into MySQL database
Agg_Trans.to_sql('agg_transaction_data', con=engine, if_exists='replace', index=False)
Agg_user.to_sql('agg_user_data', con=engine, if_exists='replace', index=False)
Agg_map.to_sql('map_transaction_data', con=engine, if_exists='replace', index=False)
user_map.to_sql('map_user_data', con=engine, if_exists='replace', index=False)
trans_top.to_sql('top_transaction_data', con=engine, if_exists='replace', index=False)
user_top.to_sql('top_user_data', con=engine, if_exists='replace', index=False)





# Establish MySQL connection
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="Phonepe_pulse",
    autocommit=True
)
mycursor = mydb.cursor()

# Title
st.title("₹PhonePe Pulse 2018-2023 Analysis")

# Define tabs for Transaction and User Analysis
tab1, tab2,tab3 = st.tabs(["TRANSACTION ANALYSIS", "USER ANALYSIS","TOP INSIGHTS"])
with tab1:
    # Subtabs for different levels of analysis
    subtab1, subtab2, subtab3 = st.tabs(["Aggregate Analysis", "State Analysis", "District Analysis"])
with subtab1:
   

    def aggregated_transaction_tab():
        # Aggregate Analysis Subtab
        with subtab1:
            col1, col2, col3 = st.columns(3)

            with col1:
                Year = st.selectbox('Year', ['2018', '2019', '2020', '2021', '2022', '2023'])

            with col2:
                Quarter = st.selectbox('Quarter', ['1', '2', '3', '4'])

            with col3:
                Transaction_type = st.selectbox('Transaction Type',
                                                ['Recharge & bill payments', 'Peer-to-peer payments',
                                                'Merchant payments', 'Financial Services', 'Others'])
                

            with st.expander("Transaction Amount Data"):
                transaction_query = f"""
                SELECT State, Transaction_amount, Transaction_count,Transaction_type
                FROM agg_transaction_data
                WHERE Year = '{Year}' 
                AND Quarter = '{Quarter}'

                AND Transaction_type = '{Transaction_type}'"""

                mycursor.execute(transaction_query)
                transaction_data = mycursor.fetchall()
                mydb.commit()
                transaction_df = pd.DataFrame(transaction_data, columns=['State', 'Transaction_amount','Transaction_count', 'Transaction_type'])
    
                    
                # Visualize data as a bar chart
                fig = px.bar(transaction_df, x='State', y='Transaction_amount', color='Transaction_type',
                            title='Transaction Amount by State', labels={'Transaction_amount': 'Transaction Amount'})
                fig.update_layout(width=800, height=600)
                st.plotly_chart(fig)


            with st.expander("Transaction Count Data"):
                transaction_count_query = f"""
                SELECT State, Transaction_count,Transaction_type
                FROM agg_transaction_data
                WHERE Year = '{Year}' 
                AND Quarter = '{Quarter}'
                AND Transaction_type = '{Transaction_type}'"""

                mycursor.execute(transaction_count_query)
                transaction_count_data = mycursor.fetchall()
                mydb.commit()
                transaction_count_df = pd.DataFrame(transaction_count_data, columns=['State', 'Transaction_count', 'Transaction_type'])

              
                # Visualize data using Plotly Bar Chart
                bar_chart = px.bar(transaction_count_df, x='State', y='Transaction_count', title='Transaction Count by State')
                st.plotly_chart(bar_chart, use_container_width=True)

            
        
            # Visualize data using Plotly Choropleth Map
            choropleth_fig = px.choropleth(transaction_df,
                                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                            locations='State', featureidkey='properties.ST_NM',
                                            color='Transaction_amount', color_continuous_scale='Reds',
                                            title='Transaction Amount by State', hover_name='State',
                                            hover_data=['State',"Transaction_amount",'Transaction_count'] )
        
            choropleth_fig.update_geos(fitbounds="locations", visible=False)
            choropleth_fig.update_layout(title_font=dict(size=25))
            st.plotly_chart(choropleth_fig, use_container_width=True)

        # Transaction Analysis Tab
    with subtab1:
        aggregated_transaction_tab()


with subtab2:
    
    def state_transaction_tab():
        with subtab2:
            col1, col2, col3 = st.columns(3)
            with col1:
                State = st.selectbox('**State**', (
                        'Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 
                        'Chhattisgarh', 'Dadra and Nagar Haveli and Daman andDiu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 
                        'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 
                        'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 
                        'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 
                        'West Bengal'), key='State')

            with col2:
                Year = st.selectbox('**Year**', ('2018', '2019', '2020', '2021', '2022','2023'), key='Year')

            with col3:
                Quarter = st.selectbox('**Quarter**', ('1', '2', '3', '4'), key='Quarter')

                # Fetch transaction data from MySQL
            transaction_query = f"""
            SELECT State, Transaction_amount, Transaction_type,Transaction_count
            FROM agg_transaction_data
            WHERE Year = '{Year}' 
            AND Quarter = '{Quarter}'
            AND State = '{State}'
            """

            # Execute query
            mycursor.execute(transaction_query)
            transaction_data = mycursor.fetchall()

            # Create DataFrame
            df = pd.DataFrame(transaction_data, columns=['State', 'Transaction_amount', 'Transaction_type','Transaction_count'])

       

        # Visualize data using Plotly Choropleth Map
            choropleth_fig = px.choropleth(
            df, geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            locations='State', featureidkey='properties.ST_NM',
            color='Transaction_amount',
            title='Transaction Analysis by State', hover_name='State',
            hover_data=['State', 'Transaction_amount', 'Transaction_count']
        )

            choropleth_fig.update_geos(fitbounds="locations", visible=False)
            choropleth_fig.update_layout(title_font=dict(size=17))
            st.plotly_chart(choropleth_fig, use_container_width=True)

                
        
            with st.expander("Transaction Count by Transaction Type"):
                
                # Plot bar chart for transaction amounts by state
                bar_fig2 = px.bar(df, x='Transaction_type', y='Transaction_count')
                st.plotly_chart(bar_fig2)
        
            with st.expander("Transaction Amount by Transaction Type"):
                # Plot bar chart for transaction amounts by transaction type
                bar_fig = px.bar(
                    df, x='Transaction_type', y='Transaction_amount'
                )
                st.plotly_chart(bar_fig,title_font=dict(size=25), use_container_width=True)

            
            st.write("### Transaction Analysis by Transaction Type")

                        # Apply CSS styling to alternate rows
            st.write("""
            <style>
            .table-striped>tbody>tr:nth-child(odd)>td {
                background-color: #f2f2f2;
            }
            .table-striped>tbody>tr:nth-child(even)>td {
                background-color: #ffffff;
            }
            </style>
            """, unsafe_allow_html=True)
            st.table(df[['Transaction_type', 'Transaction_amount', 'Transaction_count']])
            
            #df_set_index = df[['Transaction_type', 'Transaction_amount', 'Transaction_count']].set_index(pd.Index(range(1, len(df) + 1)))
            #st.table(df_set_index)  

            # Execute query to get total and average transaction amount
            total_amount_query = f"SELECT SUM(Transaction_amount), AVG(Transaction_amount) FROM agg_transaction_data WHERE State = '{State}' AND Year = '{Year}' AND Quarter = '{Quarter}';"
            mycursor.execute(total_amount_query)
            total_amount_data = mycursor.fetchall()
            df_total_amount = pd.DataFrame(total_amount_data, columns=['Total Amount', 'Average Amount'])

            # Execute query to get total and average transaction count
            total_count_query = f"SELECT SUM(Transaction_count), AVG(Transaction_count) FROM agg_transaction_data WHERE State = '{State}' AND Year = '{Year}' AND Quarter = '{Quarter}';"
            mycursor.execute(total_count_query)
            total_count_data = mycursor.fetchall()
            df_total_count = pd.DataFrame(total_count_data, columns=['Total Count', 'Average Count'])

            # Display both DataFrames with "Average" column as index
            st.dataframe(df_total_amount)
            st.dataframe(df_total_count)
    with subtab2:
        state_transaction_tab()     
