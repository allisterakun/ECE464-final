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
import Notifications from 'vue-notification'


// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
Vue.use(VueRouter);
Vue.use(Vuex);
Vue.use(VueCookie);
Vue.use(Notifications);
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
    count: 0,
    isLoggedin:false
  },
  mutations: {
    increment (state) {
      state.count++
    },
    login(state){
      state.isLoggedin = true;
    }
  }
})

store.commit('increment')
console.log(store.state.count);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

