<template>
    <div>
        <div class="container-fluid" style="height: 720px">
            <div id = "map"> </div>
        </div>

        <div class="container-fluid" >
            <button @click="getData1">更新地图</button>
            <button @click="getData2">reset map</button>
        </div>

        <h3>This is 3rd View</h3>
        <ul>{{string}}</ul>
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
</template>

<script>
import axios from 'axios';
import mapboxgl from 'mapbox-gl';


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
                const response = await axios.post('http://127.0.0.1:8081/api_1');
                console.log(response.data);
                this.data = response.data;
            } catch (error) {
                console.log(error);
            }
        }
    },
    mounted() {
        mapboxgl.accessToken = 'pk.eyJ1IjoibWF4aWVtYXhpZSIsImEiOiJjbGg3YmJmYngwN2gzM25ydXQwbHk0NjA3In0.xCCDQe7H6UFezNyi5yDbBQ';
        this.map = new mapboxgl.Map({
            container: 'map',
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
                'data': 'https://maxieren.github.io/sa4LAYERsimp.geojson'
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

            // When the user moves their mouse over the state-fill layer, we'll update the feature state for the feature under the mouse.
            this.map.on('mousemove', 'sa4-fills', (e) => {
                if (e.features.length > 0) {
                    if (hoveredStateId !== null) {
                        this.map.setFeatureState(
                            { source: 'sa4Layer', id: hoveredStateId },
                            { hover: false }
                        );
                    }
                    hoveredStateId = parseInt(e.features[0].properties.SA4_CODE21);

                    this.map.setFeatureState(
                        { source: 'sa4Layer', id: hoveredStateId },
                        { hover: true }
                    );
                }
            });

// When the mouse leaves the state-fill layer, update the feature state of the previously hovered feature.
            this.map.on('mouseleave', 'sa4-fills', () => {
                if (hoveredStateId !== null) {
                    this.map.setFeatureState(
                        { source: 'states', id: hoveredStateId },
                        { hover: false }
                    );
                }
                hoveredStateId = null;
            });
        });
    },
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

#map {
    text-align: center;
    position: relative;
    left: 70px;
    border: 4px solid #ccc;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.5);
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
