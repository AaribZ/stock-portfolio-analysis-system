import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(
    layout="wide",
    page_title="Stock Portfolio Analysis & Management System")
#arranging title
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1 style='font-size:90px;'>Stock Portfolio Management and Analysis System</h1>
    </div>
""", unsafe_allow_html=True)
#arranging subtitle and name
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1 style='font-size:37px;'>Advanced Analytical Tools for Informed Investment Decisions</h1>
        <h1 style='font-size:20px;'>By Aarib Zaidi</h1>
    </div>
""", unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
#aligning image1
image_url = "NASDAQ.webp"
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write("")
with col2:
    st.image(image_url, caption="NASDAQ is the most active stock trading venue in the U.S. by volume and second on the list of stock exchanges by market capitalization of shares traded globally")
with col3:
    st.write("")
st.markdown('#')
st.divider()
st.markdown('#')
#intro
st.markdown("""
     <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
    <h2 style='font-size:60px;'>Introduction to Stock Portfolio Analysis</h2>
    <h2 style='font-size:22px;'>Stock portfolio analysis involves a comprehensive evaluation of the performance and potential of a collection of stocks held by an investor. This critical process helps investors make informed decisions about buying, holding, or selling stocks, ultimately aiming to maximize returns and minimize risk. By analyzing key metrics and trends, such as historical price movements, earnings reports, and market conditions, investors can gain deeper insights into the strengths and weaknesses of their portfolios. Additionally, portfolio analysis allows for the identification of diversification opportunities and risk management strategies. Through thorough analysis and informed decision-making, investors can optimize their portfolios to better align with their financial goals and investment strategies. This allows such investors to gain enhanced returns and increased efficiency due to proper optimization as well as managing risks and goal allignement.</h2>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
#aligning image2
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2:
    st.image("stocks.webp", width=1000)
with col3:
    st.write()
st.markdown('#')
#my project overview
st.markdown("""
     <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
    <h2 style='font-size:60px;'>Project Overview</h2>
    <h2 style='font-size:22px;'>In this data analysis project, I developed an interactive app which displays both basic and advanced analysis of the stock data alongside numerous visual representations of the data; all of which was coded in python. Firstly, I conducted basic data analysis on both stock profiles; mainly consisting of summary statistics of each column. After that, I generated visual graphs which assisted in displaying the correlation between various datasets. I employed diagrams such as bar charts, line graphs, pie charts, scatter plots and a correlation matrix; all of which present data in a concise and coherent manner. Finally, I performed advanced analysis on the more complex data columns which helped unravel the more obscure pattern within our dataset. Once the backend coding was complete, I moved on to developing the interface through which the user could view my data analysis. I used a software called Streamlit which simplifies the process of developing apps; something that really helped me as I am currently not as proficient at CSS and HTML than I am at Python. Through Streamlit, I was able to easily produce my own web app which clearly displayed all my data analysis in a straightforward  manner. Overall, the project was very enjoyable and I fully enjoyed my time at Bank AL-Habib Limited and Teresol. Thank you! 
    </div>
  """, unsafe_allow_html=True)  
st.markdown('#')
#aligning image3
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2:
    st.image("analysis.webp", width=900)
with col3:
    st.write()
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:60px;'>Would you like to view the original data set?</h1>
        <h1 style='font-size:22px;'>If so, please click on the button below: </h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
#aligning button
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    st.write(' ')
with col2:
    st.write(' ')
with col3:
    st.link_button("NASDAQ Stock Data and Stock Market Summary Statistics", "https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset/data")
with col4:
    st.write (' ')
with col5:
    st.write(' ')
st.markdown('#')
st.divider()
st.markdown('#')
#title
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1 style='font-size:85px;'>NASDAQ Stock Data</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
#aligning image4
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2:
    st.image("stocksss.png", caption="This is a screenshot of the first few columns in the 8049-column-long NASDAQ stock market dataset",width=1050)
with col3:
    st.write()
st.markdown('#')
st.markdown('#')
st.markdown('#')
#basic data analysis started
#no. of unique stocks
st.divider()
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 1) Stocks Listed</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>The number of unique stocks listed on NASDAQ were:</h1> ,  
        <h1 style='font-size:50px;'>8049</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')    
st.markdown('#')
st.divider()
#distribution of stocks across listing exchanges
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 2) Listing Exchange</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')    
st.markdown('#')
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Choose one of the following listing exchanges:</h1>
    </div>
  """, unsafe_allow_html=True)
