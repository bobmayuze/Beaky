import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import About from './views/About.vue';
import Publish from './views/Publish.vue';
import Voter from './views/Voter.vue';
import Subscriber from './views/Subscriber.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/main',
      name: 'about',
      component: About,
    },
    {
      path: '/publish',
      name: 'publish',
      component: Publish,
    },
    {
      path: '/voter',
      name: 'voter',
      component: Voter,
    },
    {
      path: '/subscriber',
      name: 'subscriber',
      component: Subscriber,
    },
  ],
});
