
<template>
    <div class = "container">
        <figure class="highcharts-figure">
            <div id="aus-20years-container" style="width:100%; height:400px;"></div>
            <p class="highcharts-description" align="left">
                The chart above gives a high level view of unemployment during events like the:
                Global Financial Crisis (GFC) from mid-2007 to early 2009;
                Mining boom in the 2010s; and the COVID-19 pandemic from early 2020.
            </p>
        </figure>
    </div>

    <div class="container mt-3">
        <div class="insights-card mb-5">
            <h3 class="text-center mb-3">
                Employment Insights for Australia
            </h3>
            <div id="dashboard" class="container shadow-lg p-3 mb-5 bg-white rounded">
                <div class="row mb-3">
                    <div class="col-xs-12 col-sm-12 col-md-2 mt-3">
                        <div class="d-flex flex-column justify-content-center align-items-center">
                            <img src="https://img.icons8.com/nolan/512/1A6DFF/C822FF/twitter.png" alt="" class="snapshot-img" />
                            <div class="insights-data pt-2">{{size}}</div>
                            <div class="insights-title" >Twitter Numbers</div>
                            <div class="insights-title pb-2">(2022 - now)</div>
                        </div>
                    </div>

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
                            <div class="insights-title">Employment Rate </div>
                            <div class="insights-title">(15-64)</div>
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

    <div id="analysis" class="container" align="left" style="height:300px;">
        <h4 class="card-title">
            Summary:</h4>
        <p class="card-text">
            <ul>
                <li>A person is considered employed if they are aged 15 years and over and work for an hour or more for pay,
                    profit, commission or payment in kind during the ABS Labour Force Survey reference week.</li>
                <li>A person is considered unemployed if they are not employed,
                    have actively looked for work at some time in the last four weeks,
                    and are currently available for work.</li>
                <li> The unemployment rate refers to the number of unemployed people expressed
                    as a proportion of the total labour force (employed and unemployed).</li>
                <li>The youth unemployment rate refers to the number of unemployed young people (aged 15-24 years old) expressed as
                    a proportion of the labour force aged 15-24 years old (employed and unemployed).</li>
            </ul>
        </p>
    </div>

    <div id="age-container" class="container">
        <figure class="highcharts-figure">
            <highcharts :options="chartOptions"></highcharts>
            <p class="highcharts-description" align="left">
                Chart showing how many people are employed/unemployed in different age group.
                <br>{{analysis}}
            </p>
        </figure>
    </div>

    <button @click="getEmp">Employment</button>
    <button @click="getUnemp">Unemployment</button>
    <ul>{{string}}</ul>
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
            size:null,
            analysis:'',
            string:'',
            chartOptions : {
                title: {
                    text: 'Age Population (Employment)',
                    align: 'left'
                },
                xAxis: {
                    categories: ['15-24 Years', '25-34 Years', "35-44 years", "45-54 years", "55-64 years","65 years and over"]
                },
                yAxis: {
                    title: {
                        text: 'Population'
                    }
                },
                tooltip: {
                    valueSuffix: 'million people'
                },
                plotOptions: {
                    series: {
                        borderRadius: '25%'
                    }
                },
                series: [
                    {
                        type: 'column',
                        name: '2019',
                        data: [
                            2.117,
                            3.4473,
                            3.1313,
                            2.939,
                            2.0721,
                            0.5077
                        ]
                    },
                    {
                    type: 'column',
                    name: '2020',
                    data: [
                        1.9524,
                        3.3552,
                        3.1645,
                        2.92,
                        2.084,
                        0.499
                    ]
                }, {
                    type: 'column',
                    name: '2021',
                    data: [
                        2.0525,
                        3.3876,
                        3.303,
                        2.9786,
                        2.1592,
                        0.5614
                    ]
                }, {
                    type: 'column',
                    name: '2022',
                    data: [
                        2.2967,
                        3.51,
                        3.4467,
                        3.0494,
                        2.2221,
                        0.5864
                    ]
                }, {
                    type: 'spline',
                    name: 'Average',
                    data: [1.8254, 3.425, 3.2614, 2.972, 2.1343, 0.5386],
                    marker: {
                        lineWidth: 2,
                        lineColor: Highcharts.getOptions().colors[3],
                        fillColor: 'white'
                    }
                }]
            },
        }
    },
    async created() {
        const count  = await  axios.get('http://115.146.92.228:8081/count_mastodon_twitter/');
        this.size = count.data;

        const time = await axios.get('http://115.146.92.228:8081/api_overview/time');
        const female = await axios.get('http://115.146.92.228:8081/api_overview/female_unemployment_rate');
        const male= await axios.get('http://115.146.92.228:8081/api_overview/male_unemployment_rate');
        const youth= await axios.get('http://115.146.92.228:8081/api_overview/youth_unemployment_rate');
        const aus = await axios.get('http://115.146.92.228:8081/api_overview/unemployment_rate');

        Highcharts.chart('aus-20years-container',{
            title: {
                text: 'Unemployment rate, Australia (20 years)',
                x: -20 //center
            },
            subtitle: {
                text: 'Source: SUDO + abs.gov.au (Seasonly Adjusted)',
                x: -20
            },
            xAxis: {
                categories: time.data
            },
            yAxis: {
                title: {
                    text: 'Rate (%)'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                valueSuffix: '%'
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            },
            series: [{
                name: 'Male',
                data: male.data,
                allowPointSelect: true
            }, {
                name: 'Female',
                data: female.data,
                allowPointSelect: true
            }, {
                name: 'Youth(15-24)',
                data: youth.data,
                allowPointSelect: true
            }, {
                name: 'Aus',
                data: aus.data,
                allowPointSelect: true
            }]
        })
    },
    methods: {
        async getEmp() {
            try {
                const emp2019 = await axios.get('http://115.146.92.228:8081/age_population/2019/employed');
                const emp2020 = await axios.get('http://115.146.92.228:8081/age_population/2020/employed');
                const emp2021 = await axios.get('http://115.146.92.228:8081/age_population/2021/employed');
                const emp2022 = await axios.get('http://115.146.92.228:8081/age_population/2022/employed');

                this.chartOptions = {
                    title: {
                        text: 'Age Population (Employment)',
                        align: 'left'
                    },
                    plotOptions: {
                        series: {
                            borderRadius: '25%'
                        }
                    },
                    series: [
                        {
                            type: 'column',
                            name: '2019',
                            data: emp2019.data
                        },
                        {
                            type: 'column',
                            name: '2020',
                            data: emp2020.data
                        }, {
                            type: 'column',
                            name: '2021',
                            data: emp2021.data
                        }, {
                            type: 'column',
                            name: '2022',
                            data: emp2022.data
                        }, {
                            type: 'spline',
                            name: 'Average',
                            data: [1.8254, 3.425, 3.2614, 2.972, 2.1343, 0.5386],
                            marker: {
                                lineWidth: 2,
                                lineColor: Highcharts.getOptions().colors[3],
                                fillColor: 'white'
                            }
                        }]
                };
                this.string = "Updated!"
                this.analysis="Most people employed are between age 25 - 54 years."
            } catch (error) {
                console.log(error);
            }
        },
        async getUnemp() {
            try {
                const unemp2019 = await axios.get('http://115.146.92.228:8081/age_population/2019/unemployed');
                const unemp2020 = await axios.get('http://115.146.92.228:8081/age_population/2020/unemployed');
                const unemp2021 = await axios.get('http://115.146.92.228:8081/age_population/2021/unemployed');
                const unemp2022 = await axios.get('http://115.146.92.228:8081/age_population/2022/unemployed');

                this.chartOptions = {
                    title: {
                        text: 'Age Population (Unemployment)',
                        align: 'left'
                    },
                    series: [
                        {
                            type: 'column',
                            name: '2019',
                            data: unemp2019.data
                        },
                        {
                            type: 'column',
                            name: '2020',
                            data: unemp2020.data
                        }, {
                            type: 'column',
                            name: '2021',
                            data: unemp2021.data
                        }, {
                            type: 'column',
                            name: '2022',
                            data: unemp2022.data
                        }, {
                            type: 'spline',
                            name: 'Average',
                            data: [0.2077, 0.1117, 0.0635, 0.055,0.0373,0.0015],
                            marker: {
                                lineWidth: 2,
                                lineColor: Highcharts.getOptions().colors[3],
                                fillColor: 'white'
                            }
                        }]
                };

                this.analysis="People in 15 - 24 years group have higher unemployment rate."
            } catch (error) {
                console.log(error);
            }
        },
        async getCount(){
            const count  = await  axios.get('http://115.146.92.228:8081/count_mastodon_twitter/');
            this.size = count.data;
        }
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
    width: 120px;
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