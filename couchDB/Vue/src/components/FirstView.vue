<template>
    <div>
        <button @click="getData1">获取数据</button> <!--  click envent will trigger get data 1 method-->
        <h1>This is 1st View</h1>
        <ul>
            <li v-for="(item, index) in data" :key="index">{{ item }}</li> <!-- dynamically updated -->
        </ul>
        <button @click="getData2">获取数据</button>
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
            data: [],
        };
    },
    methods: {
        async getData1() { // get data 1 method calls api GET that backends implemented
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
        },
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
</style>
