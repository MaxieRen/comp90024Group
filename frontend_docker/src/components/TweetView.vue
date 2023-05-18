<template>
    <div>
        <h2>Mastodon Tweets Analysis</h2>

        <div class="container" id="word-cl">
            <figure class="highcharts-figure">
                <div id="word-cloud-container"></div>
                <p class="highcharts-description">
                    Word clouds are used to visualize how often each word in a
                    text occurs. This example uses an excerpt from the book
                    Alice's Adventures in Wonderland. Words that appear often will appear
                    larger.
                </p>
            </figure>
        </div>

        <div id="buttons" class="container-fluid">
            <button @click="getData1">获取数据</button>
            <button @click="getData2" >update</button>
            <button @click="getData3" >reset</button>
        </div>

        <div class="container-lg py-4">
            <img src="https://img.icons8.com/external-filled-outline-design-circle/64/external-Twitter-website-communication-filled-outline-design-circle.png"/>
            <img src="https://img.icons8.com/color-glass/96/null/happy.png"/>
            <img src="https://img.icons8.com/color-glass/96/null/neutral-emoticon.png"/>
            <img src="https://img.icons8.com/color-glass/96/null/sad.png"/>
            <img src="https://img.icons8.com/dusk/64/sunrise.png" alt="sunrise"/>
            <img src="https://img.icons8.com/dusk/64/smiling-sun.png" alt="smiling-sun"/>
            <img src="https://img.icons8.com/dusk/64/sunset.png" alt="sunset"/>
            <img src="https://img.icons8.com/dusk/64/bright-moon.png" alt="bright-moon"/>
        </div>
        <ul>
            <li v-for="(item, index) in valdata" :key="index">{{ item }}</li> <!-- dynamically updated -->
        </ul>

        <div id="overview-chart1-container" class="container">
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
    </div>

</template>

<script>
import axios from 'axios';
import Highcharts from "highcharts";
import loadWordcloud from 'highcharts/modules/wordcloud';


export default {
    name: 'RegionView',

    props: {
        msg: String
    },
    data() {
        return {
            chart:null,
            valdata: [56,41,53,37,43],
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
                    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
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
                this.valdata = [56,41,53,36,43];
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
                this.valdata = [1,2,3,4,5,6,7,8];
            } catch (error) {
                console.log(error);
            }
        }
    },
    mounted() {

        loadWordcloud(Highcharts);

        const text =
                'Chapter 1. Down the Rabbit-Hole ' +
                'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: ' +
                'once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations ' +
                'in it, \'and what is the use of a book,\' thought Alice \'without pictures or conversation?\'' +
                'So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy ' +
                'and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking ' +
                'the daisies, when suddenly a White Rabbit with pink eyes ran close by her.',
            lines = text.replace(/[():'?0-9]+/g, '').split(/[,\. ]+/g),
            data = lines.reduce((arr, word) => {
                let obj = Highcharts.find(arr, obj => obj.name === word);
                if (obj) {
                    obj.weight += 1;
                } else {
                    obj = {
                        name: word,
                        weight: 1
                    };
                    arr.push(obj);
                }
                return arr;
            }, []);

        Highcharts.chart('word-cloud-container', {
            accessibility: {
                screenReaderSection: {
                    beforeChartFormat: '<h5>{chartTitle}</h5>' +
                        '<div>{chartSubtitle}</div>' +
                        '<div>{chartLongdesc}</div>' +
                        '<div>{viewTableButton}</div>'
                }
            },
            series: [{
                type: 'wordcloud',
                data,
                name: 'Occurrences'
            }],
            title: {
                text: 'Wordcloud of Alice\'s Adventures in Wonderland',
                align: 'left'
            },
            subtitle: {
                text: 'An excerpt from chapter 1: Down the Rabbit-Hole',
                align: 'left'
            },
            tooltip: {
                headerFormat: '<span style="font-size: 16px"><b>{point.key}</b></span><br>'
            }
        });

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
img{
    margin: 14px;
}
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

.highcharts-figure,
.highcharts-data-table table {
    margin: 1em auto;
}

.highcharts-data-table table {
    font-family: Verdana, sans-serif;
    border-collapse: collapse;
    border: 1px solid #ebebeb;
    margin: 10px auto;
    text-align: center;
    width: 100%;
    max-width: 500px;
}

.highcharts-data-table caption {
    padding: 1em 0;
    font-size: 1.2em;
    color: #555;
}

.highcharts-data-table th {
    font-weight: 600;
    padding: 0.5em;
}

.highcharts-data-table td,
.highcharts-data-table th,
.highcharts-data-table caption {
    padding: 0.5em;
}

.highcharts-data-table thead tr,
.highcharts-data-table tr:nth-child(even) {
    background: #f8f8f8;
}

.highcharts-data-table tr:hover {
    background: #f1f7ff;
}

</style>



