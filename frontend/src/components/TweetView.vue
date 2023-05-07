<template>

    <div>
        <div id ="container1">
            <div class="container-fluid"  id = "map-container"> </div>
        </div>

        <div class="container-fluid" >
            <button @click="getData1">更新地图</button>
            <button @click="getData2">reset map</button>
        </div>

        <h3>Twitter Analysis</h3>
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
            });
        });
        const startYear = 1960,
            endYear = 2018,
            btn = document.getElementById('play-pause-button'),
            input = document.getElementById('play-range'),
            nbr = 20;

        let dataset, chart;


        /*
         * Animate dataLabels functionality
         */
        (function (H) {
            const FLOAT = /^-?\d+\.?\d*$/;

            // Add animated textSetter, just like fill/strokeSetters
            H.Fx.prototype.textSetter = function () {
                let startValue = this.start.replace(/ /g, ''),
                    endValue = this.end.replace(/ /g, ''),
                    currentValue = this.end.replace(/ /g, '');

                if ((startValue || '').match(FLOAT)) {
                    startValue = parseInt(startValue, 10);
                    endValue = parseInt(endValue, 10);

                    // No support for float
                    currentValue = Highcharts.numberFormat(
                        Math.round(startValue + (endValue - startValue) * this.pos),
                        0
                    );
                }

                this.elem.endText = this.end;

                this.elem.attr(this.prop, currentValue, null, true);
            };

            // Add textGetter, not supported at all at this moment:
            H.SVGElement.prototype.textGetter = function () {
                const ct = this.text.element.textContent || '';
                return this.endText ? this.endText : ct.substring(0, ct.length / 2);
            };

            // Temporary change label.attr() with label.animate():
            // In core it's simple change attr(...) => animate(...) for text prop
            H.wrap(H.Series.prototype, 'drawDataLabels', function (proceed) {
                const attr = H.SVGElement.prototype.attr,
                    chart = this.chart;

                if (chart.sequenceTimer) {
                    this.points.forEach(point =>
                        (point.dataLabels || []).forEach(
                            label =>
                                (label.attr = function (hash) {
                                    if (hash && hash.text !== undefined) {
                                        const text = hash.text;

                                        delete hash.text;

                                        return this
                                            .attr(hash)
                                            .animate({ text });
                                    }
                                    return attr.apply(this, arguments);

                                })
                        )
                    );
                }

                const ret = proceed.apply(
                    this,
                    Array.prototype.slice.call(arguments, 1)
                );

                this.points.forEach(p =>
                    (p.dataLabels || []).forEach(d => (d.attr = attr))
                );

                return ret;
            });
        }(Highcharts));


        function getData(year) {
            const output = Object.entries(dataset)
                .map(country => {
                    const [countryName, countryData] = country;
                    return [countryName, Number(countryData[year])];
                })
                .sort((a, b) => b[1] - a[1]);
            return [output[0], output.slice(1, nbr)];
        }

        function getSubtitle() {
            const population = (getData(input.value)[0][1] / 1000000000).toFixed(2);
            return `<span style="font-size: 80px">${input.value}</span>
        <br>
        <span style="font-size: 22px">
            Total: <b>: ${population}</b> billion
        </span>`;
        }

        (async () => {

            dataset = await fetch(
                'https://demo-live-data.highcharts.com/population.json'
            ).then(response => response.json());


            chart = Highcharts.chart('container', {
                chart: {
                    animation: {
                        duration: 500
                    },
                    marginRight: 50
                },
                title: {
                    text: 'World population by country',
                    align: 'left'
                },
                subtitle: {
                    useHTML: true,
                    text: getSubtitle(),
                    floating: true,
                    align: 'right',
                    verticalAlign: 'middle',
                    y: -20,
                    x: -100
                },

                legend: {
                    enabled: false
                },
                xAxis: {
                    type: 'category'
                },
                yAxis: {
                    opposite: true,
                    tickPixelInterval: 150,
                    title: {
                        text: null
                    }
                },
                plotOptions: {
                    series: {
                        animation: false,
                        groupPadding: 0,
                        pointPadding: 0.1,
                        borderWidth: 0,
                        colorByPoint: true,
                        dataSorting: {
                            enabled: true,
                            matchByName: true
                        },
                        type: 'bar',
                        dataLabels: {
                            enabled: true
                        }
                    }
                },
                series: [
                    {
                        type: 'bar',
                        name: startYear,
                        data: getData(startYear)[1]
                    }
                ],
                responsive: {
                    rules: [{
                        condition: {
                            maxWidth: 550
                        },
                        chartOptions: {
                            xAxis: {
                                visible: false
                            },
                            subtitle: {
                                x: 0
                            },
                            plotOptions: {
                                series: {
                                    dataLabels: [{
                                        enabled: true,
                                        y: 8
                                    }, {
                                        enabled: true,
                                        format: '{point.name}',
                                        y: -8,
                                        style: {
                                            fontWeight: 'normal',
                                            opacity: 0.7
                                        }
                                    }]
                                }
                            }
                        }
                    }]
                }
            });
        })();

        /*
         * Pause the timeline, either when the range is ended, or when clicking the pause button.
         * Pausing stops the timer and resets the button to play mode.
         */
        function pause(button) {
            button.title = 'play';
            button.className = 'fa fa-play';
            clearTimeout(chart.sequenceTimer);
            chart.sequenceTimer = undefined;
        }

        /*
         * Update the chart. This happens either on updating (moving) the range input,
         * or from a timer when the timeline is playing.
         */
        function update(increment) {
            if (increment) {
                input.value = parseInt(input.value, 10) + increment;
            }
            if (input.value >= endYear) {
                // Auto-pause
                pause(btn);
            }

            chart.update(
                {
                    subtitle: {
                        text: getSubtitle()
                    }
                },
                false,
                false,
                false
            );

            chart.series[0].update({
                name: input.value,
                data: getData(input.value)[1]
            });
        }

        /*
         * Play the timeline.
         */
        function play(button) {
            button.title = 'pause';
            button.className = 'fa fa-pause';
            chart.sequenceTimer = setInterval(function () {
                update(1);
            }, 500);
        }

        btn.addEventListener('click', function () {
            if (chart.sequenceTimer) {
                pause(this);
            } else {
                play(this);
            }
        });
        /*
         * Trigger the update on the range bar click.
         */
        input.addEventListener('click', function () {
            update();
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

#map-container {
    text-align: center;
    position: relative;
    left: 50px;
    height: 610px;
    width: 1200px;
}
.TweetView{
    width: 100%;
    height: 100%;
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
