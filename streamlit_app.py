import streamlit as st


st.text('When you enter the required information below, a price range appears as a result. The maximum value in this price range is calculated by assuming that you come back to your current location after receiving and delivering the order, and the minimum value is that you receive a new order at the location where you delivered the order and contunie delivering.')


oil_price = float(st.text_input('GAS PRICE', value = '4.5'))

mpg = int(st.text_input('MPG', value = '25'))
mph = int(st.text_input('ESTIMATED MPH', value = '30'))
pick_and_drop_time = int(st.text_input('PICK AND DROP TIME (min.)', '10'))
desired_hourly_earning = int(st.text_input('DESIRED HOURLY EARNING', value="20"))
mil = int(st.slider('DELIVERY MILE',0.0,50.0,1.0))

price_min = mil/mpg*oil_price + mil/mph*desired_hourly_earning + pick_and_drop_time/60*desired_hourly_earning
price_max = mil*2/mpg*oil_price + mil*2/mph*desired_hourly_earning + pick_and_drop_time/60*desired_hourly_earning

st.text('price range is between ' + str(round(price_min,2)) + ' - ' + str(round(price_max,2)))