x = st.selectbox('There are 5 listing exchanges: A, N, P, Q, Z. After clicking on one, the number of stocks on that listing exchange will be displayed.',[' ','A','N','P','Q','Z'])
st.markdown('#')
st.markdown('#')
if x is ('A'):
  st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>There are 253 unique stocks on this listing exchange.</h1>
    </div>
  """, unsafe_allow_html=True)
if x is ('N'): 
     st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>There are 2520 unique stocks on this listing exchange.</h1>
    </div>
  """, unsafe_allow_html=True)
if x is ('P'):
   st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>There are 1542 unique stocks on this listing exchange.</h1>
    </div>
  """, unsafe_allow_html=True) 
if x is ('Q'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>There are 3383 unique stocks on this listing exchange.</h1>
    </div>
  """, unsafe_allow_html=True) 
if x is ('Z'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>There are 351 unique stocks on this listing exchange.</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
st.markdown('#')
st.markdown('#')
#listing exchange bar graph
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Relationship Between Listing Exchange and Number of Stocks:</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
st.markdown('#')
data={"Listing Exchange":['Q','N','P','Z','A' ],"Number of Stocks":[3383, 2520, 1542, 351, 253]}
data=pd.DataFrame(data)
data=data.set_index("Listing Exchange")
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2:
    st.bar_chart(data,width=1200)
with col3:
    st.write()
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#market categories
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 3) Market Categories</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
#market categories percentages on pie graph
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>The Percentage of Stocks Across Different Market Categories:</h1>
    </div>
  """, unsafe_allow_html=True) 
market_category = ['Q','S','G']
weights = [1531, 952, 900,] 
explode = (0.03, 0.03, 0.03)
fig1, ax1 = plt.subplots()
ax1.pie(weights, explode=explode, labels=market_category, autopct='%1.1f%%',
        startangle=90)
ax1.axis('equal') 
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2: st.pyplot(fig1)
    
with col3:
    st.write()
#market categories numericals    
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Choose one of the following market categories:</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
z = st.selectbox('There are 3 listing exchanges: G, S, Q.                                        NOTE: There are also 4666 stocks with an undefined market category; all of which we have excluded. After clicking on a market category, the corresponding number of stocks will be displayed.',[' ','G','S','Q'])
st.markdown('#')
st.markdown('#')
if z is ('G'):
        st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>There are 900 unique stocks in this market category.</h1>
    </div>
  """, unsafe_allow_html=True) 
if z is ('S'):
           st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>There are 952 unique stocks in this market category.</h1>
    </div>
  """, unsafe_allow_html=True)  
if z is ('Q'):
       st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>There are 1531 unique stocks in this market category.</h1>
    </div>
  """, unsafe_allow_html=True)  
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#ETFs
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 4) ETFs</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Please select one of the two options below:</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
y = st.radio('An ETF is a type of investment fund that is also an exchange-traded product. After clicking one of the buttons below, the corresponding number of ETFs will be displayed.',['ETF','Non-ETF'])
st.markdown('#')
st.markdown('#')
if y is ('ETF'):
  st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>ETFs are used by 2165 stock companies</h1>
    </div>
  """, unsafe_allow_html=True) 
if y is ('Non-ETF'):
  st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>ETFs are not used by 5884 stock companies</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
st.markdown('#')
st.markdown('#')
#distribution of ETfs
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>The Proportion of ETF and Non-ETF Stocks:</h1>
    </div>
  """, unsafe_allow_html=True) 
