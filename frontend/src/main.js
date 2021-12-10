import Vue from 'vue'
import App from './App.vue'
import Login from './Login.vue'
import HomePageM from './HomePageM.vue'
import { BootstrapVue } from 'bootstrap-vue'
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import VueCookie from 'vue-cookie'


// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(VueCookie);
Vue.config.productionTip = false


const routes = [
  { path: '/', component: Login },
  { path: '/homepageM', component: HomePageM}
]

const router = new VueRouter({
  routes // short for `routes: routes`
})

const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment (state) {
      state.count++
    }
  }
})

store.commit('increment')
console.log(store.state.count);

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

