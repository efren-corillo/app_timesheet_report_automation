import { createApp, h } from 'vue'
import { Quasar } from 'quasar'
import 'quasar/src/css/index.sass'

const App = { render: () => h('div', 'Hello Quasar!') }
createApp(App).use(Quasar, {}).mount('#q-app')