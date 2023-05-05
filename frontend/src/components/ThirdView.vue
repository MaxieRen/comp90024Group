<template>
    <div>
        <div id="map" style="height: 500px"></div>
        <button @click="getData1">更新地图</button>
        <h3>This is 3rd View</h3>
        <ul>{{string}}</ul>
        <button @click="getData2">修改数据</button>
    </div>
</template>

<script>
import axios from 'axios';
import mapboxgl from 'mapbox-gl';

export default {
    name: 'ThirdView',
    props: {
        msg: String
    },
    data() {
        return {
            data: [],
            map: null,
            mapData: null
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://127.0.0.1:8081/api_1');
                console.log(response.data);
                this.data = response.data;
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
        mapboxgl.accessToken = 'pk.eyJ1Ijoibnl0Z3JhcGhpY3MiLCJhIjoiY2o5YTl2N29jMTBsZDM0cDl5NW50MXo5aCJ9.XWVKJju1tz6kSBXkeWJzwg';
        this.map = new mapboxgl.Map({
            container: 'map',
            style: 'mapbox://styles/nytgraphics/cj9ospgyg4lw42rnsd7k0vmxt',
            center: [132, -28],
            zoom: 3,
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
a {
    color: #42b983;
}
map {
    text-align: left;
    position: absolute;
    background-color: white;
    border: 1px solid #ccc;
    z-index: 1000001;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.5);
    pointer-events: none;
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
