<template>
	<div>

	</div>
</template>

<script setup>
	import { onMounted, ref } from 'vue';
	import { api } from 'boot/axios.js';

	const contractors = ref([]);

	onMounted(() => {
		api.get('/get-contractors').then((res) => {
			console.log(res);
		})
	});
</script>

<style lang="scss" scoped>

</style>