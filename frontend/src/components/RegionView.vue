<template>

    <div>
        <div>
            <div class="container"  id = "map-container"> </div>
            <div id="unemp-legend" class="legend">
                <p>Unemployment Rate</p>
                <div><span style="background-color: #91d7ff"></span>0%</div>
                <div><span style="background-color: #146ec8"></span>1%</div>
                <div><span style="background-color: #0051a7"></span>3%</div>
                <div><span style="background-color: #ff9696"></span>5%</div>
                <div><span style="background-color: #d7160a"></span>7%</div>
                <div><span style="background-color: #b80000"></span>9%</div>
            </div>
        </div>
        <div class="container-fluid" id="button-container">
<!--            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">Year</button>-->
<!--            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">-->
<!--                <li><a class="dropdown-item" @click="getData1">2022</a></li>-->
<!--                <li><a class="dropdown-item" @click="getData1">2023</a></li>-->
<!--            </ul>-->
        </div>


        <h3>Insights Analysis</h3>
        <ul>{{string}}</ul>
        <div id="dashboard" class="container shadow-lg p-3 mb-5 bg-white rounded">
            <div class="row">
                <div class="col mt-3">
                    <div class="d-flex flex-column justify-content-center align-items-center">
                        <img src="https://img.icons8.com/nolan/512/1A6DFF/C822FF/twitter.png" alt="" class="snapshot-img"/>
                        <div class="insights-data pt-2">{{user}}</div>
                        <p class="insights-title" >Twitter User</p>
                        <p class="insights-title pb-2">(2022)</p>
                    </div>
                </div>
                <div class="col mt-3">
                    <div class="d-flex flex-column justify-content-center align-items-center">
                        <img src="https://img.icons8.com/nolan/96/1A6DFF/C822FF/satisfaction.png" alt="" class="snapshot-img"/>
                        <div class="insights-data pt-2">{{percentage}}</div>
                        <p class="insights-title" >Overall Satisfaction</p>
                        <p class="insights-title pb-2">(2022)</p>
                    </div>
                </div>

                <div class="col col-md-2 mt-3">
                    <div class="d-flex flex-column justify-content-center align-items-center">
                        <img src="../assets/images/working-age-population.svg" alt="" class="snapshot-img" />
                        <div class="insights-data pt-2">{{worker}}</div>
                        <p class="insights-title" >Working Age Population</p>
                        <p class="insights-title pb-2">(15-64)</p>
                    </div>
                </div>

                <div class="col col-md-2 mt-3">
                    <div class="d-flex flex-column justify-content-center align-items-center">
                        <img src="https://labourmarketinsights.gov.au/Content/assets/images/global/snapshot/employment-rate.svg"  alt="" class="snapshot-img" />
                        <div class="insights-data pt-2">{{empRate}}</div>
                        <p class="insights-title">Employment Rate </p>
                        <p class="insights-title">(15-64)</p>
                    </div>
                </div>

                <div class="col col-md-2 mt-3">
                    <div class="d-flex flex-column justify-content-center align-items-center">
                        <img src="https://labourmarketinsights.gov.au/Content/assets/images/global/snapshot/unemployment-rate.svg"  alt="" class="snapshot-img" />
                        <div class="insights-data pt-2">{{unempRate}}</div>
                        <p class="insights-title">Unemployment Rate</p>
                        <p class="insights-title pb-2">(15+)</p>
                    </div>
                </div>

                <div class="col col-md-2 mt-3">
                    <div class="d-flex flex-column justify-content-center align-items-center">
                        <img src="https://labourmarketinsights.gov.au/Content/assets/images/global/snapshot/youth-unemployment-rate.svg"  alt="" class="snapshot-img" />
                        <div class="insights-data pt-2">{{youth}}</div>
                        <p class="insights-title">Youth Unemployment Rate</p>
                        <p class="insights-title pb-2">(15-24)</p>
                    </div>
                </div>

            </div>
        </div>


        <div id="2-cards" class="container-lg py-4">
            <div class="row">
                <div class="col">
                    <div id="analysis" class="container" align="left" style="height:300px;">
                        <h4 class="card-title">
                            Summary
                        </h4>
                        <p class="card-text">
                            <ul>
                                <li>This page provides a snapshot of current labour market conditions.</li>
                            </ul>
                        </p>
                    </div>
                </div>
                <div class="col">
                    <div id="activation time" class="row shadow-lg p-2 bg-white rounded" style="height:260px;">
                        <h4>Activation Time </h4>
                        <p>{{string}}</p>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/dusk/64/sunrise.png" alt="sunrise"/>
                                <div class="insights-data pt-2">{{one}}</div>
                                <p class="insights-title" >3am - 9am</p>
                            </div>
                        </div>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/dusk/64/smiling-sun.png" alt="smiling-sun"/>
                                <div class="insights-data pt-2">{{two}}</div>
                                <p class="insights-title" >9am - 3pm</p>
                            </div>
                        </div>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/dusk/64/sunset.png" alt="sunset"/>
                                <div class="insights-data pt-2">{{three}}</div>
                                <p class="insights-title">3pm - 9pm</p>
                            </div>
                        </div>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/dusk/64/bright-moon.png" alt="bright-moon"/>
                                <div class="insights-data pt-2">{{four}}</div>
                                <p class="insights-title">9pm - 3am </p>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>


        <div id="charts" class="container-lg py-4">
            <div class="row">
                <div class="col">
                    <figure class="highcharts-figure">
                        <div id="age-container" style="width:100%; height:400px;"></div>
                        <p class="highcharts-description" align="left">
                            This chart shows the age profile of the population (aged 15 years +).
                        </p>
                    </figure>
                </div>
                <div class="col">
                    <figure class="highcharts-figure">
                        <div id="wc-container" style="width:100%; height:400px;"></div>
                        <p class="highcharts-description" align="left">
                            This chart shows the word frequency in this region.
                        </p>
                    </figure>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import mapboxgl from 'mapbox-gl';
