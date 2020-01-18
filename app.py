# import all the libraries
from flask import Flask, render_template, redirect, jsonify
import pandas as pd
import json

# Create an instance of Flask
app = Flask(__name__)

colors =  ["#63b598", "#ce7d78", "#ea9e70", "#a48a9e", "#c6e1e8", "#648177" ,"#0d5ac1" ,
        "#f205e6" ,"#1c0365" ,"#14a9ad" ,"#4ca2f9" ,"#a4e43f" ,"#d298e2" ,"#6119d0",
        "#d2737d" ,"#c0a43c" ,"#f2510e" ,"#651be6" ,"#79806e" ,"#61da5e" ,"#cd2f00" ,
        "#9348af" ,"#01ac53" ,"#c5a4fb" ,"#996635","#b11573" ,"#4bb473" ,"#75d89e" ,
        "#2f3f94" ,"#2f7b99" ,"#da967d" ,"#34891f" ,"#b0d87b" ,"#ca4751" ,"#7e50a8" ,
        "#c4d647" ,"#e0eeb8" ,"#11dec1" ,"#289812" ,"#566ca0" ,"#ffdbe1" ,"#2f1179" ,
        "#935b6d" ,"#916988" ,"#513d98" ,"#aead3a", "#9e6d71", "#4b5bdc", "#0cd36d",
        "#250662", "#cb5bea", "#228916", "#ac3e1b", "#df514a", "#539397", "#880977",
        "#f697c1", "#ba96ce", "#679c9d", "#c6c42c", "#5d2c52", "#48b41b", "#e1cf3b",
        "#5be4f0", "#57c4d8", "#a4d17a", "#225b8", "#be608b", "#96b00c", "#088baf",
        "#f158bf", "#e145ba", "#ee91e3", "#05d371", "#5426e0", "#4834d0", "#802234",
        "#6749e8", "#0971f0", "#8fb413", "#b2b4f0", "#c3c89d", "#c9a941", "#41d158",
        "#fb21a3", "#51aed9", "#5bb32d", "#807fb", "#21538e", "#89d534", "#d36647",
        "#7fb411", "#0023b8", "#3b8c2a", "#986b53", "#f50422", "#983f7a", "#ea24a3",
        "#79352c", "#521250", "#c79ed2", "#d6dd92", "#e33e52", "#b2be57", "#fa06ec",
        "#1bb699", "#6b2e5f", "#64820f", "#1c271", "#21538e", "#89d534", "#d36647",
        "#7fb411", "#0023b8", "#3b8c2a", "#986b53", "#f50422", "#983f7a", "#ea24a3",
        "#79352c", "#521250", "#c79ed2", "#d6dd92", "#e33e52", "#b2be57", "#fa06ec",
        "#1bb699", "#6b2e5f", "#64820f", "#1c271", "#9cb64a", "#996c48", "#9ab9b7",
        "#06e052", "#e3a481", "#0eb621", "#fc458e", "#b2db15", "#aa226d", "#792ed8",
        "#73872a", "#520d3a", "#cefcb8", "#a5b3d9", "#7d1d85", "#c4fd57", "#f1ae16",
        "#8fe22a", "#ef6e3c", "#243eeb", "#1dc18", "#dd93fd", "#3f8473", "#e7dbce",
        "#421f79", "#7a3d93", "#635f6d", "#93f2d7", "#9b5c2a", "#15b9ee", "#0f5997",
        "#409188", "#911e20", "#1350ce", "#10e5b1", "#fff4d7", "#cb2582", "#ce00be",
        "#32d5d6", "#17232", "#608572", "#c79bc2", "#00f87c", "#77772a", "#6995ba",
        "#fc6b57", "#f07815", "#8fd883", "#060e27", "#96e591", "#21d52e", "#d00043",
        "#b47162", "#1ec227", "#4f0f6f", "#1d1d58", "#947002", "#bde052", "#e08c56",
        "#28fcfd", "#bb09b", "#36486a", "#d02e29", "#1ae6db", "#3e464c", "#a84a8f",
        "#911e7e", "#3f16d9", "#0f525f", "#ac7c0a", "#b4c086", "#c9d730", "#30cc49",
        "#3d6751", "#fb4c03", "#640fc1", "#62c03e", "#d3493a", "#88aa0b", "#406df9",
        "#615af0", "#4be47", "#2a3434", "#4a543f", "#79bca0", "#a8b8d4", "#00efd4",
        "#7ad236", "#7260d8", "#1deaa7", "#06f43a", "#823c59", "#e3d94c", "#dc1c06",
        "#f53b2a", "#b46238", "#2dfff6", "#a82b89", "#1a8011", "#436a9f", "#1a806a",
        "#4cf09d", "#c188a2", "#67eb4b", "#b308d3", "#fc7e41", "#af3101", "#ff065",
        "#71b1f4", "#a2f8a5", "#e23dd0", "#d3486d", "#00f7f9", "#474893", "#3cec35",
        "#1c65cb", "#5d1d0c", "#2d7d2a", "#ff3420", "#5cdd87", "#a259a4", "#e4ac44",
        "#1bede6", "#8798a4", "#d7790f", "#b2c24f", "#de73c2", "#d70a9c", "#25b67",
        "#88e9b8", "#c2b0e2", "#86e98f", "#ae90e2", "#1a806b", "#436a9e", "#0ec0ff",
        "#f812b3", "#b17fc9", "#8d6c2f", "#d3277a", "#2ca1ae", "#9685eb", "#8a96c6",
        "#dba2e6", "#76fc1b", "#608fa4", "#20f6ba", "#07d7f6", "#dce77a", "#77ecca"]

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    return render_template("index.html")

