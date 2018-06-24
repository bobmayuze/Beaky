import Vue from 'vue';
import App from './App.vue';
import router from './router';
import vueResource from 'vue-resource';
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import round from "vue-round-filter";

Vue.use(VueMaterial);
Vue.use(vueResource);

Vue.config.productionTip = false;

new Vue({
  filters: {
    round,
  },
  router,
  render: (h) => h(App),
}).$mount('#app');