ETF_options= ['Yes','No']
ETF_distirbution=[2165, 5884]
explode = (0.05, 0.05)
fig, ax = plt.subplots()
ax.pie(ETF_distirbution, explode=explode, labels=ETF_options, autopct='%1.1f%%',
        startangle=90)
ax1.axis('equal') 
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2: st.pyplot(fig)
    
with col3:
    st.write()
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#round lot size
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 5) Round Lot Size</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Relationship Between Round Lot Size and the First 500 Stock Symbols</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2: 
    st.image('rls.png', width=1100)
with col3:
    st.write()
st.markdown('#')
st.markdown('#')
st.markdown('#')
#top 20 round lot size
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Top 20 Companies with the Largest Round Lot Size</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
w = st.slider("Pick a ranking between 1-20:",0,20)
st.write("Slider number:",w)
st.markdown('#')
st.markdown('#')
if w is (1): 
    st.markdown("""
    </style>           
    <div class="center-text">
        <h1 style='font-size:50px;'>Sempra Energy Common Stock (SRE) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True)
if w is (2): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>PGIM QMA Strategic Alpha Small-Cap Growth ETF (PQSG) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (3): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>iShares Exponential Technologies ETF (XT) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (4): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Huntington Bancshares Incorporated - Common Stock (HBAN) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (5): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>ProShares UltraShort Yen New (YCS) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True)
if w is (6): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>New Providence Acquisition Corp. - Unit	 (NPAUU) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (7): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Orgenesis Inc. - Common Stock (ORGS) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (8): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Hartford Core Bond ETF (HCRB) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (9): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Source Capital, Inc. Common Stock (SOR) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (10): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Halliburton Company Common Stock (HAL) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (11): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Invesco S&P 500 High Beta ETF (SPHB) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (12): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Virgin Galactic Holdings, Inc. Common Stock	(SPCE) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (13): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>NortonLifeLock Inc. - Common Stock (NLOK) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (14): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Pangaea Logistics Solutions Ltd. - Common Stock (PANL) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (15): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>L3Harris Technologies, Inc. Common Stock (LHX) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (16): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Agnico Eagle Mines Limited Common Stock (AEM) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (17): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>JPMorgan Research Enhanced High Yield ETF (JPHY) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (18): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>ETRACS Wells Fargo Business Development Company(BDCZ) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (19): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Grana y Montero S.A.A. American Depositary Shares (GRAM) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
if w is (20): 
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>Empresa Distribuidora Y Comercializadora Norte S.A. (EDN) has a Round Lot Size of 250</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#nasdaq stock market summary
st.markdown('#')
st.markdown("""
    <style>
    .center-text {
        text-align: center;
    }
    </style>
    <div class="center-text">
        <h1 style='font-size:85px;'>NASDAQ Stock Market Summary</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
#aligning image5
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2: 
    st.image('marketsumsss.png',caption='This is a screenshot of the first few of 5125 columns in this data file. This summary contains vital stock data for NASDAQ; starting from November 1999 and ending in April 2020. ', width=1000)
with col3:
    st.write()
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#opening price
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 1) Opening Price</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Select which summary statistic you would like to view:</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
#opening price summary statistics
d  = st.selectbox("You must select one of the following: Mean, Median or Mode. After selecting one, it will be displayed to you below.",[' ','Mean', 'Median', 'Mode'])
st.markdown('#')
st.markdown('#')
if d is ('Mean'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The mean opening price is: 33.736178947871586</h1>
    </div>
  """, unsafe_allow_html=True)
if d is ('Median'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The median opening price is: 27.120886804999998</h1>
    </div>
  """, unsafe_allow_html=True)
