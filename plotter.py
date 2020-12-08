import plotly.graph_objects as go
from geopy.geocoders import Nominatim
import crawler

mapbox_access_token = open("config/.mapbox_token").read()
geolocator = Nominatim(user_agent='TwitterPlotter')
tweets = crawler.get_tweets('#virus', 30)

latitudes = list()
longitudes = list()
texts = list()

# for tweet in tweets:
#     print(tweet[0])

for tweet in tweets:
    location = geolocator.geocode(tweet[0])
    latitudes.append(location.latitude)
    longitudes.append(location.longitude)
    texts.append(tweet[0] + ': ' + tweet[1])

fig = go.Figure(go.Scattermapbox(
        lat=latitudes,
        lon=longitudes,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=9
        ),
        text=texts,
    ))

fig.update_layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=51.507351,
            lon=-0.127758
        ),
        pitch=0,
        zoom=2
    ),
)

fig.write_html('figure.html', auto_open=True)