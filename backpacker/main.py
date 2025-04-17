import json

import dash_leaflet as dl
import geopandas as gpd
from dash import Dash, Input, Output, callback, html

# layers = gpd.list_layers("backpacker/data/gadm41_VNM.gpkg")
gdf = gpd.read_file("backpacker/data/gadm41_VNM.gpkg", layer="ADM_ADM_1")
geojson_data = json.loads(gdf.to_json())


app = Dash()


def get_info(feature=None):
    header = [html.H4("Data:")]
    if not feature:
        return header + [html.P("Hover over a region")]

    return header + [
        f"{feature['properties']['NAME_1']}, {feature['properties']['COUNTRY']}",
    ]


info = html.Div(
    children=get_info(),
    id="info",
    className="info",
    style={"position": "absolute", "top": "10px", "right": "10px", "zIndex": "1000"},
)

geo_json = dl.GeoJSON(
    id="vnm-gadm",
    data=geojson_data,
    options=dict(style=dict(color="black", weight=1, fillOpacity=0.3)),
    hoverStyle=dict(weight=3, color="green", fillOpacity=0.5),
)

tile_layer = dl.TileLayer(
    url="https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png",
    attribution='&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>',  # noqa: E501
)

app.layout = html.Div(
    [
        dl.Map(
            center=[16, 107],
            zoom=5,
            style={"height": "90vh"},
            children=[tile_layer, geo_json, info],
        )
    ]
)


@callback(Output("info", "children"), Input("vnm-gadm", "hoverData"))
def info_hover(feature):
    return get_info(feature)


if __name__ == "__main__":
    app.run(debug=True)
