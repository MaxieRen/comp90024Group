

<template>

    <div id="overview-chart">
        <highcharts id = "chart1" :options="chartOptions" ref="highcharts"></highcharts>
    </div>

    <div id="overview-chart-2"></div>
    <button >update</button> <button >reset</button>


    <div class="container mt-3">
        <div class="insights-card mb-5">
            <h3 class="text-center mb-3">
                Employment Insights for Australia
            </h3>
            <div class="container-fluid">
                <div class="row mb-3">
                    <div class="col-xs-12 col-sm-12 col-md-3 mt-3">
                        <div class="d-flex flex-column justify-content-center align-items-center">
                            <img src="../assets/images/working-age-population.svg" alt="" class="snapshot-img" />
                            <div class="insights-data pt-2">17,028,900</div>
                            <div class="insights-title" >Working Age Population</div>
                            <div class="insights-title pb-2">(15-64)</div>
                        </div>
                    </div>

                    <div class="col-xs-12 col-sm-12 col-md-2 mt-3">
                        <div class="d-flex flex-column justify-content-center align-items-center">
                            <img src="https://labourmarketinsights.gov.au/Content/assets/images/global/snapshot/employment-rate.svg"  alt="" class="snapshot-img" />

                            <div class="insights-data pt-2">77.6%</div>
                            <div class="insights-title">
                                Employment Rate
                            </div>
                            <div class="insights-title">
                                (15-64)
                            </div>
                        </div>
                    </div>

                    <div class="col-xs-12 col-sm-12 col-md-2 mt-3">
                        <div class="d-flex flex-column justify-content-center align-items-center">
                            <img src="https://labourmarketinsights.gov.au/Content/assets/images/global/snapshot/participation-rate.svg"  alt="" class="snapshot-img" />
                            <div class="insights-data pt-2">66.7%</div>
                            <div class="insights-title">
                                Participation Rate
                            </div>
                            <div class="insights-title">
                                (15+)
                            </div>
                        </div>
                    </div>

                    <div class="col-xs-12 col-sm-12 col-md-2 mt-3">
                        <div class="d-flex flex-column justify-content-center align-items-center">
                            <img src="https://labourmarketinsights.gov.au/Content/assets/images/global/snapshot/unemployment-rate.svg"  alt="" class="snapshot-img" />
                            <div class="insights-data pt-2">3.5%</div>
                            <div class="insights-title">
                                Unemployment Rate
                            </div>
                            <div class="insights-title pb-2">
                                (15+)
                            </div>
                        </div>
                    </div>

                    <div class="col-xs-12 col-sm-12 col-md-3 mt-3">
                        <div class="d-flex flex-column justify-content-center align-items-center">
                            <img src="https://labourmarketinsights.gov.au/Content/assets/images/global/snapshot/youth-unemployment-rate.svg"  alt="" class="snapshot-img" />

                            <div class="insights-data pt-2">7.8%</div>
                            <div class="insights-title">
                                Youth Unemployment Rate
                            </div>
                            <div class="insights-title pb-2">
                                (15-24)
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>




<script>
import axios from "axios";
import Highcharts from "highcharts";

export default {
    name: 'OverView',
    props: {
        msg: String
    },
    data() {
        return {
            data: [],
            map: null,
            mapData: null,
            string:'这里可以显示一些文字',
            chartOptions : {
                        title: {
                            text: 'Unemployment Rate',
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
        }
    },
    methods: {
        async getData1() {
            try {
                // const response = await axios.get('http://127.0.0.1:8081/api_1');
                // console.log(response.data);
                // this.data = response.data;
                this.string = "已更新"
            } catch (error) {
                console.log(error);
            }
        },
        async getData2() {
            try {
                const response = await axios.post('http://127.0.0.1:8081/api_1');
                console.log(response.data);
                this.data = response.data;
            } catch (error) {
                console.log(error);
            }
        }
    },
    mounted() {
        Highcharts.chart('overview-chart-2', {
            title: {
                text: 'Unemployment Ratee'
            },
            subtitle: {
                text: 'Data input from CSV'
            },
            data: {
                csvURL:'../assets/datasets/unemployment-rate-austra.csv',
            },
            series: [
                {
                color: '#c4392d',
                negativeColor: '#5679c4',
                fillOpacity: 0.5
            }]
        });
    }
}
</script>


<style scoped>

img {
    height: 50px;
}
h1 {
    p {
        margin-bottom: 0;
    }
    font-size: 3.1em;
    color: #161471;
    font-weight: bold;
}

h2 {
    font-size: 2em;
    color: #161471;
    font-weight: bold;
}

h3 {
    font-size: 1.5em;
    color: #161471;
    font-weight: bold;
}

h4 {
    font-size: 1.25em;
    color: #161471;
    font-weight: bold;
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