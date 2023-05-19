<template>
    <div>
        <h2>Twoots & Tweets Analysis</h2>
        <div class="container-lg py-4">
            <div class="row">
                <div class="col">
                    <div class="container" id="word-cl">
                        <figure class="highcharts-figure">
                            <div id="mast-word-cloud-container"></div>
                            <p class="highcharts-description">
                                Word clouds are used to visualize how often each word in all
                                twootes occurs. Words that appear often will appear
                                larger.
                            </p>
                        </figure>
                    </div>
                </div>
                <div class="col">
                    <div class="container" id="word-cl">
                        <figure class="highcharts-figure">
                            <div id="tweets-word-cloud-container"></div>
                            <p class="highcharts-description">
                                Word clouds are used to visualize how often each word in all
                                tweets occurs. Words that appear often will appear
                                larger.
                            </p>
                        </figure>
                    </div>
                </div>
            </div>
        </div>

        <div id="sentiment-cards" class="container-lg py-4">
            <div class="row">
                <div class="col">
                    <div id="sentiment" class="row shadow-lg p-2 bg-white rounded" style="height:250px;">
                        <h4>Over-all Sentiment (Mastodon)</h4>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/external-filled-outline-design-circle/64/external-Twitter-website-communication-filled-outline-design-circle.png"/>
                                <div class="insights-data pt-2">{{twoots}}</div>
                                <div class="insights-title" >Total Twootes</div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/color-glass/96/null/happy.png"/>
                                <div class="insights-data pt-2">{{mastPOS}}</div>
                                <div class="insights-title" >Positive</div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/color-glass/96/null/neutral-emoticon.png"/>
                                <div class="insights-data pt-2">{{ mastNEU }}</div>
                                <div class="insights-title">Neutral</div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/color-glass/96/null/sad.png"/>
                                <div class="insights-data pt-2">{{ mastNEG }}</div>
                                <div class="insights-title">Negative</div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>

<!--        <ul>-->
<!--            <li v-for="(item, index) in valdata" :key="index">{{ item }}</li> &lt;!&ndash; dynamically updated &ndash;&gt;-->
<!--        </ul>-->

        <div id="buttons" class="container-fluid">
            <button @click="updateCard" >update</button>
        </div>

        <div id="overview-chart1-container" class="container">
            <figure class="highcharts-figure">
                <div id="time-container" style="width:100%; height:400px;"></div>
                <p class="highcharts-description">
                    Chart showing the total number of twoots/tweets in different time blocks.
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
            mastPOS:null,
            mastNEU:null,
            mastNEG:null,
            twoots:null,
            chart: null,
            valdata: [56,41,53,37,43]
        };
    },
    async created(){
        const mastCount  = await  axios.get('http://115.146.92.228:8081/count_mastodon/');
        const pos = await axios.get("http://115.146.92.228:8081/sentiment_number/pos");
        const neu = await axios.get("http://115.146.92.228:8081/sentiment_number/neu");
        const neg = await axios.get("http://115.146.92.228:8081/sentiment_number/neg");
        this.mastPOS = pos.data;
        this.mastNEU = neu.data;
        this.mastNEG = neg.data;
        this.twoots = mastCount.data;

        const mastWC = await axios.get('http://115.146.92.228:8081/api_word_cloud/');
        const tweetWC =await  axios.get('http://115.146.92.228:8081/total_word_collect')
        loadWordcloud(Highcharts);
        Highcharts.chart('mast-word-cloud-container', {
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
                data: mastWC.data,
                name: 'Occurrences'
            }],
            title: {
                text: 'Twoots Word cloud 2023',
                align: 'left'
            },
            subtitle: {
                text: 'Mastodon',
                align: 'left'
            },
            tooltip: {
                headerFormat: '<span style="font-size: 16px"><b>{point.key}</b></span><br>'
            }
        });
        Highcharts.chart('tweets-word-cloud-container', {
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
                data:tweetWC.data,
                name: 'Occurrences'
            }],
            title: {
                text: 'Tweets Word cloud 2022',
                align: 'left'
            },
            subtitle: {
                text: 'Twitter',
                align: 'left'
            },
            tooltip: {
                headerFormat: '<span style="font-size: 16px"><b>{point.key}</b></span><br>'
            }
        });

        const tweetAT = await axios.get('http://115.146.92.228:8081/active_time_all_twitter/');
        const mastAT = await axios.get('http://115.146.92.228:8081/mastodon_activation_time/');

        Highcharts.chart( "time-container",{
            chart: {
                type: 'column'
            },
            title: {
                text: 'Activation Time'
            },
            subtitle: {
                text: 'Source: Twitter + Mastodon'
            },
            xAxis: {
                categories: ['3am - 9am','9am - 3pm','3pm - 9pm','9pm - 3am'],
                crosshair: true
            },
            yAxis: {
                min: 0,
                title: {text: 'Time ( 24 hr)'}
            },
            tooltip: {
                headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                    pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:1f} </b></td></tr>',
                    footerFormat: '</table>',
                    shared: true,
                    useHTML: true
            },
            plotOptions: {
                column: {
                    pointPadding: 0.2,
                        borderWidth: 0
                }
            },
            series: [{
                name: 'Twoots',
                data: mastAT.data

            }, {
                name: 'Tweets',
                data: tweetAT.data

            }]
        })


    },
    methods: {

        async updateCard(){
            const mastCount  = await  axios.get('http://115.146.92.228:8081/count_mastodon/');
            this.twoots = mastCount.data;
            const pos = await axios.get("http://115.146.92.228:8081/sentiment_number/pos");
            const neu = await axios.get("http://115.146.92.228:8081/sentiment_number/neu");
            const neg = await axios.get("http://115.146.92.228:8081/sentiment_number/neg");
            this.mastPOS = pos.data;
            this.mastNEU = neu.data;
            this.mastNEG = neg.data;
        }
    },

    mounted() {
        loadWordcloud(Highcharts);
        Highcharts.chart('mast-word-cloud-container', {
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

                name: 'Occurrences'
            }],
            title: {
                text: 'Twoots Word cloud',
                align: 'left'
            },
            subtitle: {
                text: 'Mastodon',
                align: 'left'
            },
            tooltip: {
                headerFormat: '<span style="font-size: 16px"><b>{point.key}</b></span><br>'
            }
        });
        Highcharts.chart('tweets-word-cloud-container', {
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
                name: 'Occurrences'
            }],
            title: {
                text: 'Tweets Word cloud',
                align: 'left'
            },
            subtitle: {
                text: 'Twitter',
                align: 'left'
            },
            tooltip: {
                headerFormat: '<span style="font-size: 16px"><b>{point.key}</b></span><br>'
            }
        });

    }
}
</script>

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



