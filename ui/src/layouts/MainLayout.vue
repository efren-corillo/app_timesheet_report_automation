<template>
	<q-layout view="lHh Lpr lFf">
		<q-header elevated>
			<q-toolbar>
				<q-btn
					flat
					dense
					round
					@click="toggleLeftDrawer"
					icon="menu"
					aria-label="Menu"
				/>
				<q-space/>
				<div class="q-gutter-sm row items-center no-wrap">
					<q-btn round dense flat color="white" :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'"
					       @click="$q.fullscreen.toggle()"
					       v-if="$q.screen.gt.sm">
					</q-btn>
					<q-btn round dense flat color="white" icon="fab fa-github" type="a"
					       href="https://github.com/efren-corillo" target="_blank">
					</q-btn>
					<q-btn round dense flat color="white" icon="notifications">
						<q-badge color="red" text-color="white" floating>
							5
						</q-badge>
						<q-menu
						>
							<q-list style="min-width: 100px">
								<messages></messages>
								<q-card class="text-center no-shadow no-border">
									<q-btn label="View All" style="max-width: 120px !important;" flat dense
									       class="text-indigo-8"></q-btn>
								</q-card>
							</q-list>
						</q-menu>
					</q-btn>
					<q-btn round flat>
						<q-avatar size="26px">
							<img alt="logo" src="https://cdn.quasar.dev/img/boy-avatar.png" />
						</q-avatar>
					</q-btn>
				</div>
			</q-toolbar>
		</q-header>

		<q-drawer
			v-model="leftDrawerOpen"
			show-if-above
			bordered
			class="bg-primary text-white"
		>
			<q-list>
				<q-toolbar class="bg-primary text-white shadow-2 text-center">
						<q-toolbar-title>Timesheet App</q-toolbar-title>
				</q-toolbar>
				<q-item v-for="item in sideMenu" :to="item.to" active-class="q-item-no-link-highlighting">
					<q-item-section avatar>
						<q-icon :name="item.icon"/>
					</q-item-section>
					<q-item-section>
						<q-item-label>{{ item.label }}</q-item-label>
					</q-item-section>
				</q-item>

				<!--				<q-item to="/Calendar" active-class="q-item-no-link-highlighting">-->
				<!--					<q-item-section avatar>-->
				<!--						<q-icon name="date_range"/>-->
				<!--					</q-item-section>-->
				<!--					<q-item-section>-->
				<!--						<q-item-label>Timesheet</q-item-label>-->
				<!--					</q-item-section>-->
				<!--				</q-item>-->
				<!--        not completed-->
				<!--        <q-item to="/Taskboard" active-class="q-item-no-link-highlighting">-->
				<!--          <q-item-section avatar>-->
				<!--            <q-icon name="done"/>-->
				<!--          </q-item-section>-->
				<!--          <q-item-section>-->
				<!--            <q-item-label>Taskboard</q-item-label>-->
				<!--          </q-item-section>-->
				<!--        </q-item>-->
			</q-list>
		</q-drawer>

		<q-page-container class="bg-grey-2">
			<router-view/>
		</q-page-container>
	</q-layout>
</template>
<script>
	import {defineComponent, ref} from 'vue'

	export default defineComponent({
		name: 'MainLayout'
	})
</script>
<script setup>
	import EssentialLink from 'components/EssentialLink.vue'
	import Messages from "./Messages.vue";

	import {defineComponent, ref} from 'vue'
	import {useQuasar} from "quasar";

	const leftDrawerOpen = ref(false)
	const $q = useQuasar()
	const sideMenu = [
		{
			to: '/',
			label: 'Dashboard',
			icon: 'dashboard'
		},
		{
			to: '/timesheet',
			label: 'Timesheets',
			icon: 'date_range'
		},
		{
			to: '/contractors',
			label: 'Contractors',
			icon: 'supervisor_account'
		},
	]
	const toggleLeftDrawer = () => {
		leftDrawerOpen.value = !leftDrawerOpen.value
	}
</script>

<style>

	/* FONT AWESOME GENERIC BEAT */
	.fa-beat {
		animation: fa-beat 5s ease infinite;
	}

	@keyframes fa-beat {
		0% {
			transform: scale(1);
		}
		5% {
			transform: scale(1.25);
		}
		20% {
			transform: scale(1);
		}
		30% {
			transform: scale(1);
		}
		35% {
			transform: scale(1.25);
		}
		50% {
			transform: scale(1);
		}
		55% {
			transform: scale(1.25);
		}
		70% {
			transform: scale(1);
		}
	}

</style>