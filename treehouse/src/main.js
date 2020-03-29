import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';

Vue.config.productionTip = false


//import { Icon } from 'leaflet'

import { LMap, LTileLayer, LMarker,LPolyline,LCircleMarker ,LIcon , LPopup} from 'vue2-leaflet';
import 'leaflet/dist/leaflet.css'
import L from 'leaflet';

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

Vue.component('l-map', LMap);
Vue.component('l-tile-layer', LTileLayer);
Vue.component('l-marker', LMarker);
Vue.component('l-circle-marker', LCircleMarker);
Vue.component('l-polyline', LPolyline);
Vue.component('l-icon', LIcon);
Vue.component('l-popup', LPopup);



new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