if d is ('Mode'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The modal opening price is: 22.889843</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
#opening stock price graph
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Opening Stock Price Over Time</h1>
    </div>
  """, unsafe_allow_html=True) 
df={"Date":['12/1999',' 6/2000','12/2000',' 6/2001',' 12/2001',' 6/2002',' 12/2002',' 6/2003',' 12/2003',' 6/2004',' 12/2004',' 6/2005',' 12/2005',' 6/2006',' 12/2006',' 6/2007',' 12/2007',' 6/2008',' 12/2008',' 6/2009',' 12/2009',' 6/2010',' 12/2010',' 6/2011',' 12/2011',' 6/2012',' 12/2012',' 6/2013',' 12/2013',' 6/2014',' 12/2014',' 6/2015',' 12/2015',' 6/2016',' 12/2016',' 6/2017',' 12/2017',' 6/2018',' 12/2018',' 6/2019',' 12/2019',' 4/2020'], "Moving Average ($)":[34.5806509, 65.34603871, 39.71698204, 30.57986791, 19.44431102, 22.36905698, 12.4654268, 11.05991754,17.03065188, 22.57433596, 17.18033481, 16.24772079, 21.76096162, 26.15402955, 23.13513954, 24.61457546, 26.76316021, 23.39993329, 20.58495726, 12.22042808, 18.17476541, 23.54565928, 23.38686134, 32.7620691, 27.8284132, 30.60106659, 27.56361308, 31.20088342, 35.49930418, 40.84792017, 41.01404288, 41.6082179, 38.77389278, 40.08705868, 46.21858099, 52.96872554, 64.55061224, 69.03194172, 66.77547998, 76.48485436, 75.34312922, 81.43435429]}
df=pd.DataFrame(df)
df=df.set_index("Date")
st.line_chart(
    df,
    y="Moving Average ($)")
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:15px;'>Date</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#highest price
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 2) Highest stock price</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Select which summary statistic you would like to view:</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
#highest stock price summary statistics
e = st.selectbox ("You must select one of the following: Mean, Median or Mode. After clicking on one, it will be displayed below:",[' ','Mean','Median','Mode'])
st.markdown('#')
st.markdown('#')
if e is ('Mean'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The mean highest price is: 34.560553403516</h1>
    </div>
  """, unsafe_allow_html=True)
if e is ('Median'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The median highest price is: 27.70386314</h1>
    </div>
  """, unsafe_allow_html=True)
if e is ('Mode'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The modal highest prices are: 25.035765 & 25.0 </h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
#highest stock price graph
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Highest Stock Price Over Time</h1>
    </div>
  """, unsafe_allow_html=True)
highprice={"Date":['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'], "Highest Stock Price ($)":[57.17990112, 40.37017059, 20.81545067, 13.01144505, 21.04434967, 17.33190346, 23.93419075, 25.52932739, 26.71673775, 11.32331944, 22.72532272, 29.82832527, 25.40057182, 29.30615234, 41.16595078, 41.79000092, 42.34999847, 45.81999969, 67.58000183, 67.48000336, 85.33999634, 70.23000336]}
highprice=pd.DataFrame(highprice)
highprice=highprice.set_index("Date")
st.line_chart(
    highprice,
    y="Highest Stock Price ($)")
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:15px;'>Date</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#lowest stock price
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 3) Lowest Stock Price</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
#lowest stock price summary statistics
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Select which summary statistic you would like to view:</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
f = st.selectbox("You must select one of the following options: Mean, Median, Mode. After clicking on it, the corresponding summary statistic will be dislpayed below.",[' ','Mean','Median','Mode'])
st.markdown('#')
st.markdown('#')
if f is ('Mean'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The mean lowest price is: 33.62946732919711</h1>
    </div>
  """, unsafe_allow_html=True)
if f is ('Median'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The median lowest price is: 27.010014535</h1>
    </div>
  """, unsafe_allow_html=True)
if f is ('Mode'):
        st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The modal lowest price is: 26.366238</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
