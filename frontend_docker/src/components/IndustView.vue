<template>
    <div>
        <h1>Industries</h1>
        <div id="chart-1" class="container">
            <highcharts :options="chartOptions"></highcharts>
        </div>
        <button @click="getData1" >get test data</button>
        <button @click="updateChart" >更新图表</button>
        <button @click="getData2">修改数据</button>
        <ul>{{string}}</ul>


        <div class="container-lg py-4">
            <div class="row">
                <div class="col">
                    <figure class="highcharts-figure">
                        <div id="pie_container"></div>
<!--                        <p class="highcharts-description">-->
<!--                            This pie chart shows how the chart legend can be used to provide-->
<!--                            information about the individual slices.-->
<!--                        </p>-->
                    </figure>
                </div>
                <div class="col">
                    <figure class="highcharts-figure">

                        <p class="card-title">
                            <ul>
                                <li>Stay up-to-date with conditions in your local labour market</li>
                                <li>Identify jobs and skills in-demand</li>
                                <li>Understand employer needs and recruitment trends</li>
                                <li>Explore the trends impacting the jobs market now and into the future.</li>
                            </ul>
                        </p>
                    </figure>
                </div>
            </div>
        </div>
        <div class="container">

        </div>
    </div>
</template>

<script>
import axios from 'axios';
import {Chart} from "highcharts-vue";
import Highcharts from "highcharts";

export default {
    name: 'IndustView',
    props: {
        msg: String,
    },
    data() {
        return {
            chartData : null,
            string: 'nothing',
            chartOptions: {
                series: [{
                    data: [5, 20, 36, 10, 10, 20,5, 20, 36, 10, 10, 20,5, 20, 36, 10, 10, 20,5, 20, 36, 10, 10, 20]// sample data
                }]
            }
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://45.113.235.46:8081/api_0/Braidwood');
                this.chartData = response.data;
                console.log(this.chartData);
                this.chartOptions = {
                    xAxis:{
                        categories: this.chartData.Date
                    },
                    series: [{
                        name: 'rate',
                        data: this.chartData.UnempRate
                    }]
                }
            } catch (error) {
                console.log(error);
            }
        },

        async getData2() {
            try {
                this.string = this.string + 'sth '
            } catch (error) {
                console.log(error);
            }
        },
        updateChart() {
            this.chartOptions ={
                title: {
                    text: 'Unemployment rate',
                        x: -20 //center
                },
                subtitle: {
                    text: 'Source: ABS',
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
                    name: 'Tokyo',
                    data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
                }, {
                    name: 'New York',
                    data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
                }, {
                    name: 'Berlin',
                    data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
                }, {
                    name: 'London',
                    data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
                }]
            }
        },
    },
    mounted() {
        const chart =Highcharts.chart('pie_container', {
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false,
                type: 'pie'
            },
            title: {
                text: 'Industries composition',
                align: 'left'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            accessibility: {
                point: {
                    valueSuffix: '%'
                }
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
                }
            },
            series: [{
                name: 'Brands',
                colorByPoint: true,
                data: [{
                    name: 'Chrome',
                    y: 74.77,
                    sliced: true,
                    selected: true
                },  {
                    name: 'Edge',
                    y: 12.82
                },  {
                    name: 'Firefox',
                    y: 4.63
                }, {
                    name: 'Safari',
                    y: 2.44
                }, {
                    name: 'Internet Explorer',
                    y: 2.02
                }, {
                    name: 'Other',
                    y: 3.28
                }]
            }]
        });
    }
}
</script>


<style scoped>
h3 {
    margin: 40px 0 0;
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
