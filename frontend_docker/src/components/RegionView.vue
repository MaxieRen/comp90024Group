<template>

    <div>
        <div>
            <div class="container"  id = "map-container"> </div>
        </div>
        <div class="container-fluid" id="button-containter">
            <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-bs-toggle="dropdown" aria-expanded="false">Year</button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                <li><a class="dropdown-item" @click="getData1">2020</a></li>
                <li><a class="dropdown-item" @click="getData1">2021</a></li>
                <li><a class="dropdown-item" @click="getData1">2022</a></li>
                <li><a class="dropdown-item" @click="getData1">2023</a></li>
            </ul>
            <button @click="getData1">Update</button>
            <button @click="getData2">Reset</button>
        </div>
        <img src="https://img.icons8.com/nolan/512/1FB141/icons8-new-logo.png" alt="" class="snapshot-img" />

        <h3>Insights Analysis</h3>
        <ul>{{string}}</ul>
        <div id="dashboard" class="container shadow-lg p-3 mb-5 bg-white rounded">
            <div class="row mb-3">
                <div class="col-xs-12 col-sm-12 col-md-2 mt-3">
                    <div class="d-flex flex-column justify-content-center align-items-center">
                        <img src="https://img.icons8.com/nolan/512/1A6DFF/C822FF/twitter.png" alt="" class="snapshot-img" />
                        <div class="insights-data pt-2">17,028,900</div>
                        <div class="insights-title" >Related Twitter</div>
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
        <div id="analysis" class="container" align="left" style="height:300px;">
            <h4 class="card-title">
                We research and analyse employment dynamics across groups, industries, occupations and regions.
                We share what we have learnt so you can make informed decisions.</h4>
            <p class="card-text">
                <ul>
                    <li>Stay up-to-date with conditions in your local labour market</li>
                    <li>Identify jobs and skills in-demand</li>
                    <li>Understand employer needs and recruitment trends</li>
                    <li>Explore the trends impacting the jobs market now and into the future.</li>
                </ul>
            </p>
        </div>
        <div class = "container">
            <figure class="highcharts-figure">
                <div id="gender-chart-container" style="width:100%; height:400px;"></div>
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
import mapboxgl from 'mapbox-gl';
import "mapbox-gl/dist/mapbox-gl.css";
import Highcharts from "highcharts";

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
            string:'这里可以显示一些文字'
        };
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
                const response = await axios.get('http://45.113.235.46:8081/api_1');
                console.log(response.data.features);
                this.data = response.data;
            } catch (error) {
                console.log(error);
            }
        }
    },

    mounted() {
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
                popup.setLngLat(e.lngLat).setHTML(e.features[0].properties.SA4_NAME21).addTo(this.map);
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

        const chart = Highcharts.chart('gender-chart-container', {
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
                    'target="_blank">ABS</a>',
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