#lowest stock price graph
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Lowest Stock Price Over Time</h1>
    </div>
  """, unsafe_allow_html=True)
lowprice={"Date":['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'], "Lowest Stock Price ($)":[54.542202, 38.35836792, 20.35050011, 12.72532177, 19.95708084, 17.18168831, 23.66952705, 24.87839699, 26.18741035, 10.67238903, 22.12446404, 29.49928474, 24.90700912, 28.35479164, 40.82975769, 40.90000153, 41.72000122, 45.38000107, 66.93000031, 66.33999634, 84.66999817, 68.15000153]}
lowprice=pd.DataFrame(lowprice)
lowprice=lowprice.set_index("Date")
st.line_chart(
    lowprice,
    y="Lowest Stock Price ($)")
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:15px;'>Date</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#closing stock price
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 4) Closing Stock Price</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
#closing stock price summary statistics
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Select which summary statistic you would like to view:</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
g = st.selectbox ("Select one of the following options: Mean, Median or Mode. After clicking on one of them, the corresponding summary statistic will be displayed below:",[' ','Mean','Median','Mode'])
st.markdown('#')
st.markdown('#')
if g is ('Mean'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The mean closing price is: 34.315202707735025</h1>
    </div>
  """, unsafe_allow_html=True)
if g is ('Median'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The median closing price is: 27.39628029</h1>
    </div>
  """, unsafe_allow_html=True)
if g is ('Mode'):
        st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The modal closing prices are: 17.167381, 22.889843 and 25.751074</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
#closing stock price graph
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Closing Stock Price Over Time</h1>
    </div>
  """, unsafe_allow_html=True)
closeprice={"Date":['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'], "Closing Stock Price ($)":[55.30221558, 39.16308975, 20.39341927, 12.84692383, 20.9155941, 17.23891258, 23.81258965, 24.9284687, 26.28040123, 11.1802578, 22.22460747, 29.63519287, 24.98569298, 29.28469276, 40.90843964, 40.93999863, 41.81000137, 45.56000137, 66.97000122, 67.45999908, 85.30999756, 68.91999817]}
closeprice=pd.DataFrame(closeprice)
closeprice=closeprice.set_index("Date")
st.line_chart(
    closeprice,
    y="Closing Stock Price ($)")
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:15px;'>Date</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#adjusted closing price
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 5) Adjusted Closing Stock Price</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Select which summary statistic you would like to view:</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
#adj. closing price summary statistics
h = st.selectbox ("Select one of the following options: Mean, Median or Mode. After clicking on one of the options, the corresponding summary statistics will be displayed below.",[' ','Mean','Median','Mode'])
st.markdown('#')
st.markdown('#')
if h is ('Mean'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The mean adjusted closing price is: 31.778674302347973</h1>
    </div>
  """, unsafe_allow_html=True)
if h is ('Median'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The median adjusting closing price is: 24.714865685</h1>
    </div>
  """, unsafe_allow_html=True)
if h is ('Mode'):
        st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The modal adjusting closing price is: 14.764728</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
#adj. closing price graph
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Adjusted Closing Price Over Time</h1>
    </div>
  """, unsafe_allow_html=True)
adjcloseprice={"Date":['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'], "Adjusted Closing Stock Price ($)":[47.56241608, 33.68203354, 17.53926468, 11.04893684, 17.98835754, 14.82624626, 20.47990036, 22.75439072, 23.98840714, 10.20519543, 20.28634071, 27.05062103, 22.80661392, 27.10531807, 38.41082382, 38.82008362, 40.16519928, 44.24706268, 65.62631989, 66.71923828, 85.09344482, 68.91999817]}
adjcloseprice=pd.DataFrame(adjcloseprice)
adjcloseprice=adjcloseprice.set_index("Date")
st.line_chart(
    adjcloseprice,
    y="Adjusted Closing Stock Price ($)")
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:15px;'>Date</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
#stock volume
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 6) Stock Volume</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Select which summary statistic you would like to view:</h1>
    </div>
  """, unsafe_allow_html=True) 