# return total logerror
@app.route('/total_error')
def total_error():
    df_train = pd.read_csv('./static/data/clean_final.csv')
    logerror = df_train['logerror'].to_list()
    return jsonify(logerror)

# return truncated [-0.4, 0.4] of logerror
@app.route('/truncated_error')
def truncated_error():
    df_train = pd.read_csv('./static/data/clean_final.csv')
    logerror = df_train['logerror'].to_list()
    logerror = [x for x in logerror if x <=0.4 and x >= -0.4]
    return jsonify(logerror)

# return the time series of data with mean, median, seasonal, trend and residual 
@app.route('/time_series')
def time_series():
    df_train = pd.read_csv('./static/data/time_series.csv')
    df_train = df_train.fillna(0)
    df_train['residual'] = df_train['residual'] / 3
    time_series = {'mean': df_train['mean'].to_list(),
                   'median': df_train['median'].to_list(),
                   'seasonal': df_train['seasonal'].to_list(),
                   'trend': df_train['trend'].to_list(),
                   'residual': df_train['residual'].to_list(),
                    'time': df_train['transactiondate'].to_list(),
                    }
    return jsonify(time_series)

# return missing value precentages which are more than 0.1
@app.route('/missing_value')
def missing_value():
    df_missing = pd.read_csv('./static/data/missing_value.csv')
    df_missing = df_missing.loc[df_missing['missing_prec'] > 0.1,:]
    missing = json.loads(df_missing.to_json(orient='values'))
    return jsonify(missing)

# return KNN results with certain color for same values.
# have the input of geo features and return init and final json
@app.route('/geo_feature/<sample>')
def geo_feature(sample):
    # setup the color list
    
    df_init = pd.read_csv('./static/data/clean_init.csv')
    df_final = pd.read_csv('./static/data/clean_final.csv')
    col_list = [sample, 'latitude', 'longitude']
    df_temp_init = df_init[col_list].dropna()
    df_temp_final = df_final[col_list].dropna()
    unique_list = list(df_temp_final[sample].unique())
    final_list = []
    init_list = []
    color = 0
    for i in unique_list:
        color %= len(colors)
        temp_dict = {'type': "scattermapbox", 'showlegend': False, 'marker': { 'color': colors[color], 'size': 4 }}
        init = df_temp_init.loc[df_temp_init[sample] == i,:]
        init = init.head(int(init.shape[0] / 20))
        final = df_temp_final.loc[df_temp_final[sample] == i,:]
        final = final.head(int(final.shape[0] / 20))
        temp_dict['lon'] = init['longitude'].to_list()
        temp_dict['lat'] = init['latitude'].to_list()
        init_list.append(temp_dict)
        
        temp_dict['lon'] = final['longitude'].to_list()
        temp_dict['lat'] = final['latitude'].to_list()
        final_list.append(temp_dict)
        color += 1
    return jsonify([init_list, final_list])


