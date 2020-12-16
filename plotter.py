import plotly.graph_objects as go
from geopy.geocoders import Nominatim
import random
import crawler


def get_tweets_locations(to_search, count):
    tweets = crawler.get_tweets(to_search, count)
    geolocator = Nominatim(user_agent='TwitterPlotter')

    latitudes = list()
    longitudes = list()
    texts = list()

    none_found = 0
    for tweet in tweets:
        location = geolocator.geocode(tweet[0])
        already_located = False

        if location is not None:
            for i in range(len(latitudes)):
                if location.latitude == latitudes[i] and location.longitude == longitudes[i]:
                    already_located = True
                    latitudes.append(location.latitude + random.uniform(-0.005, 0.005))
                    longitudes.append(location.longitude + random.uniform(-0.005, 0.005))
                    texts.append(tweet[0] + ': ' + tweet[1])
                    break

            if not already_located:
                latitudes.append(location.latitude)
                longitudes.append(location.longitude)
                texts.append(tweet[0] + ': ' + tweet[1])
        else:
            none_found += 1

    return latitudes, longitudes, texts, none_found


def generate_html_map(to_search, count):
    mapbox_access_token = open('config/.mapbox_token').read()
    latitudes, longitudes, texts, none_found = get_tweets_locations(to_search, count)

    if none_found != 0:
        print('Could not locate', none_found, 'out of', count, 'locations')
    else:
        print('Successfully located all', count,'locations!')

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


if __name__ == '__main__':
    generate_html_map('#antivax', 30)