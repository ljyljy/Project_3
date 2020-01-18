// Sort the data array using the greekSearchResults value

let sel_list = ['buildingqualitytypeid', 'regionidcity', 'regionidneighborhood', 'regionidzip', 'unitcnt', 'yearbuilt', 'lotsizesquarefeet']

let selector = d3.select('#geo_select')

function geo_map(sample, newSample){
    var layout_init = {title: {text: "Initial data of " + newSample}, dragmode: "zoom",
    mapbox: { style: "open-street-map", center: { lat: 34.2, lon: -118.2 }, zoom: 7 },
    margin: { r: 0, t: 0, b: 0, l: 0 }}
    var layout_final = {title: {text: "with KNN filling data of " + newSample}, dragmode: "zoom",
    mapbox: { style: "open-street-map", center: { lat: 34.2, lon: -118.2 }, zoom: 7 },
    margin: { r: 0, t: 0, b: 0, l: 0 }}
    Plotly.newPlot('init_geo', sample[0], layout_init)
    Plotly.newPlot('final_geo', sample[1], layout_final)
}



sel_list.forEach((data) => {
    selector.append("option").text(data).property("value", data);
})

d3.json('/geo_feature/buildingqualitytypeid').then((data) => {
    geo_map(data, "buildingqualitytypeid")
})



function geo_option(newSample) {
    if (newSample === 'lotsizesquarefeet') {
        d3.json('/lot_knn').then((sample) => {
            console.log(typeof sample[0]['z'][0])
            var layout = {
                mapbox: {center: { lat: 34.2, lon: -118.4 }, zoom: 8, style: "open-street-map"},
                coloraxis: {colorscale: "Viridis"}, margin: { r: 0, t: 0, b: 0, l: 0 }};
            var layout_init = {title: {text: "Initial data of " + newSample}, dragmode: "zoom",
            mapbox: { style: "open-street-map", center: { lat: 34.2, lon: -118.2 }, zoom: 7},
            margin: { r: 0, t: 0, b: 0, l: 0 }, coloraxis: {colorscale: "Viridis"}}
            var layout_final = {title: {text: "with KNN filling data of " + newSample}, dragmode: "zoom",
            mapbox: { style: "open-street-map", center: { lat: 34.2, lon: -118.2 }, zoom: 7},
            coloraxis: {colorscale: "Viridis"}, margin: { r: 0, t: 0, b: 0, l: 0 }}
            Plotly.newPlot('init_geo', sample[0], layout)
            Plotly.newPlot('final_geo', sample[1], layout)
        })
    }
    else {
        d3.json('/geo_feature/' + newSample).then((data) => {
            geo_map(data, newSample)
        })
    }
}