# return lotsizesquarefeet knn filling
@app.route('/lot_knn')
def lot_knn():
    df_init = pd.read_csv('./static/data/clean_init.csv')
    df_final = pd.read_csv('./static/data/clean_final.csv')
    df_init = df_init[['lotsizesquarefeet', 'latitude', 'longitude']].dropna().sample(frac = 0.05, random_state=1)
    df_final = df_final[['lotsizesquarefeet', 'latitude', 'longitude']].dropna().sample(frac = 0.05, random_state=1)
    print(df_final.lotsizesquarefeet.dtype)
    result = [{'lon': df_init.longitude.to_list(), 'lat': df_init.latitude.to_list(), 'z': df_init.lotsizesquarefeet.to_list(), 
                'type': 'densitymapbox', 'radius': 1, 'coloraxis': 'coloraxis', 'hoverinfo': 'skip'}, 
              {'lon': df_final.longitude.to_list(), 'lat': df_final.latitude.to_list(), 'z': df_final.lotsizesquarefeet.to_list(), 
                'type': 'densitymapbox', 'radius': 1, 'coloraxis': 'coloraxis', 'hoverinfo': 'skip'}]
    return jsonify([result])
        

@app.route('/geo_logerror')
def geo_logerror():
    df = pd.read_csv('./static/data/clean_final.csv')
    df = df[['logerror', 'latitude', 'longitude']].dropna()
    df = df.loc[df.logerror <= 0.4,:]
    df = df.loc[df.logerror >= -0.419,:]
    return jsonify([{'lon': df.longitude.to_list(), 'lat': df.latitude.to_list(), 'z': df.logerror.to_list(), 
                    'type': 'densitymapbox', 'radius': 1, 'coloraxis': 'coloraxis', 'hoverinfo': 'skip'}])

@app.route("/add_feature")
def add_feature():
    df = pd.read_csv('./static/data/add_feature.csv')
    result = {'type': 'scatter', 'x': df.add_feature.to_list(), 'y': df.rmse.to_list(), 'mode': 'markers', 
    'name': 'Add new figures', 'marker': {'color': 'rgba(156, 165, 196, 0.95)', 'symbol': 'circle', 'size': 16}}
    return jsonify([result])

@app.route("/temp_feature")
def temp_feature():
    df = pd.read_csv('./static/data/tempeature_features.csv')
    result = {'type': 'scatter', 'x': df.temp_feature.to_list(), 'y': df.rmse.to_list(), 'mode': 'markers', 
    'name': 'Add new figures', 'marker': {'color': 'rgba(156, 165, 196, 0.95)', 'symbol': 'circle', 'size': 16}}
    return jsonify([result])

@app.route("/temp/<sample>")
def temp(sample):
    score = 40
    split_list = sample.split('_')
    if split_list[0] == '2016':
        df = pd.read_csv('./static/data/weather_final_2016.csv')
    else:
        df = pd.read_csv('./static/data/weather_final_2017.csv')
    if split_list[1] == 'max':
        col_list = ['max_temp', 'total_high_hours', 'latitude', 'longitude']
    else:
        col_list = ['min_temp', 'total_low_hours', 'latitude', 'longitude']
    df[col_list[1]] = df[col_list[1]] / df[col_list[1]].max() * score
    data = [{'type': 'scattermapbox', 'mode': 'markers', 'lat': df[col_list[2]].to_list(),
    'lon': df[col_list[3]].to_list(), 'marker': {'size': df[col_list[1]].to_list(),'color': df[col_list[0]].to_list(), 
    'colorscale': 'RdBu'}}]
    return jsonify(data)


