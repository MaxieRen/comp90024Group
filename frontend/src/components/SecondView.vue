<template>
    <div>
        <h1>Industries</h1>
        <div ref="chart" style="height: 300px;"></div>
        <button @click="getData1">更新图表</button>
        <ul>{{string}}</ul>
        <button @click="getData2">修改数据</button>
    </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
    name: 'SecondView',
    props: {
        msg: String,
    },
    data() {
        return {
            string: 'nothing',
            chart: null,
            chartData: [5, 20, 36, 10, 10, 20]
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://127.0.0.1:8081/api_2');
                console.log(response.data);
                this.chartData = response.data;
                this.updateChart();
            } catch (error) {
                console.log(error);
            }
        },
        async getData2() {
            try {
                this.string = this.string + 'sth'
            } catch (error) {
                console.log(error);
            }
        },
        updateChart() {
            this.chart.setOption({
                xAxis: {
                    type: 'category',
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                },
                yAxis: {
                    type: 'value',
                },
                series: [
                    {
                        data: this.chartData,
                        type: 'line',
                    },
                ],
            });
        },
    },
    mounted() {
        this.chart = echarts.init(this.$refs.chart);
        this.updateChart();
    }
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
