// import './plugins/bootstrap-vue'
// import './plugins/bootstrap-vue'
// import './plugins/bootstrap-vue'
// import './plugins/bootstrap-vue'
// import './plugins/bootstrap-vue'

// import Vue from "vue";
// import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

// // Import Bootstrap an BootstrapVue CSS files (order is important)
// import "bootstrap/dist/css/bootstrap.css";
// import "bootstrap-vue/dist/bootstrap-vue.css";

// // Make BootstrapVue available throughout your project
// Vue.use(BootstrapVue);
// // Optionally install the BootstrapVue icon components plugin
// Vue.use(IconsPlugin);

// import './plugins/axios'

// import { createApp } from 'vue'

// const app = createApp({
//   // root instance definition
// });

// import App from './App.vue'
// createApp(App).mount('#app')

// import "./plugins/bootstrap-vue";


// import Vue from "vue";
// import "./plugins/axios";
// import App from "./App.vue";

// Vue.config.productionTip = false;

// new Vue({
//   render: h => h(App)
// }).$mount("#app");


import Vue from "vue";
import "./plugins/axios";
import App from "./App.vue";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

// Import Bootstrap an BootstrapVue CSS files (order is important)
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.config.productionTip = false;

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);

new Vue({
  render: h => h(App)
}).$mount("#app");
