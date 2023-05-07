import { createApp } from 'vue'
import App from './App.vue'
import HighchartsVue from 'highcharts-vue'
import Highcharts from 'highcharts'
import router from './router/index.js'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

const app = createApp(App);
app.use(router);
app.use(Highcharts);
app.use(HighchartsVue);
app.mount('#app');