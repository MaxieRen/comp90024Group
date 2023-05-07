<template>
    <div>
        <h2>All Regions (ABS SA4)</h2>
        <div id="overview-chart1-container">
            <figure class="highcharts-figure">
                <highcharts :options="chartOptions"></highcharts>
                <p class="highcharts-description">
                    Chart showing how different series types can be combined in a single
                    chart. The chart is using a set of column series, overlaid by a line and
                    a pie series. The line is illustrating the column averages, while the
                    pie is illustrating the column totals.
                </p>
            </figure>
        </div>

        <ul>
            <li v-for="(item, index) in data" :key="index">{{ item }}</li> <!-- dynamically updated -->
        </ul>
        <div class="container-fluid">
            <button @click="getData1">获取数据</button>
            <button @click="getData2" >update</button>
            <button @click="getData3" >获取数据</button>
        </div>
        <div class = "container-fluid">
            <figure class="highcharts-figure">
                <div id="chart-container" style="width:100%; height:400px;"></div>
                <p class="highcharts-description">
                    Bar chart showing horizontal columns. This chart type is often
                    beneficial for smaller screens, as the user can scroll through the data
                    vertically, and axis labels are easy to read.
                </p>
            </figure>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import {Chart} from 'highcharts-vue';
import Highcharts from "highcharts";

export default {
    name: 'RegionView',

    props: {
        msg: String
    },
    data() {
        return {
            chart:null,
            data: [56,41,53,37,43],
            chartOptions :{
                title: {
                    text: 'Employment Rate',
                    x: -20 //center
                },
                subtitle: {
                    text: 'Source: WorldClimate.com',
                    x: -20
                },
                xAxis: {
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
                    ]
                },
                yAxis: {
                    title: {
                        text: 'Temperature (°C)'
                    },
                    plotLines: [{
                        value: 0,
                        width: 1,
                        color: '#808080'
                    }]
                },
                tooltip: {
                    valueSuffix: '°C'
                },
                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'middle',
                    borderWidth: 0
                },
                series: [{
                    name: 'Male',
                    data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
                }, {
                    name: 'Female',
                    data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
                }, {
                    name: 'youth',
                    data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
                }, {
                    name: 'adult',
                    data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
                }]
            },
        };
    },
    methods: {
        async getData1() { // get data 1 method calls api GET that backends implemented
            try {
                this.data = [56,41,53,36,43];
            } catch (error) {
                console.log(error);
            }
        },
        async getData2() {
            try {
                // const response = await axios.post('http://127.0.0.1:8081/api_1');
                // console.log(response.data);
                // this.data = response.data;
                this.chartOptions = {
                    title: {
                        text: 'Unmployment Rate',
                        x: -20 //center
                    },
                    subtitle: {
                        text: 'Source: WorldClimate.com',
                        x: -20
                    },
                    xAxis: {
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
                        ]
                    },
                    yAxis: {
                        title: {
                            text: 'Temperature (°C)'
                        },
                        plotLines: [{
                            value: 0,
                            width: 1,
                            color: '#808080'
                        }]
                    },
                    tooltip: {
                        valueSuffix: '°C'
                    },
                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        verticalAlign: 'middle',
                        borderWidth: 0
                    },
                    series: [{
                        name: 'Male',
                        data: [4.4,5,20.4,18.5,13,7.2,9,14,11,8,6,3.4]
                    }, {
                        name: 'Female',
                        data: [-11,4.5,-9,8.3,19.4,6.7,2.1,4.8,10,14.5,12,20.2]
                    }, {
                        name: 'youth',
                        data: [5,5,11,9,14,14,0,3,7,10,6,4]
                    }, {
                        name: 'adult',
                        data: [3,0,5,13,17,9,2,19,14,4,1,16]
                    }]
                };
            } catch (error) { 
                console.log(error);
            }
        },
        async getData3() {
            try {
                this.data = [1,2,3,4,5,6,7,8];
            } catch (error) {
                console.log(error);
            }
        }
    },
    mounted() {
        const chart = Highcharts.chart('chart-container', {
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Unemployment by Age',
                align: 'left'
            },
            subtitle: {
                text: 'Source: <a ' +
                    'href="https://en.wikipedia.org/wiki/List_of_continents_and_continental_subregions_by_population"' +
                    'target="_blank">Wikipedia.org</a>',
                align: 'left'
            },
            xAxis: {
                categories: ['15-25', '25-30', '30-40', '40-50', '50-60'],
                title: {
                    text: null
                },
                gridLineWidth: 1,
                lineWidth: 0
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Population (millions)',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                },
                gridLineWidth: 0
            },
            tooltip: {
                valueSuffix: ' millions'
            },
            plotOptions: {
                bar: {
                    borderRadius: '50%',
                    dataLabels: {
                        enabled: true
                    },
                    groupPadding: 0.1
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                x: -40,
                y: 80,
                floating: true,
                borderWidth: 1,
                backgroundColor:
                    Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
                shadow: true
            },
            credits: {
                enabled: false
            },
            series: [{
                name: 'Year 1990',
                data: [631, 727, 3202, 721, 26]
            }, {
                name: 'Year 2000',
                data: [814, 841, 3714, 726, 31]
            }, {
                name: 'Year 2010',
                data: [1044, 944, 4170, 735, 40]
            }, {
                name: 'Year 2020',
                data: [1276, 1007, 4561, 746, 42]
            }]
        });

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}
ul {
    list-style-type: none;
    padding: 0;
}
li {
    display: inline-block;
    margin: 0 10px;
}

button{
    background-color: #fff;
    border: 1px solid #d5d9d9;
    border-radius: 8px;
    box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;
    box-sizing: border-box;
    color: #0f1111;
    cursor: pointer;
    display: inline-block;
    font-family: "Amazon Ember",sans-serif;
    font-size: 13px;
    line-height: 29px;
    padding: 0 10px 0 11px;
    position: relative;
    text-align: center;
    text-decoration: none;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
    vertical-align: middle;
    width: 100px;
    margin: 14px;
}
button:hover {
    background-color: #f7fafa;
}
button:focus {
    border-color: #008296;
    box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;
    outline: 0;
}
</style>