@app.route("/feature_importance")
def feature_imp():
    df_imp = pd.read_csv('./static/data/init_feature_importance.csv')
    df_mean = df_imp.groupby('feature').mean().reset_index().sort_values('importance', ascending = False)
    df_max = df_imp.groupby('feature').max().reset_index().rename(columns = {'importance': 'max'})
    df_min = df_imp.groupby('feature').min().reset_index().rename(columns = {'importance': 'min'})
    df = df_mean.merge(df_max, on = 'feature', how = 'left')
    df = df.merge(df_min, on = 'feature', how = 'left')
    result = {'x': df.feature.to_list(),'y': df.importance.to_list(), 'type': 'bar'}
    max_list = []
    min_list = []
    for i in df.index:
        max_list.append(df['max'][i] - df['importance'][i])
        min_list.append(df['importance'][i] - df['min'][i])
    result['error_y'] = {'type': 'data', 'symmetric': False, 'array': max_list, 'arrayminus': min_list}
    result['marker'] = {'color': colors[:len(max_list)]}
    return jsonify([result])

@app.route("/importance_RMSE")
def importance_rmse():
    df = pd.read_csv('./static/data/del_feature.csv')
    result = {'type': 'scatter', 'x': df.imp_feature.to_list(), 'y': df.rmse.to_list(), 'mode': 'markers', 
    'name': 'Add new figures', 'marker': {'color': 'rgba(156, 165, 196, 0.95)', 'symbol': 'circle', 'size': 16}}
    return jsonify([result])


@app.route("/VIF_score")
def vif_plot():
    df = pd.read_csv('./static/data/vif.csv')
    df = df.loc[df.vifScore >= 10,:]
    result = {'type': 'bar', 'x': df.variables.to_list(), 'y': df.vifScore.to_list(), 'mode': 'markers', 
    'name': 'Add new figures', 'marker': {'color': 'rgba(156, 165, 196, 0.95)'}}
    return jsonify([result])

@app.route("/VIF_RMSE")
def vif_rmse():
    df = pd.read_csv('./static/data/vif_delete.csv')

    result = {'type': 'scatter', 'x': df.vif_feature.to_list(), 'y': df.rmse.to_list(), 'mode': 'markers', 
    'name': 'Add new figures', 'marker': {'color': 'rgba(156, 165, 196, 0.95)', 'symbol': 'circle', 'size': 16}}
    return jsonify([result])

@app.route("/cor_logerror")
def cor_logerror():
    df = pd.read_csv('./static/data/corr_logerror.csv').sort_values('corr_values', ascending = False)
    result = {'type': 'bar', 'x': df.col_labels.to_list(), 'y': df.corr_values.to_list()}
    return jsonify([result])


@app.route("/cor_key")
def cor_key():
    df = pd.read_csv('./static/data/corr_key.csv')
    column = list(df.columns)
    total_list = []
    for i in df.index:
        for j in df.index:
            total_list.append([i, j, df.iloc[i,j]])
    return jsonify({'x': column, 'z': total_list})

@app.route("/cor_RMSE")
def cor_rmse():
    df = pd.read_csv('./static/data/cor_delete_rmse.csv')

    result = {'type': 'scatter', 'x': df.cor_feature.to_list(), 'y': df.rmse.to_list(), 'mode': 'markers', 
    'name': 'Add new figures', 'marker': {'color': 'rgba(156, 165, 196, 0.95)', 'symbol': 'circle', 'size': 8}}
    return jsonify([result])


@app.route("/2d_outlier")
def outlier_2d():
    df = pd.read_csv("./static/data/outlier_strategy.csv")
    result = {'type': 'scatter', 'x': df['shape'].to_list(), 'y': df['rmse'].to_list(), 'mode': 'markers', 
    'name': 'Add new figures', 'marker': {'color': 'rgba(156, 165, 196, 0.95)', 'symbol': 'circle', 'size': 4}}
    return jsonify([result])



if __name__ == "__main__":
    app.run(debug=True)


