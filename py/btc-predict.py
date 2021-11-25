from fbprophet import Prophet
import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", interval="minute60")

df = df.reset_index()
df['ds'] = df['index']
df['y'] = df['close']
data = df[['ds','y']]

model = Prophet()
model.fit(data)

future = model.make_future_dataframe(periods=24, freq='H')
forecast = model.predict(future)

fig = model.plot(forecast)