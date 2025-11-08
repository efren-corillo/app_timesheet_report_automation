<template>
	<q-page class="flex flex-center">

		<q-btn @click="generateTimesheet" :loading="generateBtnClicked" class="q-mt-xl" color="white" text-color="blue" unelevated label="Generate Report" no-caps />
	</q-page>
</template>

<script setup>
	import { ref } from 'vue';
	import { api } from 'boot/axios.js';
	import { useQuasar } from 'quasar';

	const $q = useQuasar();
	const generateBtnClicked = ref(false);
	const generateTimesheet = () => {
		generateBtnClicked.value = !generateBtnClicked.value;

		api.get('/generate-weekly-report').then((res) => {
			console.log(res);
		}).catch(
			$q.notify({
				color: 'negative',
				position: 'top',
				message: 'Error: Could not generate report',
				icon: 'report_problem'
			})
		)

	}
</script>