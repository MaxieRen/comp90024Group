<template>
    <div>
        <h2>All Regions (ABS SA4)</h2>
        <ul>
            <li v-for="(item, index) in data" :key="index">{{ item }}</li> <!-- dynamically updated -->
        </ul>
        <div class="container-fluid">
            <button @click="getData1">获取数据</button> <!--  click event will trigger get data 1 method-->
            <button @click="getData2">update</button>
            <button class="button-13" role="button" @click="getData3">获取数据</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'FirstView',
    props: {
        msg: String
    },
    data() {
        return {
            data: [56,41,53,37,43],
        };
    },
    methods: {
        async getData1() { // get data 1 method calls api GET that backends implemented
            try {
                this.data = [56,41,53,37,43];
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
        },
        async getData3() {
            try {
                this.data = [1,2,3,4,5,6,7,8];
            } catch (error) {
                console.log(error);
            }
        }
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
