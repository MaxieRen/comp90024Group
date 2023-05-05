import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

const app = createApp(App);
app.use(router); // 在应用程序中使用路由

app.mount('#app');

