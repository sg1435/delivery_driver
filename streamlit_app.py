import streamlit as st




oil_price = st.text_input('GAS PRICE', value = '4.17')
oil_price = int(oil_price)
mpg = st.text_input('MPG', value = '25')
mpg = int(mpg)
mph = int(st.text_input('ESTIMATED MPH', value = '30'))
pick_and_drop_time = int(st.text_input('PICK AND DROP TIME (min.)', '10'))
desired_hourly_earning = int(st.text_input('DESIRED HOURLY EARNING', value="20"))
mil = st.slider('DELIVERY MILE',0.0,50.0,1.0)

price_min = mil/mpg*oil_price + mil/mph*desired_hourly_earning + pick_and_drop_time/60*desired_hourly_earning
price_max = mil*2/mpg*oil_price + mil*2/mph*desired_hourly_earning + pick_and_drop_time/60*desired_hourly_earning

if st.button('CALCULATE THE OFFER PRICES'):  
  st.text('price range is between ' + str(round(price_min,2)) + ' - ' + str(round(price_max,2)))
