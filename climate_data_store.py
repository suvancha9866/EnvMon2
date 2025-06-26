import cdsapi

dataset = "reanalysis-era5-land-timeseries"
request = {
    "variable": [
        "2m_dewpoint_temperature",
        "2m_temperature",
        "surface_solar_radiation_downwards",
        "10m_u_component_of_wind",
        "10m_v_component_of_wind"
    ],
    "location": {"longitude": -87.75, "latitude": 41.75},
    "date": ["2023-06-01/2025-06-19"],
    "data_format": "netcdf"
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()
