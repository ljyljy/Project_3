// @TODO: YOUR CODE HERE!
d3.json('/missing_value').then((data) => {
  Highcharts.chart('missing', {
    chart: {
      type: 'column'
    },
    title: {
      text: 'The percentage of missing value'
    },
    xAxis: {
      type: 'category',
      labels: {
        rotation: -45,
        style: {
          fontSize: '13px',
          fontFamily: 'Verdana, sans-serif'
        }
      }
    },
    yAxis: {
      min: 0,
      title: {
        text: 'Missing value percentage'
      }
    },
    legend: {
      enabled: false
    },
    tooltip: {
      formatter: function(){
        if (this.x === 2){
          return 'basementsqft: Replacing with 0';
        }
        else if (this.x === 12){
          return 'pooltypeid2: Replacing with 0 (as no pools)';
        }
        else if (this.x === 13){
          return 'hashottuborspa: Replacing with False';
        }
        else if (this.x === 15){
          return 'taxdelinquencyflag: Replacing with 0.';
        }
        else if (this.x === 18){
          return 'calculatedfinishedsqarefeet and finishedsquarefeet50 are same in the description. Drop!';
        }
        else if (this.x === 19){
          return 'calculatedfinishedsqarefeet and finishedsquarefeet50 are same in the description. Keep!';
        }
        else if (this.x === 20){
          return 'fireplacecnt: Replacing with 0';
        }
        else if (this.x === 21){
          return 'threequarterbathnbr: Replacing with 0';
        }
        else if (this.x === 23){
          return 'poolcnt: Replacing with 0';
        }
        else if (this.x === 26){
          return 'garagetotalsqft: Replacing with 0';
        }
        else if (this.x === 27){
          return 'garagecarcnt: Replacing with 0';
        }
        else if (this.x === 28){
          return 'regionidneighborhood: Geo features fill with KNN';
        }
        else if (this.x === 30){
          return 'buildingqualitytypeid: Geo features fill with KNN';
        }
        else if (this.x === 31){
          return 'propertyzoningdesc: unknown description, drop!';
        }
        else if (this.x === 32){
          return 'unitcnt: Geo features fill with KNN';
        }
        else if (this.x === 33){
          return 'lotsizesquarefeet: Geo features fill with KNN';
        }
        else if (this.x > 23){
          return 'keep them because the missing value percentage is less than 95%'
        }
        else{
          return 'Drop!';
        }
      }
    },
    series: [{
      name: 'Population',
      data: data,
      turboThreshold: 0,
      dataLabels: {
        enabled: true,
        rotation: -90,
        color: '#FFFFFF',
        align: 'right',
        format: '{point.y:.2f}', // one decimal
        y: 10, // 10 pixels down from the top
        style: {
          fontSize: '13px',
          fontFamily: 'Verdana, sans-serif'
        }
      }
    }]
  });
})

