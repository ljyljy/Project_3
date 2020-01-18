// Sort the data array using the greekSearchResults value

// add features plot

function plotly_scattor(web, title, margins, id){
    d3.json(web).then((data) => {
        var layout = {title: {text: title}, margin: margins, xaxis: {
            autotick: false, ticks: 'outside', tickangle: 45, tickwidth: 4, size: 1}};
        Plotly.newPlot(id, data, layout);
    });
}

plotly_scattor('/add_feature', 'Add new features VS RMSE of lightGBM', {t:40,r:20,b:120,l:60}, 'feature_add')



// make function to add option
function add_option(list, opt){
    let temp_sel = d3.select(opt)
    list.forEach((data) => {
        temp_sel.append("option").text(data).property("value", data);
    })
}

// add new temperature features plot
// add select option in temp_sel
add_option(['2016_max_temp', '2016_min_temp', '2017_max_temp', '2017_min_temp', 'RMSE_test'], '#temp_sel')


// define a function to make a geo map for temp
function geo_plot(newSample){
    d3.json('/temp/' + newSample).then((data) =>{
        var layout = {title: {text: "Temperature data of " + newSample}, dragmode: "zoom",
        mapbox: { style: "open-street-map", center: { lat: 34.2, lon: -118.2 }, zoom: 7 },
        margin: { r: 0, t: 0, b: 0, l: 0 }}
        Plotly.newPlot('temp_plot', data, layout)
    })
}
geo_plot('2016_max_temp')

// function for temp_sel of selection
function temp_sel(newSample){
    if (newSample === 'RMSE_test'){
        plotly_scattor('/temp_feature', 'Add new features VS RMSE of lightGBM', {t:40,r:20,b:190,l:60}, 'temp_plot')
    }
    else{
        geo_plot(newSample)
    }
}

// add select option in feature importance 
add_option(["feature_importance", "importance_RMSE"], '#sel_feature')

plotly_scattor('/feature_importance', 'Feature importance of Light GBM', {t:40,r:100,b:150,l:40}, 'feature_imp')

function feature_importance(newSample){
    if (newSample === "feature_importance"){
        plotly_scattor('/feature_importance', 'Feature importance of Light GBM', {t:40,r:100,b:150,l:40}, 'feature_imp')
    }
    else{
        plotly_scattor('/importance_RMSE', 'Delete top 10 least important feature', {t:40,r:40,b:150,l:90}, 'feature_imp')
    }
}

add_option(['VIF_score', 'VIF_RMSE'], '#sel_vif')

plotly_scattor('/VIF_score', 'VIF of features (larger than 10)', {t:40,r:100,b:150,l:40}, 'vif_plot')

function vif_select(newSample){
    if (newSample === 'VIF_score'){
        plotly_scattor('/VIF_score', 'VIF of features (larger than 10)', {t:40,r:100,b:150,l:40}, 'vif_plot')
    }
    else{
        plotly_scattor('/VIF_RMSE', 'Delete features of VIF larger than 10', {t:40,r:100,b:150,l:70}, 'vif_plot')
    }
}


d3.json('/cor_logerror').then((data) =>{
    var layout = {title: {text: 'correlation between logerror and different features'}, margin: {t:40,r:100,b:150,l:40}, 
                barmode: 'relative', xaxis: {autotick: false, ticks: 'outside', tickangle: 45, tickwidth: 4, size: 1}};
    Plotly.newPlot('cor_plot', data, layout)
})

add_option(['Corr_for_logerror', 'Corr_between_features', 'Correlation_RMSE'], '#sel_cor')


function getPointCategoryName(point, dimension) {
    var series = point.series,
        isY = dimension === 'y',
        axis = series[isY ? 'yAxis' : 'xAxis'];
    return axis.categories[point[isY ? 'y' : 'x']];
}

function heatmap(data){
    Highcharts.chart('cor_plot', {
        chart: {
            type: 'heatmap', marginTop: 40, marginBottom: 80, plotBorderWidth: 1},
            title: {text: 'Heatmap of features which have high correlations with logerror'},
            xAxis: {categories: data['x'], labels: {style: {fontSize: '7px'}}}, yAxis: {categories: data['x'], title: null}, 
            accessibility: {point: {descriptionFormatter: function (point) {
                        var ix = point.index + 1,
                            xName = getPointCategoryName(point, 'x'),
                            yName = getPointCategoryName(point, 'y'),
                            val = point.value;
                        return ix + '. ' + xName + ' sales ' + yName + ', ' + val + '.';
                    }
                }
        },
        colorAxis: {min: -1, stops: [[0, '#3060cf'], [0.5, '#ffffff'], [0.9, '#c4463a']]},   
        legend: {align: 'right', layout: 'vertical', margin: 0, verticalAlign: 'top', y: 25,symbolHeight: 280},    
        tooltip: {
            formatter: function () {
                return 'the correlation between ' + getPointCategoryName(this.point, 'x') + ' and ' + 
                getPointCategoryName(this.point, 'y') + ' are ' +  this.point.value;
            }
        },
        series: [{name: 'Correlation', borderWidth: 1, data: data['z']}],
        responsive: {rules: [{condition: {maxWidth: 500}, chartOptions: {yAxis: {labels: {formatter: function () {return this.value.charAt(0);}}}}}]}   
    });
}

function correlation(newSample){
    if (newSample === 'Corr_for_logerror'){
        document.getElementById("cor_plot").innerHTML = "";
        d3.json('/cor_logerror').then((data) =>{
            var layout = {title: {text: 'correlation between logerror and different features'}, margin: {t:40,r:100,b:150,l:40}, 
                        barmode: 'relative', xaxis: {autotick: false, ticks: 'outside', tickangle: 45, tickwidth: 4, size: 1}};
            Plotly.newPlot('cor_plot', data, layout)
        })
    }
    else if (newSample === 'Corr_between_features'){
        d3.select("#cor_plot").select("svg").remove();
        d3.json('/cor_key').then((data) =>{
            heatmap(data)
        })
    }
    else {
        document.getElementById("cor_plot").innerHTML = "";
        plotly_scattor('/cor_RMSE', 'Delete features which has high correlations', {t:40,r:100,b:150,l:70}, 'cor_plot')
    }
}

add_option(['3D viewing', '2D viewing'], '#outlier_sel')


d3.json('/2d_outlier').then((data) =>{
    var layout = {title: {text: 'Total number of size VS rmse'}, margin: {t:40,r:40,b:40,l:40}, 
                barmode: 'relative', xaxis: {showgrid: false, showticklabels: false}};
    Plotly.newPlot('outlier_plot', data, layout)
})
// plotly_scattor('/2d_outlier', 'min and max determination of outlier', {t:40,r:100,b:150,l:40}, 'outlier_plot')