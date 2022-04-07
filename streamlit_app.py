import streamlit as st

oil_price = st.slider('GAS PRICE', 1.0, 10.0, 0.1)
mpg = st.slider('MPG', 1, 100)
mph = st.slider('ESTIMATED MPH', 10, 100)
pick_and_drop_time = st.slider('PICK AND DROP TIME (min.)', 1, 60)
desired_hourly_earning = st.text_input('DESIRED HOURLY EARNING', value="")
desired_hourly_earning = int(desired_hourly_earning)

mil = st.slider('DELIVERY MILE',0.0,50.0,0.5)

price_max = mil/mpg*oil_price + mil/mph*desired_hourly_earning + pick_and_drop_time/60*desired_hourly_earning
price_min = mil/mpg*oil_price + mil/mph*desired_hourly_earning*2 + pick_and_drop_time/60*desired_hourly_earning
st.button('CALCULATE THE OFFER PRICES')
st.text('minimum price is ' + str(price_min))
