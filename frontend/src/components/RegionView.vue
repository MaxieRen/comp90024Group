<template>

    <div>
        <div>
            <div class="container"  id = "map-container"> </div>
        </div>
        <div class="container-fluid" id="button-container">
<!--            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">Year</button>-->
<!--            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">-->
<!--                <li><a class="dropdown-item" @click="getData1">2022</a></li>-->
<!--                <li><a class="dropdown-item" @click="getData1">2023</a></li>-->
<!--            </ul>-->
            <button @click="getData1">Update</button>
            <button @click="getData2">Reset</button>
            <button @click="getData2">Update</button>
        </div>


        <h3>Insights Analysis</h3>
        <ul>{{string}}</ul>
        <div id="dashboard" class="container shadow-lg p-3 mb-5 bg-white rounded">
            <div class="row mb-3">
                <div class="col-xs-12 col-sm-12 col-md-2 mt-3">
                    <div class="d-flex flex-column justify-content-center align-items-center">
                        <img src="https://img.icons8.com/nolan/512/1A6DFF/C822FF/twitter.png" alt="" class="snapshot-img" />
                        <div class="insights-data pt-2">17,028,900</div>
                        <div class="insights-title" >Twitter User</div>
                        <div class="insights-title pb-2">(2022 only)</div>
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


        <div id="2-cards" class="container-lg py-4">
            <div class="row">
                <div class="col">
                    <div id="analysis" class="container" align="left" style="height:300px;">
                        <h4 class="card-title">
                            We research and analyse employment dynamics across groups, industries, occupations and regions.</h4>
                        <p class="card-text">
                            <ul>
                                <li>Stay up-to-date with conditions in your local labour market</li>
                                <li>Identify jobs and skills in-demand</li>
                                <li>Understand employer needs and recruitment trends</li>
                                <li>Explore the trends impacting the jobs market now and into the future.</li>
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
                                <div class="insights-data pt-2">17,028,900</div>
                                <div class="insights-title" >3am - 9am</div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/dusk/64/smiling-sun.png" alt="smiling-sun"/>
                                <div class="insights-data pt-2">17,028,900</div>
                                <div class="insights-title" >9am - 3pm</div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/dusk/64/sunset.png" alt="sunset"/>
                                <div class="insights-data pt-2">17,028,900</div>
                                <div class="insights-title">3pm - 9pm</div>
                            </div>
                        </div>
                        <div class="col">
                            <div class="d-flex flex-column justify-content-center align-items-center">
                                <img src="https://img.icons8.com/dusk/64/bright-moon.png" alt="bright-moon"/>
                                <div class="insights-data pt-2">17,028,900</div>
                                <div class="insights-title">9pm - 3am </div>
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
                        <p class="highcharts-description">
                        </p>
                    </figure>
                </div>
                <div class="col">
                    <figure class="highcharts-figure">
                        <div id="wc-container" style="width:100%; height:400px;"></div>
                        <p class="highcharts-description">
                        </p>
                    </figure>
                </div>
            </div>
            <p>{{string0}}</p>
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
            data: [],
            map: null,
            mapData: null,
            string:' ',
            string0:' '
        };
    },
    methods: {
        async getData1() {
            try {
                // const response = await axios.get('http://127.0.0.1:8081/api_1');
                // console.log(response.data);
                // this.data = response.data;

            } catch (error) {
                console.log(error);
            }
        },
        async getData2() {
            try {
                const response = await axios.get('http://45.113.235.46:8081/api_1');
                console.log(response.data.features);
                this.data = response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async getSA4WC(x,y) {
            try {
                const response = await axios.get('http://45.113.235.46:8081/api_word_cloud_twitter/'+x);
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
                const ageFemales = await axios.get('http://45.113.235.46:8081/unemployment_age/'+x+'/Females');
                const ageMales = await axios.get('http://45.113.235.46:8081/unemployment_age/'+x+'/Males');
                console.log(ageFemales);
                console.log(ageMales.data);
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
                    'fill-color': '#627BC1',
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
                new mapboxgl.Popup().setLngLat(coordinates).setHTML('<h3>Selected!</h3>').addTo(this.map);
                this.getSA4WC(sa4code,description);
                this.getSA4age(sa4code,description);
                this.string = "Selected Area: "+ description+ " ("+sa4code+") "
                this.string0 = "Unemployment Rate: "

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
                console.log(e.lngLat);
                popup.setLngLat(e.lngLat).setHTML(description+"<br>" + "Sentiment : ").addTo(this.map);
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


</style>