st.markdown('#')
#stock volume summary statistics
i = st.selectbox("Please select one of the following options: Mean, Median or Mode. After clicking on one of them, the corresponding summary statistics will be displayed below.",[' ','Mean', 'Median','Mode'])
st.markdown('#')
st.markdown('#')
if i is ('Mean'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The mean stock volume is: 3693249.9804839967</h1>
    </div>
  """, unsafe_allow_html=True)
if i is ('Median'):
    st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The median stock volume is: 3174050.0</h1>
    </div>
  """, unsafe_allow_html=True)
if i is ('Mode'):
        st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:50px;'>The modal stock volume is: 2223300.0</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
#stock volume graph
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Stock Volume Over Time</h1>
    </div>
  """, unsafe_allow_html=True)
volume={"Date":['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'], "Stock Volume":[1931100,  2069300,  2142000, 1627900, 3234200, 1650400, 3244600, 2443200, 2844700, 6415000, 5224600, 2050700, 1930900, 4707900, 1316000, 1421100, 1451000, 1216100, 1064900, 1572100, 1176200, 2173600]}
volume=pd.DataFrame(volume)
volume=volume.set_index("Date")
st.line_chart(
    volume,
    y="Stock Volume")
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:15px;'>Date</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.divider()
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Section 7) Advanced Analysis</h1>
        <h1 style='font-size:40px;'>Relationships between numerical columns</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Implied Volatility of Opening Stock Price</h1>
    </div>
  """, unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2: 
    st.image('3dgraph.png',caption='This is a 3d scatter graph displaying the implied volatility of the opening price between the years of 200 - 2020. ', width=1000)
with col3:
    st.write()
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Simplified Correlation Heat-Map Between Opening Stock Price and Stock Volume </h1>
    </div>
  """, unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.write()
with col2: 
    st.image('correlation.png',caption='This is a simplified correlation heat-map/matrix displaying the relationship between the Opening Stock Price and Stock Volume between the years of 2000-2020. ', width=1000)
with col3:
    st.write()
st.markdown('#')
st.markdown('#')
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>Daily Returns over Time </h1>
    </div>
  """, unsafe_allow_html=True)
dailyreturns={"Date":['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'], "Daily Returns":[1.0729599, 0.44706726, 0.13590812, -0.00715256, -0.4220314, -0.00715255, -0.00715256, 0.28612328, 0.40057182, -0.50786877, -0.02145958, 0, 0, -0.89413452, 0.18598175, 0.45000076, 0.09000016, 0.19999695, 0.52999878, -1.12000274, -0.47000122,  0.55000305]}
dailyreturns=pd.DataFrame(dailyreturns)
dailyreturns=dailyreturns.set_index("Date")
st.line_chart(
    dailyreturns,
    y="Daily Returns")
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:15px;'>Date </h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown('#')
st.divider()
st.markdown('#')
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:80px;'>Thank You!</h1>
        <h1 style='font-size:80px;'> </h1>
        <h1 style='font-size:40px;'>Congratulations for reaching the end of this web app. I hope you learnt something new about the NASDAQ Stock Market and it's data.</h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
st.markdown("""
    </style>
    <div class="center-text">
        <h1 style='font-size:30px;'>If you would like to contact me, please do so through the following email address: aaribhaider2008@gmail.com</h1>
        <h1 style='font-size:30px;'> </h1>
        <h1 style='font-size:30px;'>Alternatively, you can find my socials below: </h1>
    </div>
  """, unsafe_allow_html=True)
st.markdown('#')
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col1:
    st.link_button("Instagram", "https://www.instagram.com/aaribzaidi_/?next=%2F&hl=en")
with col2:
    st.write(' ')
with col3:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/aarib-zaidi-009101232/")
with col4:
    st.write (' ')
with col5:
    st.button("Phone number: 0302-133-1671")