import "mapbox-gl/dist/mapbox-gl.css";
import Highcharts from "highcharts";
import loadWordcloud from "highcharts/modules/wordcloud";

export default {
    name: 'TweetView',
    props: {
        msg: String
    },
    data() {
        return {
            user:null,
            percentage:null,
            worker:null,
            empRate:null,
            unempRate:null,
            youth:null,
            one:null,
            two:null,
            three:null,
            four:null,
            UNEMP_RATE: null,
            map: null,
            mapData: null,
            string:' ',
            string0:' '
        };
    },
    methods: {
        async getSA4WC(x,y) {
            try {
                const response = await axios.get('http://115.146.92.228:8081/api_word_cloud_twitter/'+x);
                const mastWC= response.data;

                loadWordcloud(Highcharts);
                Highcharts.chart('wc-container', {
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
                        data:mastWC,
                        name: 'Occurrences'
                    }],
                    title: {
                        text: 'Tweets Word cloud',
                        align: 'left'
                    },
                    subtitle: {
                        text: 'Area: '+y,
                        align: 'left'
                    },
                    tooltip: {
                        headerFormat: '<span style="font-size: 16px"><b>{point.key}</b></span><br>'
                    }
                });
            } catch (error) {
                console.log(error);
            }
        },
        async getSA4age(x,y) {
            try {
                const ageFemales = await axios.get('http://115.146.92.228:8081/unemployment_age/'+x+'/Females');
                const ageMales = await axios.get('http://115.146.92.228:8081/unemployment_age/'+x+'/Males');

                Highcharts.chart('age-container', {
                    chart: {
                        type: 'column'
                    },
                    title: {
                        text: 'Unemployment by Age',
                        align: 'left'
                    },
                    subtitle: {
                        text: 'Area: '+y,
                        align: 'left'
                    },
                    xAxis: {
                        categories: ['15-24 years', '25-34 years', '35-44 years', '45-54 years','55-64 years','65+ years']
                    },
                    yAxis: {
                        min: 0,
                        title: {
                            text: 'Population'
                        },
                        stackLabels: {
                            enabled: true,
                            style: {
                                fontWeight: 'bold',
                                color: (
                                    Highcharts.defaultOptions.title.style &&
                                    Highcharts.defaultOptions.title.style.color
                                ) || 'gray',
                                textOutline: 'none'
                            }
                        }
                    },
                    legend: {
                        align: 'left',
                        x: 70,
                        verticalAlign: 'top',
                        y: 70,
                        floating: true,
                        backgroundColor:
                            Highcharts.defaultOptions.legend.backgroundColor || 'white',
                        borderColor: '#CCC',
                        borderWidth: 1,
                        shadow: false
                    },
                    tooltip: {
                        headerFormat: '<b>{point.x}</b><br/>',
                        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
                    },
                    plotOptions: {
                        column: {
                            stacking: 'normal',
                            dataLabels: {
                                enabled: true
                            }
                        }
                    },
                    series: [{
                        name: 'Male',
                        data: ageMales.data
                    }, {
                        name: 'Female',
                        data: ageFemales.data
                    }]
                });
            } catch (error) {
                console.log(error);
            }
        },
        async updateRegion(x,users,sentiment){
            try {
                const working = await axios.get('http://115.146.92.228:8081/labour_2022/'+x+'/2022_working_age_population');
                const unemp = await axios.get('http://115.146.92.228:8081/labour_2022/'+x+'/2022_unemployment_rate_15_plus');
                const emp = await axios.get('http://115.146.92.228:8081/labour_2022/'+x+'/2022_employment_rate_15_64');
                const youth = await axios.get('http://115.146.92.228:8081/labour_2022/'+x+'/2022_youth_unemployment_rate_15_24')
                this.worker = working.data;
                this.unempRate =unemp.data;
                this.empRate =emp.data;
                this.youth = youth.data;

                const time1 = await axios.get('http://115.146.92.228:8081/area_active_time/'+x+'/0');
                const time2 = await axios.get('http://115.146.92.228:8081/area_active_time/'+x+'/1');
                const time3 = await axios.get('http://115.146.92.228:8081/area_active_time/'+x+'/2');
                const time4 = await axios.get('http://115.146.92.228:8081/area_active_time/'+x+'/3');
                this.one = time1.data;
                this.two = time2.data;
                this.three =time3.data;
                this.four = time4.data;

                this.user = users;
                this.percentage = sentiment;
            }
            catch (error){
            console.log(error)}

        }
    },

    mounted() { //load map data after render
        mapboxgl.accessToken = 'pk.eyJ1IjoibWF4aWVtYXhpZSIsImEiOiJjbGg3YmJmYngwN2gzM25ydXQwbHk0NjA3In0.xCCDQe7H6UFezNyi5yDbBQ';
        this.map = new mapboxgl.Map({
            container: 'map-container',
            style: 'mapbox://styles/maxiemaxie/clh9u62ox00c701rh24ol9n52',
            maxBounds:[95.82, -44.44, 173, -10.14],
            projection: {name: 'mercator'},
            zoom: 1,
            attributionControl: false
        });

        let hoveredStateId = null;
        this.map.on('load', () => {
            this.map.addSource('sa4Layer', {
                'type': 'geojson',
                'data': 'https://maxieren.github.io/sa4LAYERsimp.geojson',
                generateId: true
            });

            // The feature-state dependent fill-opacity expression will render the hover effect when a feature's hover state is set to true.
            this.map.addLayer({
                'id': 'sa4-fills',
                'type': 'fill',
                'source': 'sa4Layer',
                'layout': {},
                'paint': {
                    'fill-color': {
                        property: 'UNEMP_RATE',
                        stops: [[0, '#91d7ff'], [1, '#146ec8'], [3, '#0051a7'], [5, '#ff9696'], [7, '#d7160a'], [9, '#b80000']]
                    },
                    'fill-opacity': [
                        'case', ['boolean', ['feature-state', 'hover'], false],
                        1, 0.5
                    ]
                }
            });

            this.map.addLayer({
                'id': 'state-borders',
                'type': 'line',
                'source': 'sa4Layer',
                'layout': {},
                'paint': {
                    'line-color': '#6484e3',
                    'line-width': 2
                }
            });

            // Create a popup, but don't add it to the map yet.
            const popup = new mapboxgl.Popup({
                closeButton: false,
                closeOnClick: false
            });

            this.map.on('click', 'sa4-fills', (e) => {
                // Copy coordinates array.
                const coordinates = e.lngLat;
                const sa4code = e.features[0].properties.SA4_CODE21;
                const description = e.features[0].properties.SA4_NAME21;
                new mapboxgl.Popup().setLngLat(coordinates).setHTML('<h4>Selected!</h4>').addTo(this.map);
                this.getSA4WC(sa4code,description);
                this.getSA4age(sa4code,description);
                const sent = e.features[0].properties.SENTIMENT;
                const users = e.features[0].properties.USER_COUNT;
                this.updateRegion(sa4code,users,sent);
                this.string = "Selected Area: "+ description+ " ("+sa4code+") "
            });

            // When the user moves their mouse over the state-fill layer, we'll update the feature state for the feature under the mouse.
            this.map.on('mousemove', 'sa4-fills', (e) => {
                this.map.getCanvas().style.cursor = 'pointer';
                if (e.features.length > 0) {
                    if (hoveredStateId !== null) {
                        this.map.setFeatureState(
                            { source: 'sa4Layer', id: hoveredStateId },
                            { hover: false }
                        );
                    }
                    hoveredStateId = e.features[0].id;
                    this.map.setFeatureState(
                        { source: 'sa4Layer', id: hoveredStateId },
                        { hover: true }
                    );
                }
                const description = e.features[0].properties.SA4_NAME21;
                const sent = e.features[0].properties.SENTIMENT;
                const users = e.features[0].properties.USER_COUNT;
                const unempRate = e.features[0].properties.UNEMP_RATE;
                popup.setLngLat(e.lngLat).setHTML(description+"<br> UnEmp Rate: "+ unempRate +"%<br> Sentiment: "+ sent +"<br> User count: "+ users).addTo(this.map);
            });

            // When the mouse leaves the state-fill layer, update the feature state of the previously hovered feature.
            this.map.on('mouseleave', 'sa4-fills', () => {
                if (hoveredStateId !== null) {
                    this.map.setFeatureState(
                        { source: 'sa4Layer', id: hoveredStateId },
                        { hover: false }
                    );
                }
                hoveredStateId = null;
                // Reset the cursor style
                this.map.getCanvas().style.cursor = '';
                popup.remove();
            });

        });



        Highcharts.chart('age-container', {
            chart: {
                type: 'column'
            },
            title: {
                text: 'Unemployment by Age',
                align: 'left'
            },
            subtitle: {
                text: 'Source: SUDO',
                align: 'left'
            },
            xAxis: {
                categories: ['15-24 years', '25-34 years', '35-44 years', '45-54 years','55-64 years','65+ years']
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Count trophies'
                },
                stackLabels: {
                    enabled: true,
                    style: {
                        fontWeight: 'bold',
                        color: ( // theme
                            Highcharts.defaultOptions.title.style &&
                            Highcharts.defaultOptions.title.style.color
                        ) || 'gray',
                        textOutline: 'none'
                    }
                }
            },
            legend: {
                align: 'left',
                x: 70,
                verticalAlign: 'top',
                y: 70,
                floating: true,
                backgroundColor:
                    Highcharts.defaultOptions.legend.backgroundColor || 'white',
                borderColor: '#CCC',
                borderWidth: 1,
                shadow: false
            },
            tooltip: {
                headerFormat: '<b>{point.x}</b><br/>',
                pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
            },
            plotOptions: {
                column: {
                    stacking: 'normal',
                    dataLabels: {
                        enabled: true
                    }
                }
            }
        });

        loadWordcloud(Highcharts);
        Highcharts.chart('wc-container', {
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
    },
}



</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h3 {
    margin: 40px 0 0;
}

p{
    font-size: small;
}


#map-container {
    left: 50px;
    height: 610px;
    width: 1200px;
}

button {
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

.legend {
    background-color: #fff;
    border-radius: 3px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
    font: 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;
    padding: 10px;
    position: absolute;
    top: 700px;
    left: 200px;
    z-index: 1;
}

.legend div span {
    border-radius: 50%;
    display: inline-block;
    height: 10px;
    margin-right: 5px;
    width: 10px;
}
</style>
