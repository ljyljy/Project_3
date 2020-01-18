// Sort the data array using the greekSearchResults value

var select = d3.select("#truncate_not")
select.append("option").text('total_data').property("value", 'total');
select.append("option").text('truncated_data').property("value", 'truncate');


d3.json('/total_error').then((data) => {
    var trace = [{
        x: data,
        type: 'histogram',
    }];
    var layout = {title: 'Histogram of logerror for total data'};
    Plotly.newPlot('target_normal', trace, layout);
});



function optionChanged(newSample) {
    // Fetch new data each time a new sample is selected
    if (newSample == 'total'){
        d3.json('/total_error').then((data) => {
            var trace = [{
                x: data,
                type: 'histogram',
            }]
            var layout = {title: 'Histogram of logerror for total data'};
            Plotly.newPlot('target_normal', trace, layout)
        });
    }
    else{
        d3.json('/truncated_error').then((data) => {
            var trace = [{
                x: data,
                type: 'histogram',
            }]
            var layout = {title: 'Histogram of logerror in absoluated 0.4'};
            Plotly.newPlot('target_normal', trace, layout)
        });
    }
}

d3.json('/time_series').then((data) => {
    var mean = {
        type: "scatter", mode: "lines", name: 'Mean of target', x: data['time'], 
        y: data['mean'], line: {color: '#FF5533'}
    }
    var median = {
        type: "scatter", mode: "lines", name: 'median of target', x: data['time'], 
        y: data['median'], line: {color: '#12FAF6'}
    }
    var seasonal = {
        type: "scatter", mode: "lines", name: 'seasonal', x: data['time'], 
        y: data['seasonal'], line: {color: '#33FFF6'}
    }
    var trend = {
        type: "scatter", mode: "lines", name: 'trend', x: data['time'], 
        y: data['trend'], line: {color: '#FF33FF'}
    }
    var residual = {
        type: "scatter", mode: "lines", name: 'residual', x: data['time'], 
        y: data['residual'], line: {color: '#FF5533'}
    }
    let small_list = [seasonal, trend, residual]
    let large_list = [median, mean]
    let layout1 = {title: 'Time series of target'};
    let layout2 = {title: 'Time series of seasonal, residuals and trend'}
    Plotly.newPlot('time_series', large_list, layout1);
    Plotly.newPlot('time_series_small', small_list, layout2);
})


d3.json('/geo_logerror').then((data) => {
    // var layout = {mapbox: { style: "open-street-map", center: { lat: 34.2, lon: -118.2 }, zoom: 7 },
    // margin: { r: 0, t: 0, b: 0, l: 0 }};
    var layout = {
        mapbox: {center: { lat: 34.2, lon: -118.4 }, zoom: 8, style: "open-street-map"},
        coloraxis: {colorscale: "Viridis"}, margin: { r: 0, t: 0, b: 0, l: 0 }};
    Plotly.newPlot('target_geo', data, layout)
})